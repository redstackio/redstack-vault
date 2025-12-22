---
tags:
  - request-forwarding
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Content-Type-Converter]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: ded17512-64b8-4e40-aef7-0ba9351b2cbc
created_at: '2025-12-11T06:10:31.056Z'
updated_at: '2025-12-11T06:10:31.056Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Forward Modified Request

## Summary

This procedure sends the altered JSON request to the GitLab server, triggering the password reset emails to both addresses.

## Description

After modification, forward the request using Burp Suite to execute the exploit. The server will process the array and send reset links accordingly. This step completes the exploitation phase in a GitLab web environment.

## Requirements

1. Modified request in Burp Suite
2. Active interception
3. Server accessibility

## Defense

Defensive measures and detection strategies:

- Monitor for anomalous reset requests
- Implement array rejection in inputs

## Objectives

1. Send modified request
2. Trigger email dispatch
3. Advance to link usage

## Instructions

### Step 1: Forward in Burp

**Context**: Click 'Forward' in Burp Suite to send the request.

> Observe the server response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- request-forwarding
