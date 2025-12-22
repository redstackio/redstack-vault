---
id: proc-004
tags:
  - xss-trigger
  - rce-execution
  - payload-access
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:32.394Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Command-Line Interface]]'
---
# Access-Uploaded-File-to-Trigger-Payload

## Summary

Retrieve and view the uploaded HTML file to execute stored XSS JavaScript and invoke the PHP shell for remote command execution on the server.

## Description

Using the Document ID, access the file via the request page or direct URL like /{DocumentID}/$FILE/{filename}. Rendering triggers JS in the browser context, enabling session theft. Appending ?cmd= to the URL executes PHP, allowing arbitrary commands. High impact due to authenticated context and server control.

## Requirements

1. Valid Document Number from prior step
2. Browser for rendering and developer console for verification
3. Knowledge of payload parameters (e.g., cmd for shell)

## Defense

Defensive measures and detection strategies:

- Sanitize and escape uploaded content; serve files with noexec/nojs headers
- Monitor for anomalous file accesses and command executions in logs
- Use Content Security Policy (CSP) to block inline scripts

## Objectives

1. Execute JavaScript for data exfiltration (e.g., cookies)
2. Run server commands via PHP interpreter
3. Achieve session hijacking or system compromise

## Instructions

### Step 1: Locate Attachment on Request Page

**Context**: Find the file link in the document view.

Scroll to the bottom of the modification page.

> Attachments section displays; click the HTML file link.

### Step 2: Trigger XSS Execution

**Context**: Render the file to run JavaScript.

Browser opens or embeds the file; observe alert or console output.

> XSS fires, potentially displaying or sending cookies.

### Step 3: Invoke PHP Shell for RCE

**Context**: Directly access with parameters.

Construct URL: `https://target.com/{DocumentID}/$FILE/unsure1.html?cmd=ls` and load.

> Output shows directory listing; replace cmd for other commands like `whoami` or `cat /etc/passwd`.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[rce-execution]]
