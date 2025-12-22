---
id: proc-weblate-malicious-next-access
tags:
  - open-redirect
  - weblate
  - authentication
  - bypass
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:10.966Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Weblate Auth Endpoint with Malicious 'next'

## Summary

This procedure constructs and accesses a Weblate third-party authentication endpoint with a crafted 'next' parameter prefixed by triple slashes (///) to bypass the sanitize_redirect function in Python Social Auth, setting up an open redirect.

## Description

In Weblate's authentication flow, the 'next' parameter specifies the post-login redirect URL. Due to a flaw in the underlying Python Social Auth library (issue #62), prefixing with /// tricks the URL parser into treating the external domain as a path, bypassing validation that restricts redirects to the same origin. This affects endpoints like /accounts/login/github/ and enables redirection to arbitrary sites after authentication, ideal for phishing authenticated users.

## Requirements

1. Access to a Weblate instance (e.g., demo.weblate.org) with third-party auth enabled
2. Web browser or command-line tool like curl for URL construction
3. Knowledge of target external domain for redirection (e.g., attacker-controlled phishing site)

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation in authentication flows, rejecting triple slashes or relative paths
- Use Content Security Policy (CSP) with strict redirect rules
- Monitor authentication logs for anomalous 'next' parameters containing ///
- Educate users on phishing risks post-authentication

## Objectives

1. Deliver a malicious authentication URL to the victim
2. Preserve the 'next' parameter through the login prompt
3. Set up for post-auth redirect to external site

## Instructions

### Step 1: Construct Malicious URL

**Context**: Build the URL by appending the 'next' parameter with /// prefix to the auth endpoint.

No specific command; manually craft or use browser URL bar:

Example URL: `https://demo.weblate.org/accounts/login/github/?next=///google.com`

> This loads the GitHub login prompt while embedding the malicious redirect.

### Step 2: Access the Endpoint

**Context**: Visit the URL to initiate the flow, luring the victim if needed.

Use a browser to navigate to the constructed URL, or simulate with curl for testing:

```bash
curl -v "https://demo.weblate.org/accounts/login/github/?next=///google.com"
```

> Expected output includes the authentication HTML response, confirming the parameter is accepted without sanitization error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- open-redirect
- weblate
- url-bypass
