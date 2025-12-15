---
id: proc-uuid-4
tags:
  - unauthorized-delete
  - vote-removal
type: procedure
tools:
  - '[[tools/cURL]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-delete-vote]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:20.013Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Delete Vote via DELETE Request

## Summary

This procedure sends a DELETE request to remove a previously created vote from a Hacktivity report, confirming the endpoint's vulnerability to unauthorized modifications.

## Description

Using the vote ID obtained from creation, a DELETE request to https://hackerone.com/reports/[Report_ID]/votes/[VOTE_ID] removes the vote. The lack of server-side authorization allows any user to perform this action, enabling full control over votes.

## Requirements

1. Vote ID from prior creation step
2. Target report ID
3. cURL or HTTP client

## Defense

Defensive measures and detection strategies:

- Require ownership verification for vote deletions
- Log all DELETE operations with user context
- Disable endpoints during development

## Objectives

1. Remove a specific vote
2. Validate unauthorized deletion capability
3. Clean up test votes

## Instructions

### Step 1: Send DELETE Request

**Context**: Target the vote resource with the known ID.

Execute [[commands/curl-delete-vote]]:

```bash
curl -X DELETE https://hackerone.com/reports/[Report_ID]/votes/[VOTE_ID]
```

> Expected output: HTTP 200/204 with no content, indicating successful deletion.

### Step 2: Confirm Deletion

**Context**: Verify the vote is no longer active.

Check response status; optionally, attempt to create and list votes to confirm removal.

> Success if no error and status code indicates deletion.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-delete-vote]]

## Tools Used

- [[tools/cURL]]

## Tags

- [[unauthorized-delete]]
- [[vote-removal]]
