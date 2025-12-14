---
tags:
  - xss
  - csp-bypass
  - iframe
  - rocket-chat
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 50df84a5-2471-4da5-b715-866b090c3167
created_at: '2025-12-14T05:32:10.405Z'
updated_at: '2025-12-14T05:32:10.405Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-Uploaded-JS-via-XSS-Iframe-in-Rocket-Chat

## Summary

This procedure exploits an XSS vulnerability in Rocket.Chat message content to inject an iframe with a srcdoc attribute, sourcing and executing the previously uploaded JavaScript file, thereby bypassing CSP's unsafe-inline restriction and script tag filters.

## Description

Rocket.Chat filters direct <script> tags in user messages but fails to sanitize iframes and srcdoc attributes adequately. By injecting an iframe whose srcdoc contains a script sourcing the uploaded JS (e.g., from /file-upload/<ID>/payload.js), the payload executes in the page's context. This amplifies an existing HTML injection (XSS) to full JavaScript execution. Prerequisites: An existing XSS point and the upload ID from the prior procedure. Outcomes include arbitrary code execution, such as stealing cookies or manipulating the DOM.

## Requirements

1. Existing XSS vulnerability allowing HTML injection in messages
2. Upload ID from a previously uploaded JS file
3. Authenticated session to post messages

## Defense

Defensive measures and detection strategies:

- Sanitize or strip iframe and srcdoc attributes in user-generated content
- Strengthen CSP to block data: or srcdoc-based executions if possible
- Implement client-side monitoring for unexpected script loads from uploads and log anomalous iframe injections

## Objectives

1. Bypass CSP and filters to execute external JS
2. Achieve arbitrary code execution in the victim's browser
3. Enable impacts like session hijacking or data exfiltration

## Instructions

### Step 1: Craft the Iframe Payload

**Context**: Build the injection payload using the upload ID to reference the JS file.

Construct the payload as: `<iframe srcdoc="<script src='/file-upload/<UPLOAD ID>/payload.js?download'></script>"></iframe>`. Replace <UPLOAD ID> with the actual value (e.g., abc123).

**Expected Output**: Valid HTML snippet ready for injection.

### Step 2: Inject via XSS and Execute

**Context**: Post the payload in a message where XSS is possible, triggering execution.

Use the XSS vector (e.g., a vulnerable input field or message composer) to submit the iframe payload. View the rendered message in the chat to activate the srcdoc, which loads and runs the script.

**Expected Output**: JavaScript executes immediately, e.g., alert pops up or network request to attacker server with stolen data.

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
- [[csp-bypass]]
- [[iframe]]
- [[rocket-chat]]
