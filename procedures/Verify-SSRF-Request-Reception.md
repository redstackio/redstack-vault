---
id: proc-uuid-004
tags:
  - ssrf
  - verification
  - poc
type: procedure
tools:
  - '[[tools/Flask]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Linux
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:02.503Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-SSRF-Request-Reception

## Summary

Confirms SSRF by checking server logs and curl output for successful internal redirection and response.

## Description

After executing the curl request, verify that the local server received the request to localhost, proving the hostname was parsed as 127.0.0.1.

## Requirements

1. Running Flask server from prior step
2. Curl verbose output captured
3. Access to server console

## Defense

Defensive measures and detection strategies:

- Implement request logging in applications
- Detect anomalies in resolved IP vs. requested hostname

## Objectives

1. Validate encoding conversion occurred
2. Confirm internal access
3. Assess potential for further exploitation

## Instructions

### Step 1: Check Curl Output

**Context**: Review connection details.

Look for 'Connected to 127.0.0.1' and HTTP 200 with 'FindVuln'.

### Step 2: Inspect Server Logs

**Context**: Confirm request arrival.

In Flask terminal, observe GET / request log.

**Expected Output**: '127.0.0.1 - - [date] "GET / HTTP/1.1" 200 -'.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Flask]]

## Tags

- [[ssrf]]
- [[verification]]
