---
id: uuid-4
tags:
  - replay
  - exploit
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite-Community-Edition]]'
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
updated_at: '2025-12-14T17:24:26.987Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send-Modified-POST-Request

## Summary

Transmits the tampered POST request to the AMA endpoint, triggering a 302 redirect based on the manipulated 'failed' parameter.

## Description

This simulates a failed form submission, causing the server to redirect using the unsanitized user input, confirming the open redirect vulnerability.

## Requirements

1. Modified request in Repeater
2. Target endpoint reachable

## Defense

Defensive measures and detection strategies:

- Implement redirect validation (e.g., domain checks)
- Log 302 responses with Location headers

## Objectives

1. Elicit 302 response
2. Verify redirect to external URL
3. Assess exploitability

## Instructions

### Step 1: Review Request

**Context**: Confirm modifications.

Double-check the 'failed' parameter in Repeater.

### Step 2: Transmit Request

**Context**: Send to server.

Click the "Send" button in Repeater.

**Expected Output**: Response pane shows HTTP/1.1 302 Found with Location: http://google.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Community-Edition]]

## Tags

- [[replay]]
- [[exploit]]
- [[web]]
