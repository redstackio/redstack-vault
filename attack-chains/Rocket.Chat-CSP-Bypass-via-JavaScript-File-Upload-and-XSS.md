---
tags:
  - csp-bypass
  - xss
  - file-upload
  - rocket-chat
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Upload-Malicious-JavaScript-File-in-Rocket-Chat]]'
  - '[[procedures/Execute-Uploaded-JS-via-XSS-Iframe-in-Rocket-Chat]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
description: >-
  A multi-stage attack exploiting CSP restrictions in Rocket.Chat by uploading
  executable JavaScript files and injecting them via an XSS vulnerability using
  iframes with srcdoc attributes.
skill_level: intermediate
impact_level: high
id: 69d9d1eb-7529-4638-8f27-5543ee413edb
created_at: '2025-12-14T05:32:10.439Z'
updated_at: '2025-12-14T05:32:10.439Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Rocket.Chat CSP Bypass via JavaScript File Upload and XSS

## Overview

This attack chain demonstrates a Content-Security Policy (CSP) bypass in Rocket.Chat, where an attacker uploads a JavaScript file through the file upload feature, which is served with an executable content-type like application/javascript. The uploaded file is then sourced into an iframe with a srcdoc attribute, injected via an existing XSS vulnerability in message content. This circumvents CSP's unsafe-inline restriction and filters that remove direct script tags, enabling arbitrary JavaScript execution. The attack can lead to session hijacking, data theft, or further system compromise in the victim's browser context.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Upload JS Payload] --> B[Inject XSS Iframe]
    B --> C[Arbitrary JS Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser with developer tools for testing uploads and injections
- Access to a vulnerable Rocket.Chat instance (authenticated user with file upload permissions)

### Target Environment

- Rocket.Chat web application (version vulnerable to this issue, e.g., pre-patch for report #1380157)
- Required services/ports: HTTP/HTTPS on standard web ports (80/443)
- Network access requirements: Direct access to the Rocket.Chat instance as a registered user

### Initial Access Requirements

- Valid user account in Rocket.Chat with permissions to upload files and post messages
- Existing XSS vulnerability in message injection (HTML injection point)
- No special credentials beyond standard user access

## Detailed Attack Procedures

### Step 1: Upload Malicious JavaScript File
procedure: [[procedures/Upload-Malicious-JavaScript-File-in-Rocket-Chat]]

**Objective**: Upload a JavaScript payload file that will be served with an executable content-type, bypassing CSP for later execution.

**Instructions**: Use the file upload feature in Rocket.Chat to upload a file named payload.js containing malicious JavaScript code, such as `alert('XSS');` or more advanced payloads for session theft. Ensure the file is uploaded with content-type application/javascript or text/javascript. Note the upload ID returned by the server, typically in the form of a unique identifier for the uploaded file path.

**Expected Output**: Successful upload confirmation, with the file accessible at a URL like `/file-upload/<UPLOAD ID>/payload.js?download`.

**Success Indicators**:
- File upload succeeds without errors
- File is downloadable and verifiable via browser (check content-type in network tab)

### Step 2: Execute Uploaded JS via XSS Iframe
procedure: [[procedures/Execute-Uploaded-JS-via-XSS-Iframe-in-Rocket-Chat]]

**Objective**: Inject an iframe using the srcdoc attribute to load and execute the uploaded JavaScript, bypassing CSP and script tag filters.

**Instructions**: Exploit an arbitrary XSS vulnerability in message content to inject the following payload: `<iframe srcdoc="<script src='/file-upload/<UPLOAD ID>/payload.js?download'></script>"></iframe>`, replacing `<UPLOAD ID>` with the actual ID from Step 1. Post this in a chat message or wherever HTML injection is possible. The iframe's srcdoc will render the script tag, sourcing the external JS file and executing it in the page context.

**Expected Output**: The JavaScript from payload.js executes, e.g., an alert box appears or session data is exfiltrated.

**Success Indicators**:
- Iframe injects without sanitization
- JavaScript executes (visible via alert, console logs, or network requests for exfiltration)
- No CSP violation errors in browser console

## Attack Chain Summary

### Key Achievements

1. Successful upload of executable JS despite CSP restrictions on inline scripts
2. Bypass of message filtering for script tags using iframe srcdoc
3. Arbitrary JavaScript execution leading to potential session hijacking or data theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
