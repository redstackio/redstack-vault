---
id: proc-uuid-003
tags:
  - mass-requests
  - idor
  - execution
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/send-connection-request-idor]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.121Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Sending-Mass-Connection-Requests

## Summary

This procedure automates sending thousands of connection requests to enumerated user IDs via a POST endpoint, exploiting IDOR to bypass authorization and set up data harvesting.

## Description

In the DoD website attack, the /██████ endpoint accepts RequesteeId parameters without validating the requester's permissions, allowing any authenticated user to target others. Burp Suite's Intruder tool is used to payload sequential IDs. Prerequisites: Enumerated ID list and active session. Expected outcomes: Pending requests that, upon acceptance, expose personal data.

## Requirements

1. List of enumerated user IDs
2. Burp Suite with captured base request
3. Auth tokens from login

## Defense

Defensive measures and detection strategies:

- Validate RequesteeId against requester's connections or permissions
- Implement rate limiting on connection requests per user
- Monitor for high-volume requests from single sessions

## Objectives

1. Initiate connections to target users
2. Flood system with requests for broad coverage
3. Await acceptances for data access

## Instructions

### Step 1: Capture Base Request

**Context**: Intercept a manual connection request to use as template.

Send a test request to a known ID via the website interface, captured in Burp.

> Base POST includes headers like Authorization-Code and body RequesteeId=known_id&RequestMessage=+

### Step 2: Automate with Intruder

**Context**: Use Burp Intruder to send mass requests.

In Intruder, mark RequesteeId as payload position, load sequential numbers (1-10000), and attack.

Execute [[commands/send-connection-request-idor]] for each, adapted in Repeater if needed:

```bash
# Simulated curl equivalent for Burp automation
curl -X POST https://█████████/██████ -H "Authorization-Code: b6315c0b-3f28-4b63-93de-b6a5a1c3db82" -d "RequesteeId=123&RequestMessage=+"
```

> Each response: {"Status": "Pending", "Id": 123}

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/send-connection-request-idor]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[mass-requests]]
- [[Execution]]
