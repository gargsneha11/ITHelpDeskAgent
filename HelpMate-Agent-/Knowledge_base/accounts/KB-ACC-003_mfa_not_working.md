# Multi-Factor Authentication Is Not Working

Document ID: KB-ACC-003
Title: Multi-Factor Authentication Is Not Working
Category: Accounts > Multi-Factor Authentication
Priority: High
Version: 1.0
Status: Active
Owner: IT Service Desk
Last Updated: 2026-09-15

## Symptoms

- User enters the correct password but cannot complete MFA.
- Verification code is rejected.
- Push notification does not arrive.
- User has changed or lost their MFA device.

## Possible Causes

1. Incorrect or expired verification code.
2. Mobile device has no network connection.
3. MFA application is not synchronized.
4. MFA registration is outdated.
5. User replaced their phone.

## Prerequisites

- User identity must be verified according to organizational policy.
- Support staff must use the approved identity-management system.

## Troubleshooting Steps

1. Confirm that the user's account is active.
2. Ask the user to generate a new MFA code if applicable.
3. Verify that the user's device has network connectivity.
4. Check whether the MFA registration is current.
5. If the registered device was replaced, follow the approved MFA re-registration process.
6. Retry authentication.

## Resolution

MFA authentication succeeds and the user can access the required service.

## Escalation

Escalate to Identity and Access Support if:

- The MFA registration must be reset.
- The user cannot complete identity verification.
- Suspicious authentication activity is detected.

## Security Notes

- Never ask the user to provide an MFA verification code.
- Never approve an unexpected MFA request on behalf of a user.
- Report suspicious authentication activity according to security procedures.