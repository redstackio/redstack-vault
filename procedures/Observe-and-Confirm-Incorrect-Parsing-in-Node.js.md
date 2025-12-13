---
tags:
  - http-request-smuggling
  - verification
  - node-js
type: procedure
tools:
  - '[[tools/Node-js]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Node.js
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 8e05f98c-a485-4c94-9aee-5d025c2f155a
created_at: '2025-12-13T09:01:17.436Z'
updated_at: '2025-12-13T09:01:17.436Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe and Confirm Incorrect Parsing in Node.js

## Summary

This procedure involves analyzing the Node.js server's response to confirm the HTTP Request Smuggling vulnerability through incorrect handling of multi-line Transfer-Encoding headers.

## Description

After sending the crafted request, the server's JSON output is examined to verify that the header was not properly folded (replaced with spaces) and was parsed as 'chunked' with the body processed accordingly. This confirms the root cause: violation of RFC7230 section 3.2.4.

## Requirements

1. Completed prior steps with server running and request sent
2. Access to server console or output
3. Basic understanding of HTTP headers and parsing

## Defense

Defensive measures and detection strategies:

- Patch Node.js to ensure proper obs-fold replacement in headers
- Log and alert on anomalous header values or parsing discrepancies

## Objectives

1. Validate the vulnerability's presence
2. Document the impact on request processing
3. Assess potential for real-world exploitation

## Instructions

### Step 1: Review Server Output

**Context**: Check the JSON response from the server for parsing details.

> Examine the output showing 'transfer-encoding': 'chunked , identity', body length 1, and body 'a'. This indicates the parser did not replace the folded line with a space, leading to incorrect interpretation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Node-js]]

## Tags

- [[http-request-smuggling]]
- [[verification]]
