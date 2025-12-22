---
tags:
  - xss-execution
  - request-replay
  - vulnerability-trigger
type: procedure
tools:
  - '[[tools/LiveHTTPHeaders]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:41.575Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 23d64df1-4217-486d-99c2-4e69ea30011c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Replay Modified Request to Trigger XSS

## Summary

This procedure sends the tampered file upload request to the server, eliciting an error response that reflects the unescaped XSS payload, resulting in JavaScript execution in the victim's browser.

## Description

In the Udemy file upload scenario, replaying the modified request with the malicious filename causes the server to return a JSON error message where the filename is improperly escaped, allowing HTML/JS injection. This can lead to self-XSS or broader impact if the error is displayed in shared views like profiles. Prerequisites: Modified request ready. Outcome: Alert popup confirming exploitation.

## Requirements

1. Modified request in LiveHTTPHeaders
2. Active session with the target endpoint
3. Browser configured to execute JS (default)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize filenames server-side before inclusion in responses
- Use Content-Security-Policy to mitigate XSS
- Monitor for error responses containing script-like content

## Objectives

1. Trigger the vulnerable error response
2. Confirm payload execution via alert
3. Assess potential for wider impact (e.g., profile views)

## Instructions

### Step 1: Forward the Request

**Context**: Resume the intercepted request to hit the endpoint.

**Instructions**: In LiveHTTPHeaders, click 'Resume' or 'Forward' on the modified request to send it to the Udemy server.

> The server processes the invalid filename, generates an error, and responds with JSON including the reflected payload.

### Step 2: Observe Response and Execution

**Context**: Capture and inspect the response for reflection and JS trigger.

**Instructions**: View the response in the tool; look for the JSON body echoing the filename. The browser should pop an alert(1) if successful.

> Expected: Unescaped payload in JSON leads to <img> tag execution, firing onerror.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/LiveHTTPHeaders]]

## Tags

- [[xss-execution]]
- [[request-replay]]
