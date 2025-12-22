---
id: proc-uuid-002
tags:
  - xss
  - request-submission
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:31.806Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit Malicious Project Join Request

## Summary

This procedure submits a join request to a Localize project using a translator account with an injected XSS payload, embedding the malicious name in the backend data for later reflection.

## Description

Once the translator name is tainted, requesting to join a project transmits the unsanitized input to the server, where it is stored in the pending invites queue. The admin review interface then renders this data without escaping, setting up the XSS trigger. This step relies on the platform's lack of server-side validation for join requests and assumes the attacker knows or targets a specific project.

## Requirements

1. Translator account with malicious name configured
2. Knowledge of target project ID or name
3. Network access to Localize web application

## Defense

Defensive measures and detection strategies:

- Sanitize all inputs on server-side before storage (e.g., strip HTML tags)
- Rate-limit join requests per user to prevent abuse
- Log and alert on requests containing script-like patterns (e.g., <svg>)

## Objectives

1. Transmit payload via join request
2. Ensure inclusion in pending invites without rejection
3. Position payload for admin exposure

## Instructions

### Step 1: Select Target Project

**Context**: Identify and navigate to the project join interface.

- From the translator dashboard, search for the target project.
- Ensure you do not have prior access to it.

### Step 2: Initiate Join Request

**Context**: Submit the request, including the tainted name in the payload.

Click 'Request to Join' or fill any required form fields.

> The name field from your profile is automatically included in the request data sent via POST or similar.

### Step 3: Confirm Submission

**Context**: Verify the request is pending.

- Look for a success message like 'Request sent'.
- If possible, use another account to check pending invites.

> Expected output: Request status shows as pending; no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web-request]]
