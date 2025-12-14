---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
name: Inject-Stored-XSS-Payload-in-DoD-App
tags:
  - xss
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
updated_at: '2025-12-14T03:15:53.524Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-DoD-App

## Summary

This procedure exploits insufficient input sanitization in the U.S. DoD web application at https://███ to inject a malicious JavaScript payload into a stored field, such as the 'Year Group (Military Only)' parameter, allowing the script to persist and execute when viewed by victims.

## Description

The vulnerability stems from lack of proper output encoding or input validation, enabling attackers to store arbitrary JavaScript in application data. In the DoD app, this affects features requiring user input that is later displayed to others. Prerequisites include authenticated access to the application. Expected outcomes include successful payload storage, confirmed by viewing the infected content, leading to browser script execution in victim sessions for theft or manipulation.

## Requirements

1. Authenticated access to https://███ with military user privileges
2. Web browser with developer console for testing
3. Optional proxy (e.g., Burp Suite) for request interception

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to block inline scripts
- Use input validation and output encoding (e.g., HTML entity encoding) on all user inputs
- Monitor for anomalous JavaScript in logs or database fields

## Objectives

1. Inject and store malicious payload without immediate rejection
2. Verify persistence in application storage
3. Set up for victim-side execution

## Instructions

### Step 1: Access Vulnerable Feature

**Context**: Log in to the DoD application and navigate to the feature with the vulnerable input, such as the 'Year Group (Military Only)' form.

Inspect the form using browser developer tools to identify the input field (e.g., via element selector).

### Step 2: Craft and Inject Payload

**Context**: Enter a test payload to confirm the vulnerability, then escalate to malicious code.

Use the browser form to input: `<script>alert('XSS Test')</script>` and submit.

> If using a proxy, intercept the POST request and modify the parameter (e.g., year_group=<script>alert('XSS')</script>).

**Expected Output**: Form submits successfully; no sanitization errors.

### Step 3: Verify Storage

**Context**: Access the page or view where the input is displayed to confirm storage.

Refresh or navigate to the dashboard/report displaying the year group data.

View page source to check for unencoded script tags.

**Expected Output**: Payload appears in HTML as-is, triggering alert on load.

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
- injection
