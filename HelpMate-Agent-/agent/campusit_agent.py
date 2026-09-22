import json

from azure.identity import AzureCliCredential
from azure.ai.projects import AIProjectClient

from tools.ticket_tools import create_ticket
from tools.ticket_status_tool import get_ticket_status
from tools.check_service_status import check_service_status


PROJECT_ENDPOINT = (
    "https://sneha-agent-resource.services.ai.azure.com/"
    "api/projects/sneha-agent"
)

AGENT_NAME = "Sneha-agent"


credential = AzureCliCredential()

project = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=credential
)

openai_client = project.get_openai_client(
    agent_name=AGENT_NAME
)


def chat_with_agent(
    user_message,
    previous_response_id=None,
    user_id=None
):
    """
    Send a message to the CampusIT Foundry agent.

    user_id comes from the currently logged-in Django user.
    """

    if previous_response_id:

        response = openai_client.responses.create(
            input=user_message,
            previous_response_id=previous_response_id
        )

    else:

        response = openai_client.responses.create(
            input=user_message
        )

    # Process tool calls
    while True:

        tool_called = False

        for item in response.output:

            if item.type != "function_call":
                continue

            tool_called = True

            arguments = json.loads(item.arguments)

            print("Tool called:", item.name)

            # -----------------------------
            # CREATE TICKET
            # -----------------------------

            if item.name == "create_ticket":

                result = create_ticket(
                    issue=arguments["issue"],
                    category=arguments["category"],
                    priority=arguments["priority"],
                    troubleshooting_attempted=arguments[
                        "troubleshooting_attempted"
                    ],
                    user_id=user_id
                )

            # -----------------------------
            # TICKET STATUS
            # -----------------------------

            elif item.name == "get_ticket_status":

                result = get_ticket_status(
                    ticket_id=arguments["ticket_id"]
                )

            # -----------------------------
            # SERVICE STATUS
            # -----------------------------

            elif item.name == "check_service_status":

                result = check_service_status(
                    service=arguments["service"]
                )

            else:

                result = {
                    "success": False,
                    "message": "Unknown tool."
                }

            # Send tool result back to Foundry
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

            break

        if not tool_called:
            break

    return {
        "message": response.output_text,
        "response_id": response.id
    }