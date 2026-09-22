import json
from azure.ai.projects.models import FunctionTool


def check_service_status(service: str) -> dict:
    """
    Check the current status of an IT service.
    """

    with open("data/services.json", "r") as file:
        data = json.load(file)

    services = data.get("services", [])

    for item in services:
        if item["service"].lower() == service.lower():
            return {
                "success": True,
                "service": item["service"],
                "status": item["status"]
            }

    return {
        "success": False,
        "service": service,
        "message": f"Service '{service}' was not found."
    }


check_service_status_tool = FunctionTool(
    name="check_service_status",
    description=(
        "Check the current status of an IT service such as campus Wi-Fi, "
        "student portal, email, or VPN."
    ),
    parameters={
        "type": "object",
        "properties": {
            "service": {
                "type": "string",
                "description": "The IT service whose status should be checked."
            }
        },
        "required": [
            "service"
        ],
        "additionalProperties": False
    },
    strict=True
)