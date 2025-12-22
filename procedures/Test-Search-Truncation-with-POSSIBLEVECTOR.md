---
id: proc-001
tags:
  - xss
  - html-injection
  - truncation-test
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-mixmax-search-possiblevector]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:10.449Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test-Search-Truncation-with-POSSIBLEVECTOR

## Summary

This procedure tests the Mixmax Sequences dashboard search for truncation caused by unquoted user input insertion into HTML, where a payload like 'a POSSIBLEVECTOR' results in only 'a' being displayed as the rest is parsed as raw HTML.

## Description

In the Mixmax dashboard, the 'q' search parameter is reflected into HTML without proper quoting, allowing the browser to misparse input. This test uses 'a POSSIBLEVECTOR' to demonstrate truncation, indicating a risk for attribute confusion or future XSS if sanitization fails. The target is the /dashboard/sequences endpoint, requiring authenticated access. Expected outcome is visual truncation in the UI, confirming improper escaping.

## Requirements

1. Valid Mixmax user credentials for dashboard authentication
2. Web browser or curl for HTTP requests
3. Network access to https://app.mixmax.com

## Defense

Defensive measures and detection strategies:

- Implement proper HTML escaping and quoting for all user inputs reflected in attributes
- Use Content Security Policy (CSP) to mitigate XSS
- Monitor for anomalous search queries in application logs

## Objectives

1. Confirm truncation behavior indicating parsing flaw
2. Document evidence for potential vulnerability reporting
3. Assess risk of escalation to full XSS

## Instructions

### Step 1: Authenticate and Access Dashboard

**Context**: Log in to Mixmax and navigate to the Sequences dashboard to prepare for testing.

**Command** ([[commands/curl-mixmax-search-possiblevector]]):
```bash
curl "https://app.mixmax.com/dashboard/sequences?q=a+POSSIBLEVECTOR" -H "Cookie: your-session-cookie"
```

> This sends the request with the payload. Replace session cookie with your authenticated value. In a browser, simply visit the URL after login.

### Step 2: Inspect Output

**Context**: Examine the HTML response or UI to verify truncation.

**Command** (Browser inspection):

> Open developer tools (F12) and check the search input element. The value should show only 'a', with the rest absent due to parsing.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-mixmax-search-possiblevector]]

## Tools Used


## Tags

- xss
- html-injection
