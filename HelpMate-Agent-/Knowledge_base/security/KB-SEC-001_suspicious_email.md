# Suspicious Email

Document ID: KB-SEC-001
Title: Suspicious Email
Category: Security > Email Security
Priority: High
Version: 1.0
Status: Active
Owner: Security Operations
Last Updated: 2026-09-15

## Symptoms

- User receives an unexpected email requesting credentials or sensitive information.
- Email contains suspicious links or attachments.
- Sender address appears unusual or does not match the expected organization.
- Message creates urgency or threatens consequences if the user does not act.

## Possible Causes

1. Phishing attempt.
2. Malicious attachment.
3. Spoofed sender address.
4. Compromised external account.

## Prerequisites

- User should not interact further with the suspicious message.
- Security support must have access to the approved email-security reporting mechanism.

## Troubleshooting Steps

1. Tell the user not to click links or open attachments.
2. Ask the user to report the message using the approved reporting mechanism.
3. Determine whether the user clicked a link or opened an attachment.
4. If the user interacted with the message, follow the organization's incident-response procedure.
5. Preserve the message for security investigation when required.

## Resolution

The suspicious message is reported and handled according to the organization's security process.

## Escalation

Escalate to Security Operations if:

- The user clicked a suspicious link.
- A suspicious attachment was opened.
- Credentials may have been entered.
- Multiple users received the same message.
- Malware infection is suspected.

## Security Notes

Never ask the user to send passwords, MFA codes, or other authentication secrets through email or chat.