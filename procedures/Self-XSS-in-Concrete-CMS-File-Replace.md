---
tags:
  - xss
  - self-xss
  - concrete-cms
  - file-manager
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
updated_at: '2025-12-14T03:15:27.022Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: cd4e1446-4bd8-40cc-a32e-8e236d426f4d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Self-XSS-in-Concrete-CMS-File-Replace

## Summary

This procedure exploits a self-XSS vulnerability in the File Replace feature of Concrete CMS's File manager when selecting remote files, allowing the execution of arbitrary JavaScript in the authenticated user's browser session upon entering a malicious URL payload.

## Description

The vulnerability arises from insufficient input sanitization in the URL field for remote file replacement. By crafting a URL that includes HTML-breaking characters and an inline JavaScript payload, such as an onerror event in an img tag, the input is reflected directly into the page without proper escaping. This results in immediate JavaScript execution, but only affects the user who enters the payload (self-XSS). In a real attack scenario, this could be used to confirm the vulnerability or, if combined with social engineering, trick other users into executing it. The target environment is Concrete CMS web application, requiring authenticated access to the File manager.

## Requirements

1. Authenticated access to a Concrete CMS instance with File manager permissions
2. A web browser to interact with the dashboard
3. No additional network access or tools beyond standard HTTP

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and HTML/JS escaping on all user inputs, especially URL fields
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for unusual JavaScript alerts or errors in browser consoles during file operations
- Educate users on avoiding suspicious payloads in admin interfaces

## Objectives

1. Execute arbitrary JavaScript in the user's browser to confirm the XSS vulnerability
2. Demonstrate the lack of sanitization in the remote URL input
3. Highlight the self-XSS nature, limiting impact to the individual user

## Instructions

### Step 1: Access File Manager

**Context**: Log in and navigate to the vulnerable feature to prepare for payload injection.

Log in to the Concrete CMS dashboard using valid credentials. Go to the File manager section, select any existing file, and click the Replace button to open the replacement dialog.

### Step 2: Select Remote Files and Inject Payload

**Context**: Choose the remote source and enter the malicious URL to trigger the reflection.

In the replacement dialog, select 'Remote files' as the source. In the URL input box, enter the following payload:

```
http://example.com/"/><img src=x onerror=confirm('XSS')>
```

Submit or trigger the field validation. The payload breaks out of the HTML context and executes the JavaScript, showing a confirmation dialog with 'XSS'.

> The expected output is an immediate browser alert confirming execution. If no alert appears, check the browser console for errors indicating failed reflection.

### Step 3: Verify Execution

**Context**: Confirm the self-XSS has occurred without affecting other users.

Observe the alert dialog in your browser. Attempt the same in an incognito session or different user to verify it does not propagate (self-XSS confirmation).

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
- [[self-xss]]
- [[concrete-cms]]
