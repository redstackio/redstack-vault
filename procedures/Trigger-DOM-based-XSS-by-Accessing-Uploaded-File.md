---
id: proc-uuid-2
name: Trigger-DOM-based-XSS-by-Accessing-Uploaded-File
tags:
  - xss
  - dom-xss
  - stored-xss
type: procedure
tools: []
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
updated_at: '2025-12-13T23:52:20.843Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-DOM-based-XSS-by-Accessing-Uploaded-File

## Summary

This procedure triggers the execution of a stored XSS payload by accessing the path of an uploaded file with a malicious filename, causing the server to embed the unescaped payload in the HTML response and execute JavaScript in the browser.

## Description

Following the upload of a file with an XSS payload in its filename on partners.line.me, accessing the file's URL causes the server to generate an HTML page that includes the filename without proper escaping. This results in DOM-based XSS, where the browser parses and executes the injected script. The impact is limited to the duration the file is stored on the server, and certain restrictions prevent cookie theft, but arbitrary JS can still run in the context of the page.

## Requirements

1. Web browser for navigation and execution
2. Knowledge of the uploaded file's path (e.g., from upload response)
3. The file must still be stored on the server (temporary retention)

## Defense

Defensive measures and detection strategies:

- Escape all user-controlled data (including filenames) when embedding in HTML using HTML entity encoding
- Implement output validation to prevent script injection in file listings or paths
- Use strict CSP headers to mitigate XSS even if injection occurs
- Log and alert on access to uploaded files with suspicious paths

## Objectives

1. Cause the server to serve the unescaped filename in HTML
2. Execute the stored XSS payload in the browser DOM
3. Demonstrate JS execution without requiring further interaction

## Instructions

### Step 1: Locate the File Path

**Context**: Identify the URL where the uploaded file is accessible to trigger the embedding.

After upload, note the file's storage path, typically something like https://partners.line.me/uploads/[filename].

### Step 2: Access the Path

**Context**: Navigate to the file URL to force the server to embed the filename in the response.

Enter the full URL in the browser address bar and load the page, e.g., https://partners.line.me/uploads/test'><script>alert('XSS')</script>.txt.

> The server embeds the filename in HTML (e.g., <a href="...">test'><script>alert('XSS')</script>.txt</a>), causing the script to execute as the DOM parses it.

**Expected Output**: JavaScript alert or console log executes, confirming XSS. Inspect the page source to see the unescaped payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[dom-xss]]
- [[stored-xss]]
