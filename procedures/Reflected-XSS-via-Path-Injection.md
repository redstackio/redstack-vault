---
tags:
  - xss
  - reflected-xss
  - path-injection
  - node-js
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
commands:
  - '[[commands/echo-create-script-file]]'
platforms:
  - Web
  - Node.js
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 899e4f6b-0d24-4d61-89fc-839b6f05c089
created_at: '2025-12-14T03:15:10.404Z'
updated_at: '2025-12-14T03:15:10.404Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Reflected-XSS-via-Path-Injection

## Summary

This procedure exploits path handling in tianma-static by using URL encoding to inject HTML script tags into responses, loading and executing malicious scripts from uploaded files, enabling reflected XSS.

## Description

The module uses `decodeURI` on `req.pathname`, which allows `%2f` to decode to `/` without proper escaping, enabling path manipulation. Attackers upload a script file, then craft a URL like `/%2f<script src='/ex'></script>` to inject a `<script>` tag that loads the uploaded script (e.g., `ex` containing `alert(1);`). When processed, the response includes the injection, executing in the browser. Requires file upload capability.

## Requirements

1. File upload access to store the script payload.
2. Direct access to the static file server endpoint on port 8080.
3. Knowledge of uploaded file paths.

## Defense

Defensive measures and detection strategies:

- Use `decodeURIComponent` instead of `decodeURI` and validate paths against allowlists.
- Escape or sanitize path components to prevent HTML injection.
- Implement strict URL parsing and reject suspicious encodings like `%2f`.
- Log and monitor unusual URL patterns with encoded slashes.

## Objectives

1. Inject HTML/script tags via manipulated paths.
2. Load and execute external scripts for XSS.
3. Achieve browser-based code execution on reflection.

## Instructions

### Step 1: Create Script Payload File

**Context**: Prepare a JavaScript file to load via injection.

**Command** ([[commands/echo-create-script-file]]):
```bash
echo "alert(1);" > ex
```

> This creates `ex` with alert code. Expected output: File created. Verify with `cat ex`.

### Step 2: Upload the Script File

**Context**: Store the payload on the server.

**Instructions**: Upload `ex` via the application's endpoint, e.g., `curl -F "file=@ex" http://target:8080/upload`.

> Expected output: Upload confirmed; file at `/ex`.

### Step 3: Craft and Request Manipulated Path

**Context**: Use encoding to inject the script tag.

**Instructions**: Request `http://target:8080/%2f<script src='/ex'></script>`. The path decodes and injects the tag, loading `/ex`.

> Expected output: Response includes injected HTML; alert '1' executes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Initial Access]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques

- None

## Commands Used

- [[commands/echo-create-script-file]]

## Tools Used

- None

## Tags

- [[xss]]
- [[reflected-xss]]
- [[path-injection]]
