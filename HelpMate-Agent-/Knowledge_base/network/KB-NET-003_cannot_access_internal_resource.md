# Cannot Access Internal Network Resource

Document ID: KB-NET-003
Title: Cannot Access Internal Network Resource
Category: Network > Internal Resources
Priority: High
Version: 1.0
Status: Active
Owner: Network Support
Last Updated: 2026-09-15

## Symptoms

- User cannot access an internal website, application, or file share.
- External websites work normally.
- User receives an access, timeout, or connection error.

## Possible Causes

1. User is not connected to the organizational network.
2. VPN connection is not established.
3. DNS resolution failure.
4. User does not have permission to access the resource.
5. Internal service is unavailable.
6. Network routing or firewall issue.

## Prerequisites

- User must be authorized to access the internal resource.
- Remote users must have an approved VPN connection when required.
- Support staff should have access to approved account and network diagnostic tools.

## Troubleshooting Steps

1. Confirm that the user has network connectivity.
2. Determine whether the user is working on-site or remotely.
3. If remote, verify that the VPN connection is active.
4. Check whether the resource hostname resolves correctly.
5. Verify the user's account status.
6. Check whether other authorized users can access the resource.
7. Check the service status if monitoring information is available.

## Resolution

The user successfully accesses the required internal resource.

## Escalation

Escalate to Network or Application Support if:

- Multiple users cannot access the resource.
- VPN connectivity is functioning but the resource remains unavailable.
- DNS or routing problems are suspected.
- The internal service appears to be unavailable.
- The user requires access permissions they do not currently have.

## Security Notes

Do not bypass firewall, VPN, or access-control policies to restore connectivity.