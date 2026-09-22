from azure.identity import AzureCliCredential
from azure.ai.projects import AIProjectClient
from tools.ticket_tools import create_ticket
from tools.ticket_status_tool import get_ticket_status
from tools.check_service_status import check_service_status

import json

PROJECT_ENDPOINT = "https://sneha-agent-resource.services.ai.azure.com/api/projects/sneha-agent"
AGENT_NAME = "Sneha-agent"

# Demo user ID supplied by the application
CURRENT_USER_ID = "USR-1004"

credential = AzureCliCredential()

project = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=credential
)

openai_client = project.get_openai_client(
    agent_name=AGENT_NAME
)

print("CampusIT Agent is ready!")
print("Type 'exit' to stop.\n")

previous_response_id = None

while True:

    user_message = input("You: ")

    if user_message.lower() == "exit":
        print("Goodbye!")
        break

    # Send user message
    if previous_response_id:
        response = openai_client.responses.create(
            input=user_message,
            previous_response_id=previous_response_id
        )
    else:
        response = openai_client.responses.create(
            input=user_message
        )

        # Handle tool calls
    for item in response.output:

        if item.type == "function_call":

            print("\n[Tool called:", item.name, "]")

            arguments = json.loads(item.arguments)

            if item.name == "create_ticket":

                print("[Ticket arguments:", arguments, "]")

                result = create_ticket(
                    issue=arguments["issue"],
                    category=arguments["category"],
                    priority=arguments["priority"],
                    troubleshooting_attempted=arguments[
                        "troubleshooting_attempted"
                    ],
                    user_id=CURRENT_USER_ID
                )

            elif item.name == "get_ticket_status":

                result = get_ticket_status(
                    ticket_id=arguments["ticket_id"]
                )

            elif item.name == "check_service_status":

                result = check_service_status(
                    service=arguments["service"]
                )

            else:
                continue

            # Send tool result back to the agent
            response = openai_client.responses.create(
                input=[
                    {
                        "type": "function_call_output",
                        "call_id": item.call_id,
                        "output": json.dumps(result)
                    }
                ],
                previous_response_id=response.id
            )

    previous_response_id = response.id

    print("Agent:", response.output_text)
    print()