---
tags:
  - xss-execution
  - javascript-alert
  - dom-manipulation
  - browser-exploitation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ce389b9e-7072-4b40-8c69-34cebc6bc9b1
created_at: '2025-12-14T03:15:26.767Z'
updated_at: '2025-12-14T03:15:26.767Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-and-Verify-DOM-based-XSS-Execution

## Summary

This procedure triggers the injected JavaScript from the malicious URL hash and verifies execution in the admin browser context, confirming the DOM-based XSS vulnerability in the Huge IT Image Gallery plugin.

## Description

Once the malicious hash is loaded, the plugin's jQuery manipulates the DOM using the unsanitized hash, executing the payload like `<img src=M onerror=alert('0wn3d');>`. The `onerror` fires due to the invalid src, running arbitrary JS. Tested across Chrome, Firefox, and Safari on localhost and production-like environments, this leads to code execution with admin privileges, risking session hijacking, keylogging, or chained exploits for RCE. Verification involves observing the alert and inspecting console for errors.

## Requirements

1. Loaded vulnerable page with malicious hash
2. Active admin session
3. Web browser supporting JavaScript (modern versions of Chrome, Firefox, Safari)

## Defense

Defensive measures and detection strategies:

- Implement output encoding for all dynamic DOM insertions (e.g., via DOMPurify library)
- Enable browser extensions or site-wide CSP to block unsafe inline scripts
- Log and monitor client-side errors or unexpected JS execution in admin panels

## Objectives

1. Execute arbitrary JavaScript in the admin context
2. Confirm payload delivery and firing
3. Assess potential for further exploitation like session theft

## Instructions

### Step 1: Interact with Page to Trigger DOM Update

**Context**: Force jQuery to process the hash by simulating tab selection or page load events.

Click on gallery tabs or refresh the page if necessary.

> The DOM should update, parsing the injected script. No server request needed; all client-side.

### Step 2: Observe Payload Execution

**Context**: Wait for the onerror event on the injected img tag to fire the alert.

Monitor for the alert dialog popping up with the message '0wn3d'.

> If no alert, check browser console (F12 > Console) for JS errors or execution logs. Adjust payload if blocked (e.g., use console.log instead).

### Step 3: Verify in Multiple Browsers

**Context**: Test cross-browser compatibility to ensure reliability.

Repeat in Chrome, Firefox, and Safari, noting any differences.

> Success across browsers confirms the vuln; document variations for reporting.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[javascript-alert]]
- [[dom-manipulation]]
- [[browser-exploitation]]
