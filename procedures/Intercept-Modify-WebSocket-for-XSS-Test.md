---
id: proc-uuid-002
tags:
  - xss
  - websocket-interception
type: procedure
tools:
  - '[[tools/WebSocket-Interceptor]]'
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
updated_at: '2025-12-14T03:47:23.610Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Intercept-Modify-WebSocket-for-XSS-Test

## Summary

Intercept the WebSocket response from the set_watch event evaluation and append an XSS payload to test for unsanitized HTML rendering in the debugger's date/time display area.

## Description

After observing the WebSocket request, this procedure captures the incoming response containing the evaluated datetime string. By modifying it to include raw HTML/JS, the lack of sanitization is confirmed when the frontend renders it directly, executing the payload. This targets the hardcoded expression's response handling in Quantopian's JavaScript frontend.

## Requirements

1. Active WebSocket session from previous observation
2. Interception tool configured for real-time modification
3. Test payload ready (e.g., simple alert)

## Defense

Defensive measures and detection strategies:

- Sanitize all WebSocket response payloads before UI rendering
- Validate expression results server-side for expected formats
- Log and alert on modified WebSocket frames

## Objectives

1. Verify XSS feasibility via response tampering
2. Confirm execution in the UI without user interaction
3. Identify response structure for advanced payloads

## Instructions

### Step 1: Set Up Interception

**Context**: Position the tool to capture incoming responses post-evaluation.

Configure [[tools/WebSocket-Interceptor]] to break on responses matching the set_watch event.

**Expected Output**: Paused on response with datetime string.

### Step 2: Append XSS Payload and Forward

**Context**: Inject the payload into the response body.

Modify the JSON response's result field by appending '<img src=x onerror=alert(1)>', then resume traffic.

**Expected Output**: Alert executes in the browser's date area.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/WebSocket-Interceptor]]

## Tags

- xss
- websocket-interception
