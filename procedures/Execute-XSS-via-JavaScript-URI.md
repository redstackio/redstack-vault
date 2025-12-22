---
tags:
  - xss
  - web-vuln
  - mopub
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/javascript-alert-poc]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2e88fa4e-b8ab-4d1f-a93b-bb5c37b3e65b
created_at: '2025-12-13T23:56:20.515Z'
updated_at: '2025-12-13T23:56:20.515Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute XSS via JavaScript URI

## Summary

This procedure leverages an open redirect to execute arbitrary JavaScript in the context of the MoPub domain by using a javascript: URI in the 'next' parameter, enabling XSS attacks like cookie theft or session hijacking.

## Description

By setting the 'next' parameter to a javascript: scheme, the vulnerability allows execution of client-side code upon redirection after login. This occurs because the parameter lacks filtering for non-http schemes. The attack targets the MoPub login page, requiring credentials, and results in JavaScript execution that could compromise user data.

## Requirements

1. Valid MoPub credentials
2. Browser supporting JavaScript execution
3. Access to the login URL

## Defense

Defensive measures and detection strategies:

- Filter out javascript: and other non-http schemes in redirect parameters
- Use Content Security Policy (CSP) to restrict script execution

## Objectives

1. Execute arbitrary JavaScript for proof of concept
2. Demonstrate potential for session compromise
3. Identify filtering deficiencies

## Instructions

### Step 1: Prepare XSS Payload in URL

**Context**: Modify the next parameter to include a javascript: URI.

Set the URL to:

```bash
https://app.mopub.com/login?next=javascript:alert("proof of concept")
```

> This embeds the XSS payload.

### Step 2: Login and Trigger Execution

**Context**: Authenticate to invoke the redirect and execute the script.

Submit login credentials.

> The JavaScript executes in the browser upon redirect.

### Step 3: Verify Execution

**Context**: Confirm the alert or other script behavior.

Observe the browser for the alert box.

> Success is indicated by the dialog appearing.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/javascript-alert-poc]]

## Tools Used



## Tags

- xss
- javascript
