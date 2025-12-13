---
tags:
  - verification
  - node-js
type: procedure
tools:
  - '[[tools/Node-js]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Node.js
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 540efa0e-7f04-4975-b58c-d4f681fcbab2
created_at: '2025-12-13T09:01:16.945Z'
updated_at: '2025-12-13T09:01:16.945Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify Template Functionality

## Summary

This procedure verifies the functionality of the lodash template in the test application by sending a normal input and checking the rendered output.

## Description

Access the running application with a benign query parameter to ensure the template processes input correctly without errors, setting the stage for exploitation.

## Requirements

1. Running test application on port 8000
2. Web browser or curl for HTTP requests

## Defense

Defensive measures and detection strategies:

- Monitor for unusual query parameters
- Implement input validation

## Objectives

1. Confirm application responsiveness
2. Validate template rendering

## Instructions

### Step 1: Send Normal Request

**Context**: Access the URL with a test name.

```bash
curl "http://127.0.0.1:8000/?name=Test"
```

> Expect the response 'Hello Test.' to confirm functionality.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used

## Tools Used

- [[tools/Node-js]]

## Tags

- [[verification]]
- [[tools/Node-js]]
