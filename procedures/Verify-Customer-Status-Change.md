---
tags:
  - csrf
  - shopify
  - verification
  - wholesale
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:50.023Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7351019d-8fe3-4758-bc7d-9d99359a9361
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Verify Customer Status Change

## Summary

This procedure confirms the success of the CSRF attack by refreshing the Wholesale app's customer section to observe the unauthorized status update and token generation.

## Description

Post-execution of the CSRF PoC, this validation step checks the impact on the target customer in Shopify's Wholesale app. It involves reloading the relevant page to see the status shift to 'invited' and the creation of an invite link. This demonstrates the vulnerability's effect, such as potential spam invitations or unauthorized access facilitation. Environment: Shopify admin web interface. Outcomes: Visible proof of exploitation, with token usable for further testing.

## Requirements

1. Completed CSRF execution from prior procedure
2. Access to Wholesale app customer section
3. ~30 seconds wait time post-PoC

## Defense

Defensive measures and detection strategies:

- Implement real-time notifications for status changes in Wholesale customers
- Review invitation logs for patterns indicating CSRF (e.g., no referrer from admin)

## Objectives

1. Confirm status updated to 'invited'
2. Retrieve generated invitation token
3. Assess potential for further exploitation

## Instructions

### Step 1: Wait for Processing

**Context**: Allow Shopify backend time to process the forged request.

Pause for about 30 seconds after the PoC loads to ensure the invitation is generated.

> Expected: No immediate feedback needed; proceed to refresh.

### Step 2: Refresh Customer Section

**Context**: Reload the Wholesale customers page to view changes.

Navigate to Wholesale app > Customers and refresh the page (Ctrl+R or browser refresh).

> Expected: Target customer now shows status 'invited'.

### Step 3: Inspect Invitation Details

**Context**: Verify token generation and potential impact.

Click on the customer record to view details; note the generated invite link and any associated token.

> Expected: Invite link present; status confirmed changed from initial state.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[status-change]]
- [[token-generation]]
