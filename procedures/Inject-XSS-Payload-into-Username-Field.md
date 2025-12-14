---
tags:
  - xss
  - payload-injection
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
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 2af3751f-b596-4bb3-8980-a718e3fd1419
created_at: '2025-12-14T03:47:18.449Z'
updated_at: '2025-12-14T03:47:18.449Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Username-Field

## Summary

This procedure injects a stored XSS payload into the username field during account creation on the OWOX Finance platform, exploiting insufficient input sanitization to store malicious JavaScript on the server.

## Description

The attack targets the account addition feature at https://finance.owox.com/customer/accountAdd, where the server stores the username without escaping HTML entities like <, >, and quotes. The payload "><script>alert(document.cookie);</script> closes any surrounding HTML attributes and injects executable script. This is a stored XSS variant, persisting the payload for execution on any user viewing affected pages. Prerequisites include an authenticated session; outcomes include successful account creation with embedded payload, setting up for later execution.

## Requirements

1. Authenticated session from prior login
2. Web browser for form submission
3. Knowledge of XSS payloads (basic JavaScript)

## Defense

Defensive measures and detection strategies:

- Sanitize and escape user inputs on storage and output using libraries like OWASP ESAPI
- Implement Content Security Policy (CSP) to restrict script execution
- Log and monitor form submissions for suspicious patterns, such as script tags in inputs

## Objectives

1. Store unescaped JavaScript in the database via the username field
2. Create a persistent vector for XSS execution on shared pages
3. Avoid detection during submission by mimicking valid input

## Instructions

### Step 1: Navigate to Account Addition Page

**Context**: Access the form for creating a new account to prepare payload injection.

From the dashboard, go to https://finance.owox.com/customer/accountAdd.

> The page loads a form with fields including username; ensure the session is active.

### Step 2: Enter Malicious Payload

**Context**: Inject the XSS payload into the vulnerable username field.

In the username field, enter: "><script>alert(document.cookie);</script>
Fill other required fields (e.g., email, password) with valid data, then submit the form.

> Submission succeeds if the server accepts the input without validation errors. The payload is now stored in the database associated with the new account.

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
