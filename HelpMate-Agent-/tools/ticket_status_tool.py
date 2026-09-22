import json
from azure.ai.projects.models import FunctionTool


def get_ticket_status(ticket_id: str) -> dict:
    """
    Get the current status and details of an IT support ticket.
    """

    with open("data/tickets.json", "r") as file:
        data = json.load(file)

    tickets = data.get("tickets", [])

    for ticket in tickets:
        if ticket["ticket_id"].upper() == ticket_id.upper():
            return {
                "success": True,
                "ticket_id": ticket["ticket_id"],
                "status": ticket["status"],
                "issue": ticket["issue"],
                "priority": ticket["priority"],
                "assigned_team": ticket["assigned_team"]
            }

    return {
        "success": False,
        "ticket_id": ticket_id,
        "message": f"Ticket {ticket_id} was not found."
    }


get_ticket_status_tool = FunctionTool(
    name="get_ticket_status",
    description=(
        "Get the current status and details of an existing IT support ticket "
        "using its ticket ID."
    ),
    parameters={
        "type": "object",
        "properties": {
            "ticket_id": {
                "type": "string",
                "description": "The ticket ID, such as HD-1043."
            }
        },
        "required": [
            "ticket_id"
        ],
        "additionalProperties": False
    },
    strict=True
)