---
id: proc-002
tags:
  - xss
  - attribute-injection
  - readonly-test
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-mixmax-search-readonly]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:10.447Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test-Attribute-Injection-with-Readonly

## Summary

This procedure injects 'a readonly' into the Mixmax search parameter to demonstrate HTML attribute interpretation, making the input field readonly and exposing the risk of unquoted insertion leading to potential XSS.

## Description

The vulnerability stems from user input in the 'q' parameter being placed in HTML without quotes, allowing strings like 'readonly' to be treated as attributes. This test alters UI behavior, showing how bypassing current sanitization (filtering =, <, >) could enable XSS. Targets the /dashboard/sequences endpoint post-authentication. Outcome: Non-editable search field confirms injection.

## Requirements

1. Authenticated session to Mixmax dashboard
2. Access to browser for UI interaction or curl for requests
3. HTTPS connectivity to app.mixmax.com

## Defense

Defensive measures and detection strategies:

- Quote all dynamic attributes in HTML generation
- Sanitize inputs to prevent attribute-like strings
- Log and alert on search payloads with spaces or keywords like 'readonly'

## Objectives

1. Prove attribute injection feasibility
2. Illustrate UI manipulation risk
3. Evaluate path to exploitable XSS

## Instructions

### Step 1: Send Injection Payload

**Context**: Submit the payload to trigger attribute parsing.

**Command** ([[commands/curl-mixmax-search-readonly]]):
```bash
curl "https://app.mixmax.com/dashboard/sequences?q=a+readonly" -H "Cookie: your-session-cookie"
```

> Use your session cookie for auth. In browser, enter the URL directly after login.

### Step 2: Verify Injection Effect

**Context**: Check if the search field is now readonly.

**Command** (Browser test):

> Attempt to type in the search box. It should be disabled. Inspect element to see 'readonly' attribute added.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-mixmax-search-readonly]]

## Tools Used


## Tags

- xss
- attribute-injection
