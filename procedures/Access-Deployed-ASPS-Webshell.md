---
tags:
  - rce
  - webshell
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/whoami]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:29:44.605Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 8323d493-e9ce-4a71-81ef-39ab7f8fa52f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Access-Deployed-ASPS-Webshell

## Summary

This procedure accesses the extracted ASPX webshell URL to execute arbitrary commands, demonstrating RCE such as running whoami to identify the server context.

## Description

The shell at /CServer/Courseware/<COURSE_ID>/shared/cdlcdlcdl.aspx executes on IIS without sanitization, allowing command injection. Accessing it triggers the embedded code, outputting results directly in the browser, enabling data theft and pivoting on the military server.

## Requirements

1. Extracted course ID
2. Direct access to /CServer/ path
3. Browser or curl for GET request

## Defense

Defensive measures and detection strategies:

- Disable script execution in uploaded directories
- Implement WAF rules for webshell patterns
- Monitor access to courseware/shared paths and command outputs

## Objectives

1. Construct and visit shell URL
2. Execute proof-of-concept command
3. Confirm RCE with output

## Instructions

### Step 1: Build Shell URL

**Context**: Form the path using the course ID.

Replace <COURSE_ID> with extracted GUID: https://█████/CServer/Courseware/F6BAC72B45D64B34ACB662BB001D8523/shared/cdlcdlcdl.aspx

> Expected output: Valid URL.

### Step 2: Access and Execute

**Context**: Trigger the shell to run embedded command.

Visit the URL in browser; it executes [[commands/whoami]].

> Expected output: Page displays server user, e.g., ███ (app pool identity).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used

- [[commands/whoami]]

## Tools Used


## Tags

- rce
- webshell
