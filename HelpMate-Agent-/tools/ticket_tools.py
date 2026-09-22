import json
import os
from datetime import datetime


TICKETS_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "tickets.json"
)
def create_ticket(
    issue: str,
    category: str,
    priority: str,
    troubleshooting_attempted: str,
    user_id: str
) -> str:

    # Read existing tickets
    if os.path.exists(TICKETS_FILE):
        with open(TICKETS_FILE, "r") as file:
            data = json.load(file)
    else:
        data = {"tickets": []}

    tickets = data["tickets"]

    # Generate ticket ID
    ticket_number = 1040 + len(tickets)
    ticket_id = f"HD-{ticket_number}"

    # Decide assigned team
    if category.lower() == "network":
        assigned_team = "Network Support"
    elif category.lower() == "accounts":
        assigned_team = "Identity Support"
    elif category.lower() == "devices":
        assigned_team = "Desktop Support"
    elif category.lower() == "software":
        assigned_team = "Software Support"
    else:
        assigned_team = "IT Support"

    # Create ticket
    ticket = {
        "ticket_id": ticket_id,
        "user_id": user_id,
        "issue": issue,
        "priority": priority,
        "status": "Open",
        "assigned_team": assigned_team,
        "troubleshooting_attempted": troubleshooting_attempted
    }

    # Add ticket to the tickets list
    tickets.append(ticket)

    # Save updated data
    with open(TICKETS_FILE, "w") as file:
        json.dump(data, file, indent=4)

    # Return result
    return json.dumps({
        "success": True,
        "ticket_id": ticket_id,
        "status": "Open",
        "message": f"Ticket {ticket_id} has been created."
    })

if __name__ == "__main__":
    result = create_ticket(
        issue="Account is still locked",
        category="Accounts",
        priority="Medium",
        troubleshooting_attempted="Confirmed username and stopped repeated sign-in attempts",
        user_id="USR-1001"
    )

    print(result)