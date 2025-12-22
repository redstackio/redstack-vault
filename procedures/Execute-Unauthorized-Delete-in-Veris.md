---
tags:
  - deletion
  - impact
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-veris-delete]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data Destruction]]'
updated_at: '2025-12-14T17:25:23.215Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 12a3f900-5689-424b-b518-927b56a7c49a
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Data Destruction]]'
---
# Execute Unauthorized Delete in Veris

## Summary

This procedure submits the modified delete request to the Veris application, resulting in the unauthorized removal of a target organization's terminal or gatekeeper, confirming the critical IDOR impact.

## Description

With the ID altered to reference an unauthorized asset, replaying the request exploits the lack of permission checks in the Veris delete endpoint. This leads to immediate service disruption for the victim organization. The attack requires an active authenticated session and assumes the modified request is valid. Target environment: Veris web API over HTTPS. Expected outcome: Successful deletion response and verifiable asset removal.

## Requirements

1. Modified delete request with target ID
2. Valid authentication token
3. Ability to verify deletion (e.g., via UI or API query)

## Defense

Defensive measures and detection strategies:

- Enforce strict access controls with user-org matching on every endpoint
- Alert on delete operations crossing organizational boundaries
- Implement audit logs for all deletions with rollback capabilities

## Objectives

1. Achieve unauthorized data destruction
2. Disrupt target operations
3. Validate the full IDOR chain

## Instructions

### Step 1: Replay via Proxy

**Context**: Send the modified request using Burp Repeater to observe the response.

Click 'Send' in Repeater; check response for success codes.

> Expected output: 200/204 status with confirmation message (e.g., {"deleted": true}).

### Step 2: Verify Deletion

**Context**: Confirm the asset is removed from the target organization.

Query the Veris UI or API for the asset ID; use [[commands/curl-veris-delete]] if crafting directly:

```bash
curl -X DELETE -H "Authorization: Bearer YOUR_TOKEN" "https://veris.example.com/api/terminals/UNAUTHORIZED_ID/delete"
```

> Expected output: Asset no longer accessible; error on subsequent access attempts.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Data Destruction]]

### Sub-Techniques


## Commands Used

- [[commands/curl-veris-delete]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[deletion]]
- [[Impact]]
- [[web]]
