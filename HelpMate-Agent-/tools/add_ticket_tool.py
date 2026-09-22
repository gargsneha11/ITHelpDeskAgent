from azure.ai.projects.models import FunctionTool

create_ticket_tool = FunctionTool(
    name="create_ticket",

    description=(
        "Create an IT support ticket when the user's issue cannot be resolved "
        "through the available troubleshooting steps and escalation is required."
    ),

    parameters={
        "type": "object",

        "properties": {
            "issue": {
                "type": "string",
                "description": "The user's IT issue."
            },

            "category": {
                "type": "string",
                "description": (
                    "The issue category, such as Accounts, Network, "
                    "Devices, or Software."
                )
            },

            "priority": {
                "type": "string",
                "description": (
                    "The ticket priority: Low, Medium, High, or Critical."
                )
            },

            "troubleshooting_attempted": {
                "type": "string",
                "description": "The troubleshooting steps already attempted."
            }
        },

        "required": [
            "issue",
            "category",
            "priority",
            "troubleshooting_attempted"
        ],

        "additionalProperties": False
    },

    strict=True
)