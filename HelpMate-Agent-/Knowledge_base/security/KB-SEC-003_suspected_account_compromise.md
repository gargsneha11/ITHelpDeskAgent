# Suspected Account Compromise

Document ID: KB-SEC-003
Title: Suspected Account Compromise
Category: Security > Identity Security
Priority: Critical
Version: 1.0
Status: Active
Owner: Security Operations
Last Updated: 2026-09-15

## Symptoms

- User reports an unexpected login notification.
- User sees activity they do not recognize.
- MFA approval requests appear without the user initiating a login.
- Password or account settings appear to have changed unexpectedly.

## Possible Causes

1. Stolen credentials.
2. Phishing attack.
3. Password reused on another compromised service.
4. Unauthorized access to the user's account.

## Prerequisites

- User identity must be verified using the approved process.
- Do not request the user's password or MFA code.
- Follow the organization's security incident-response procedure.

## Troubleshooting Steps

1. Ask the user whether they recognize the reported login activity.
2. Ask the user not to approve unexpected MFA requests.
3. Check account activity using approved security tools.
4. If compromise is suspected, follow the approved account-containment procedure.
5. Require a password reset through the approved process when instructed.
6. Review active sessions or tokens when supported by the organization's identity system.
7. Escalate the incident to Security Operations.

## Resolution

The account is secured and Security Operations confirms that unauthorized access has been contained.

## Escalation

Immediately escalate to Security Operations if:

- Unauthorized access is confirmed.
- Sensitive information may have been accessed.
- Unexpected MFA requests continue.
- Account settings were changed without authorization.

## Security Notes

Never request or record passwords, MFA codes, recovery codes, or other authentication secrets.