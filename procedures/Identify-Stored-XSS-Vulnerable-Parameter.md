---
id: proc-identify-stored-xss-param
tags:
  - xss
  - recon
  - web-testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T03:16:08.242Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Identify-Stored-XSS-Vulnerable-Parameter

## Summary

This procedure involves reconnaissance to identify user input parameters in a web application that accept and store data without proper sanitization, enabling stored XSS attacks. In the DoD application case, it targets the q_13787 parameter to confirm persistence of unsanitized inputs.

## Description

Stored XSS occurs when user-supplied data is stored (e.g., in a database) and later displayed to users without output escaping, allowing malicious scripts to execute in viewers' browsers. This procedure focuses on testing input fields for lack of sanitization, using the DoD app at https://███████ as an example where q_13787 handles stored data. Prerequisites include access to the application and basic web inspection tools. Expected outcomes: Confirmation of vulnerability via reflected raw inputs.

## Requirements

1. Access to the target web application (authenticated or public)
2. Web browser with developer tools for inspecting requests and responses
3. Optional: Intercepting proxy like Burp Suite for form manipulation

## Defense

Defensive measures and detection strategies:

- Implement input validation and output encoding (e.g., HTML entity escaping) on all stored data
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript in logs or database queries

## Objectives

1. Discover parameters that store user input without sanitization
2. Verify persistence and lack of escaping in displayed content
3. Assess potential for XSS payload injection

## Instructions

### Step 1: Inspect Application Inputs

**Context**: Examine forms and endpoints to identify candidate parameters for testing.

Navigate to the input form in the DoD application and use browser dev tools (F12) to inspect the q_13787 parameter in the request payload.

**Expected Output**: Parameter identified in POST/GET requests handling user data.

### Step 2: Test with Benign Payload

**Context**: Submit a simple test payload to check for sanitization.

Submit <script>alert('XSS')</script> via q_13787 and view the stored content page. Check source code for raw reflection.

**Expected Output**: Alert dialog if reflected XSS, or raw tags if stored without escaping.

### Step 3: Confirm Storage Mechanism

**Context**: Verify the input is persisted across sessions or users.

Log out/in or access as another user to see if the input remains unsanitized in the display.

**Expected Output**: Persistent raw input visible in HTML source.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web-recon]]
