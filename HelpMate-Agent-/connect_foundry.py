from azure.identity import AzureCliCredential
from azure.ai.projects import AIProjectClient

endpoint = "https://sneha-agent-resource.services.ai.azure.com/api/projects/sneha-agent"

credential = AzureCliCredential()

project = AIProjectClient(
    endpoint=endpoint,
    credential=credential
)

print("Connected to Foundry project successfully!")

print("\nAvailable agents:")
for agent in project.agents.list():
    print("Name:", agent.name)
    print("ID:", agent.id)
    print("---")