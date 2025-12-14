---
id: proc-001
tags:
  - xss
  - stored-xss
  - injection
  - veris
type: procedure
tools:
  - '[[tools/Mozilla-Firefox]]'
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.743Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-Veris-Edit-Group-Details

## Summary

This procedure exploits the lack of input sanitization in the Veris application's Edit Group Details form by injecting malicious JavaScript payloads, which are stored in the backend and later reflected unsanitized, enabling stored XSS attacks.

## Description

In the Veris application, the Edit Group Details form allows users to modify group information through input fields that do not sanitize or escape user-supplied data. Attackers can insert JavaScript payloads, such as event-handler based scripts, which are saved directly to the database. When this data is retrieved and displayed in other parts of the application, like the Rule Book, it executes in the context of the viewing user's browser. This leads to arbitrary code execution, potentially allowing session token theft or other client-side manipulations. The procedure assumes access to the form, either authenticated or public, and targets web browsers as the execution environment.

## Requirements

1. Access to the Veris application with permissions to edit group details
2. A modern web browser like Firefox or Chrome for testing
3. Knowledge of basic JavaScript payloads for XSS

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and sanitization using libraries like DOMPurify or OWASP ESAPI
- Escape output in all rendered contexts, especially in the Rule Book display
- Deploy Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript alerts or network requests from the application

## Objectives

1. Persist malicious JavaScript in the application's storage
2. Set up conditions for execution in victim browsers
3. Validate injection success without immediate execution

## Instructions

### Step 1: Access the Edit Group Details Form

**Context**: Locate and load the vulnerable form to begin injection.

No specific command; manually navigate in the browser to the group editing interface.

> Expected: Form fields load without restrictions.

### Step 2: Enter Malicious Payloads

**Context**: Inject payloads into multiple input fields to maximize storage points.

Use payloads like:

```html
<img src=x onerror=alert(document.domain)>
```

or

```html
<img src=x onerror=alert(document.cookie)>
```

> These onload error handlers execute when the image fails to load, common for XSS testing. Expected: Payloads are typed or pasted without form rejection.

### Step 3: Submit the Form

**Context**: Save the data to trigger backend storage.

Click the submit/save button.

> Expected: Success message; payloads are now stored unsanitized.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mozilla-Firefox]]
- [[tools/Google-Chrome]]

## Tags

- xss
- stored-xss
- veris
