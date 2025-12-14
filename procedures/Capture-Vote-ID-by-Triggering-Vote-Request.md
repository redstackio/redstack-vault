---
id: proc-uuid-2
tags:
  - request-interception
  - vote-capture
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:20.021Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture Vote ID by Triggering Vote Request

## Summary

This procedure triggers a vote action on the manipulated Hacktivity page to generate and capture a vote ID from the server response, allowing identification of the resource for subsequent unauthorized operations like deletion.

## Description

After revealing the vote controls, clicking the vote button sends a POST request to the server, which assigns a unique vote ID if the request is processed. The attacker intercepts this using browser tools to note the ID, then immediately deletes the vote to minimize impact. This step confirms the endpoint's vulnerability to unauthorized requests.

## Requirements

1. Hidden vote button revealed from previous procedure
2. Browser developer tools for request interception
3. Target report ID on HackerOne Hacktivity

## Defense

Defensive measures and detection strategies:

- Enforce authentication on all vote endpoints
- Rate-limit requests to vote resources
- Audit logs for vote creations from unauthenticated sessions

## Objectives

1. Generate a vote ID via POST request
2. Intercept and record the ID for cleanup
3. Validate endpoint accessibility

## Instructions

### Step 1: Trigger Vote Action

**Context**: Click the enabled vote button to initiate the POST request.

In the browser, click the vote button on the target report.

> The Network tab in dev tools shows the POST request to /reports/[Report_ID]/votes.

### Step 2: Intercept and Note Vote ID

**Context**: Capture the response containing the new vote ID.

Filter the Network tab for the POST request, inspect the response body for the vote ID, and copy it. Then trigger a delete to remove the vote.

> Expected output: JSON response with vote object including ID, e.g., {"id": "vote-123"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[request-interception]]
- [[vote-capture]]
