---
id: proc-uuid-3
tags:
  - unauthorized-post
  - vote-creation
type: procedure
tools:
  - '[[tools/cURL]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-create-vote]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:20.016Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create Unauthorized Vote via POST Request

## Summary

This procedure sends a crafted POST request to HackerOne's vote endpoint to create a vote on a Hacktivity report without proper authorization, exploiting the lack of server-side checks.

## Description

The endpoint https://hackerone.com/reports/[Report_ID]/votes accepts POST requests to create votes. Since it relies on client-side validation, any user can send a direct request with a simple JSON payload indicating a vote (e.g., true for upvote). This allows manipulation of report scores if the feature were active.

## Requirements

1. Target report ID from HackerOne Hacktivity
2. cURL or similar HTTP client
3. Internet access to hackerone.com

## Defense

Defensive measures and detection strategies:

- Add server-side authentication and authorization checks (e.g., verify user permissions)
- Return 404 or 403 for unreleased features
- Implement request signing or CSRF tokens

## Objectives

1. Create a vote on a specified report
2. Confirm successful unauthorized access
3. Demonstrate potential ranking manipulation

## Instructions

### Step 1: Prepare and Send POST Request

**Context**: Use cURL to send the vote creation request.

Execute [[commands/curl-create-vote]] to POST to the endpoint:

```bash
curl -X POST https://hackerone.com/reports/[Report_ID]/votes -H "Content-Type: application/json" -d '{"vote": true}'
```

> Expected output: HTTP 200/201 with vote confirmation, e.g., {"success": true, "vote_id": "123"}.

### Step 2: Verify Vote Creation

**Context**: Check the response for success and note any returned ID.

Inspect the response headers and body for creation status.

> If successful, the vote is applied without permission checks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-create-vote]]

## Tools Used

- [[tools/cURL]]

## Tags

- [[unauthorized-post]]
- [[vote-creation]]
