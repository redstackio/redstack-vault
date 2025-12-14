---
tags:
  - xss
  - injection
  - mysql
  - username
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
updated_at: '2025-12-14T03:15:26.433Z'
sub_techniques: []
id: 5b618fdb-6956-4e32-a291-cba8ae02f01c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Injecting XSS into MySQL Username Field

## Summary

This procedure details the injection of a JavaScript payload into the 'mysql Username' field of the Nextcloud setup form, exploiting the lack of input escaping to prepare for reflection.

## Description

The 'mysql Username' parameter in the setup configuration is vulnerable to reflected XSS because user input is directly echoed back in the HTML response without sanitization. By entering a script tag payload, an attacker can cause JavaScript execution upon form submission. This is limited to self-XSS, affecting only the browser of the user performing the setup on an uninstalled instance.

## Requirements

1. Access to the loaded setup form from the previous procedure
2. Knowledge of basic HTML/JavaScript payloads
3. Valid filler values for other form fields (e.g., host: localhost, database: nextcloud_db)

## Defense

Defensive measures and detection strategies:

- Apply input validation and HTML entity encoding on all user inputs in setup forms
- Use Content Security Policy (CSP) to restrict script execution
- Log and alert on setup attempts with suspicious payloads

## Objectives

1. Insert malicious payload without form rejection
2. Complete other required fields to enable submission
3. Set up for payload reflection

## Instructions

### Step 1: Enter Payload in Username Field

**Context**: Locate and populate the vulnerable input field with the XSS payload.

In the 'mysql Username' field, type: `<script>alert(1)</script>`.

> This payload will be reflected unsanitized. The form should accept it as plain text input.

### Step 2: Fill Supporting Fields

**Context**: Provide valid data for other fields to avoid submission errors.

- Database host: `localhost`
- Database password: `testpass`
- Database name: `nextcloud`

> Ensure fields are filled to mimic a legitimate setup attempt.

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
- injection
- mysql
- username
