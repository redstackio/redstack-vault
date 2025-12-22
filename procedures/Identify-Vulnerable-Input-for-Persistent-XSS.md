---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - xss
  - persistent-xss
  - web
  - input-validation
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
updated_at: '2025-12-14T03:15:26.759Z'
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
# Identify-Vulnerable-Input-for-Persistent-XSS

## Summary

This procedure involves manual testing of user input fields on a web application's booking or reservation form to identify fields lacking proper sanitization, allowing for persistent cross-site scripting (XSS) where injected JavaScript is stored in the database and executes for subsequent viewers.

## Description

In the context of the Eternal application, this targets the booking page where user inputs like names or notes are stored without escaping. The attack scenario assumes an external attacker with access to the public form. Expected outcomes include confirmation of vulnerability through payload reflection in stored data, leading to client-side script execution. Prerequisites include a web browser and basic knowledge of JavaScript payloads.

## Requirements

1. Access to the target web application (e.g., Eternal booking page).
2. Web browser with developer tools for inspecting page source.
3. No special credentials needed for public forms.

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and output encoding (e.g., using HTML entity encoding).
- Use Content Security Policy (CSP) to restrict script execution.
- Monitor for anomalous JavaScript in database logs or user inputs.

## Objectives

1. Locate unsanitized input fields susceptible to XSS.
2. Verify persistence by checking if payloads execute on page reload or for other users.
3. Assess potential for broader attacks like session hijacking.

## Instructions

### Step 1: Navigate and Inspect Form

**Context**: Access the target booking or reservation page and examine input fields for potential injection points.

Open the Eternal application's booking form in a web browser. Use developer tools (F12) to inspect elements like text inputs for names, descriptions, or notes. Submit neutral test data first to understand how inputs are stored and displayed.

### Step 2: Test for XSS Vulnerability

**Context**: Inject a basic payload to check for sanitization failures and persistence.

Enter a test payload such as `<script>alert('XSS Test')</script>` into a suspected field (e.g., reservation notes). Submit the form and then navigate to view the booking details. Inspect the page source or observe if the alert triggers. If the script executes without sanitization, the field is vulnerable to persistent XSS.

> If the payload appears unescaped in the HTML output and executes, vulnerability is confirmed. For persistence, create a new session or use incognito mode to view the details.

### Step 3: Validate Persistence

**Context**: Confirm the injected script is stored in the database and affects multiple users.

After submission, access the booking details as if viewing another user's reservation. Check if the payload executes again, indicating database storage without sanitization.

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
- [[persistent-xss]]
- [[web]]
- [[input-validation]]
