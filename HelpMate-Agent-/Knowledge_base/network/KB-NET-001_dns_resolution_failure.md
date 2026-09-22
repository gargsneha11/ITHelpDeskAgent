# DNS Resolution Failure

Document ID: KB-NET-001
Title: DNS Resolution Failure
Category: Network > DNS
Priority: High
Version: 1.0
Status: Active
Owner: Network Support
Last Updated: 2026-09-15

## Symptoms

- User can access some network resources but cannot open specific websites or internal services.
- Applications report that a hostname cannot be found.
- User can access a service by IP address but not by hostname.

## Possible Causes

1. Incorrect DNS configuration.
2. DNS server is unavailable.
3. Local DNS cache contains outdated information.
4. Network connectivity problem.
5. Internal DNS record is missing or incorrect.

## Prerequisites

- User must have network connectivity.
- Support staff should have access to approved network diagnostic tools.
- DNS configuration should only be changed by authorized support personnel.

## Troubleshooting Steps

1. Confirm that the device has network connectivity.
2. Test access to another known service.
3. Check the DNS configuration on the device.
4. Clear the local DNS cache if appropriate.
5. Test hostname resolution using an approved diagnostic tool.
6. Compare results with another known-working device.
7. Check whether the affected hostname has a valid DNS record.

## Resolution

Hostname resolution succeeds and the user can access the affected service.

## Escalation

Escalate to Network Support if:

- The organization's DNS server is unavailable.
- Multiple users are affected.
- An internal DNS record appears incorrect or missing.
- DNS resolution continues to fail after local troubleshooting.

## Security Notes

Do not modify DNS settings to unauthorized external servers without approval.