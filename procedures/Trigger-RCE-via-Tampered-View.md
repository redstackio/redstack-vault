---
tags:
  - rce
  - erb
  - view-injection
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-trigger-rce]]'
  - '[[commands/system-date-execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[PowerShell]]'
updated_at: '2025-12-14T17:26:22.380Z'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques: []
id: 7a5b1162-a735-4385-8718-5097fea0aa47
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[PowerShell]]'
---
# Trigger-RCE-via-Tampered-View

## Summary

This procedure triggers remote code execution by accessing an endpoint that renders the tampered ERB view, executing the injected system command.

## Description

After writing the malicious ERB to a view file, requesting /users/show causes Rails to render it, evaluating the ERB code and running the embedded system('date') command on the server.

## Requirements

1. Malicious ERB successfully written to view
2. Accessible endpoint that renders the tampered view
3. HTTP client like curl or browser
4. Server-side ERB rendering enabled

## Defense

Defensive measures and detection strategies:

- Validate and escape user-controlled content in views
- Use safe rendering modes or disable ERB in certain contexts
- Monitor process execution logs for unexpected commands
- Implement runtime code scanning in templates

## Objectives

1. Execute arbitrary commands on the server
2. Confirm RCE from file write chain
3. Demonstrate full compromise impact

## Instructions

### Step 1: Access Tampered Endpoint

**Context**: Request the view to trigger ERB evaluation.

**Command** ([[commands/curl-trigger-rce]]):
```bash
curl http://0.0.0.0:3000/users/show
```

> Response includes output from system('date'), e.g., current date/time.

### Step 2: Verify Execution

**Context**: The embedded command executes during rendering.

**Command** ([[commands/system-date-execution]]):
```bash
system('date')
```

> This is the payload; output appears in the HTTP response.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[PowerShell]] Command and Scripting Interpreter

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-rce]]
- [[commands/system-date-execution]]

## Tools Used

- [[tools/curl]]

## Tags

- rce
- erb
- view-injection
