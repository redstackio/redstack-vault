---
tags:
  - http-smuggling
  - verification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 76ed84d1-21b1-4183-a970-a9e7ff8a7700
created_at: '2025-12-13T09:01:22.160Z'
updated_at: '2025-12-13T09:01:22.160Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe and Verify Smuggled Response

## Summary

This procedure focuses on observing and verifying the server's response to a smuggled HTTP request, confirming the vulnerability by checking for multiple responses in one connection.

## Description

After sending the smuggled request, the server should return two responses (e.g., 302 and 200), indicating that the back-end processed the hidden request. This confirms the smuggling success and opens avenues for further attacks like cache poisoning.

## Requirements

1. Prior execution of smuggling request
2. Tool for capturing HTTP responses (e.g., Burp Suite)
3. Access to response logs

## Defense

Defensive measures and detection strategies:

- Implement strict HTTP validation and reject ambiguous requests
- Log and alert on multiple responses per connection

## Objectives

1. Confirm receipt of dual HTTP responses
2. Validate vulnerability exploitation
3. Assess potential impact

## Instructions

### Step 1: Monitor Response

**Context**: Analyze the output from the smuggling request to identify multiple HTTP status codes.

> Look for a 302 Found followed by a 200 OK in the response stream, confirming the smuggled request was executed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[http-smuggling]]
- [[verification]]
