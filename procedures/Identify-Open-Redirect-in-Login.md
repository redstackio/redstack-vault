---
id: proc-uuid-1
tags:
  - open-redirect
  - web-testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.513Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Open-Redirect-in-Login

## Summary

This procedure tests for open redirect vulnerabilities in web application login flows by manipulating redirect parameters to external domains, confirming lack of domain validation. It is primarily used during security assessments to identify phishing enablers in authentication endpoints.

## Description

In the context of the Moneybird login procedure, the vulnerability arises from an unvalidated 'redirect_to' parameter that allows arbitrary URLs. Attackers can test this by appending external domains to the login URL and observing if the application redirects post-authentication without checking the target domain. This exposes users to phishing risks, as legitimate login flows can be hijacked to malicious sites. Prerequisites include public access to the login endpoint and basic web testing tools.

## Requirements

1. Public access to the target login URL (e.g., https://moneybird.com/login)
2. Ability to make HTTP requests (browser or curl)
3. Knowledge of URL parameter manipulation

## Defense

Defensive measures and detection strategies:

- Implement strict domain whitelisting for redirect parameters (e.g., only allow redirects to *.moneybird.com)
- Log and monitor unusual redirect patterns or external domain attempts
- Use Content Security Policy (CSP) to restrict navigation to untrusted origins

## Objectives

1. Confirm the presence of an open redirect vulnerability
2. Document the exact parameter and endpoint affected
3. Assess potential for phishing exploitation

## Instructions

### Step 1: Access Login Endpoint

**Context**: Locate the login page and inspect for redirect parameters, typically in GET requests.

**Command** ([[commands/curl-test-redirect]]):
```bash
curl -L "https://moneybird.com/login?redirect_to=http://example.com" -v
```

> This command follows redirects (-L) and provides verbose output (-v) to show the 302 response and Location header pointing to the external site, indicating no validation.

### Step 2: Validate Redirect Behavior

**Context**: Attempt login simulation if possible, or observe post-login redirect to confirm persistence.

**Command** ([[commands/curl-test-redirect]]):
```bash
curl -L -c cookies.txt "https://moneybird.com/login?redirect_to=http://evil.com" --data "username=test&password=test"
```

> Simulates a login POST with redirect parameter; expected output includes redirect to evil.com if vulnerable, stored in cookies.txt for session tracking.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-redirect]]

## Tools Used


## Tags

- [[open-redirect]]
- [[Phishing]]
- [[web]]
