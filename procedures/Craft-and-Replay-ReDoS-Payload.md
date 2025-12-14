---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - redos
  - payload-craft
  - dos
  - api-exploit
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:48.903Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Application or System Exploitation]]'
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Craft-and-Replay-ReDoS-Payload

## Summary

This procedure details crafting a malicious JSON payload with deeply nested parentheses in the 'name' parameter and replaying it via Burp Suite Repeater to exploit a ReDoS vulnerability in the CS.Money search API, leading to server-side computation overload and denial of service.

## Description

The search endpoint /api/skin/search on 3d.cs.money lacks input sanitization, allowing regex patterns vulnerable to catastrophic backtracking when processing inputs like deeply nested parentheses (e.g., ((((()0))))). This causes exponential time complexity in parsing, hanging the server. The procedure assumes a captured request and focuses on modification and replay, with impact scalable by nesting depth.

## Requirements

1. Captured legitimate request in Burp Repeater.
2. Understanding of JSON structure and regex behaviors.
3. Network access to the target API.
4. Burp Suite Repeater tab open.

## Defense

Defensive measures and detection strategies:

- Sanitize inputs by limiting nesting depth or using safe regex libraries (e.g., RE2).
- Implement request timeouts and rate limiting on API endpoints.
- Monitor server CPU usage and log slow queries to detect backtracking patterns.

## Objectives

1. Create a payload that triggers excessive regex computation.
2. Successfully replay the request to the vulnerable endpoint.
3. Achieve server hang without crashing the application.

## Instructions

### Step 1: Edit JSON Payload

**Context**: Modify the 'name' field to include nested parentheses.

In Repeater, locate the JSON body and replace the 'name' value with "((((()0))))))" for initial testing, or increase to "((((((()0))))))))" for deeper nesting.

### Step 2: Validate Payload

**Context**: Ensure the JSON remains valid before sending.

Check for syntax errors in the body; use Burp's raw view to confirm the Content-Type header is application/json;charset=utf-8.

### Step 3: Replay the Request

**Context**: Send the modified request to trigger the exploit.

Click the 'Send' button in Repeater to POST the payload to /api/skin/search.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques

- [[Application or System Exploitation]]

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[redos]]
- [[payload-craft]]
- [[dos]]
- [[api-exploit]]
