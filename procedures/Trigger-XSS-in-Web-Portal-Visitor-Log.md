---
tags:
  - xss
  - stored-xss
  - web
  - execution
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
id: a891befb-f81b-41b7-8571-2e02815cf17a
created_at: '2025-12-14T17:24:39.218Z'
updated_at: '2025-12-14T17:24:39.218Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Web-Portal-Visitor-Log

## Summary

This procedure triggers the execution of stored XSS payloads by accessing the vulnerable visitor log page in the Veris web portal, where unsanitized inputs from the app are reflected and run as JavaScript in the authenticated user's browser.

## Description

After payloads are stored via the Android app, logging into the web portal at https://sandbox.veris.in/ and navigating to /portal/visitor-log/ causes the malicious JavaScript to render without escaping. This executes in the victim's session context, enabling attacks like cookie theft (e.g., via `document.cookie`). The procedure assumes prior injection and requires portal credentials, targeting any user with log access.

## Requirements

1. Valid login credentials for the Veris web portal
2. Browser with JavaScript enabled
3. Prior successful payload injection via the app

## Defense

Defensive measures and detection strategies:

- Enforce output encoding in the visitor log rendering (e.g., escape HTML/JS)
- Deploy Web Application Firewall (WAF) rules to block XSS patterns in logs
- Log and alert on JavaScript errors or unexpected DOM changes in the portal

## Objectives

1. Load the visitor log to render stored payloads
2. Execute JavaScript in the portal's browser context
3. Validate impact through alert popups or console logs

## Instructions

### Step 1: Access the Web Portal

**Context**: Authenticate to gain access to administrative features like the visitor log.

Open a web browser and navigate to https://sandbox.veris.in/. Enter valid credentials (username and password) and log in.

### Step 2: Navigate to Visitor Log

**Context**: Reach the page where stored check-in data is displayed unsanitized.

From the portal dashboard, select the 'Visitor Log' option or directly visit https://sandbox.veris.in/portal/visitor-log/.

### Step 3: Load and Observe Execution

**Context**: Trigger the rendering of injected entries to execute the XSS.

Scroll or refresh the page to ensure the recent check-in entries (with payloads) are loaded. Observe JavaScript alerts (e.g., alert(3) and alert(4)) confirming execution.

### Step 4: Validate Impact

**Context**: Confirm the vulnerability's potential for further exploitation.

Inspect the browser console for errors or use developer tools to check if payloads like `alert(document.cookie)` could steal session data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- stored-xss
- web
