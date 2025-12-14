---
id: proc-brave-create-html-blob
name: Create-HTML-for-Blob-URL-Replacement
tags:
  - url-spoofing
  - javascript
  - history-api
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
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:39.946Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Create-HTML-for-Blob-URL-Replacement

## Summary

This procedure creates a simple HTML file with embedded JavaScript that uses the history.replaceState() method to replace the current URL in the browser's address bar with a blob URL, exploiting a vulnerability in iOS Brave browser to demonstrate potential UI spoofing.

## Description

In the context of testing browser security, this procedure targets the iOS version of Brave browser (1.3.1), where the History API does not properly enforce same-origin policy restrictions on blob URLs. The resulting HTML, when loaded, immediately alters the displayed URL to a blob format, which could mislead users about the page's origin. This is a low-severity issue as it does not enable direct data theft but violates secure design principles. Prerequisites include a text editor and basic knowledge of HTML/JavaScript.

## Requirements

1. Text editor (e.g., VS Code, Notepad)
2. Knowledge of local file paths for saving the HTML
3. Target: iOS Brave browser version 1.3.1

## Defense

Defensive measures and detection strategies:

- Update Brave browser to the latest version to patch History API restrictions
- Monitor for anomalous JavaScript usage in web apps via content security policies (CSP)
- Educate users on verifying URLs beyond the address bar

## Objectives

1. Generate a proof-of-concept HTML file for URL manipulation
2. Verify the script's syntax and functionality in a safe environment
3. Prepare for hosting to test in the target browser

## Instructions

### Step 1: Write the HTML Script

**Context**: Create the core HTML structure with an inline script that calls history.replaceState on page load to set a blob URL.

No command required; use a text editor to create `blob.html` with the following content:

```html
<!DOCTYPE html>
<html>
<head><title>Blob URL Test</title></head>
<body>
<script>history.replaceState('','','blob:http://192.168.1.111/xxxx');</script>
<p>Page loaded. Check the address bar.</p>
</body>
</html>
```

> This script replaces the URL state with a blob URL upon execution. Save the file in a directory for hosting.

### Step 2: Validate the HTML

**Context**: Ensure the file is syntactically correct and the script will run without errors.

Open the file in a desktop browser (non-target) to test if the script executes without console errors.

> Expected: No JavaScript errors; URL changes to blob format in desktop browser if similar behavior exists, but primary test is in iOS Brave.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[url-spoofing]]
- [[browser-vulnerability]]
