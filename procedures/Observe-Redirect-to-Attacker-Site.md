---
id: proc-weblate-observe-redirect
tags:
  - phishing
  - redirect
  - exploitation
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
  - '[[Phishing]]'
updated_at: '2025-12-14T17:31:10.962Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Observe Redirect to Attacker Site

## Summary

This procedure verifies the open redirect by observing the post-authentication navigation to the external attacker-controlled site, confirming the bypass and phishing potential.

## Description

Upon successful auth, Weblate redirects to the 'next' URL. The /// prefix causes the sanitizer to misparse, allowing external domains. This can trick users into interacting with a phishing page that appears legitimate, capturing sensitive data or credentials.

## Requirements

1. Successful completion of prior authentication steps
2. Network monitoring capability (e.g., browser dev tools or curl -v)
3. Attacker site prepared (e.g., phishing page hosted on google.com equivalent)

## Defense

Defensive measures and detection strategies:

- Enforce same-origin policy for all post-auth redirects
- Implement URL allowlisting in auth libraries
- Monitor user-agent strings and referer headers for anomalous redirects
- Deploy web application firewall (WAF) rules to block suspicious 'next' patterns

## Objectives

1. Confirm redirection to arbitrary external site
2. Enable phishing by mimicking legitimate flow
3. Impact all third-party providers uniformly

## Instructions

### Step 1: Monitor Post-Auth Redirect

**Context**: After login, watch for the HTTP 302 redirect in browser or tools.

Use curl with verbose for testing:

```bash
curl -v -L "https://demo.weblate.org/accounts/login/github/?next=///google.com" # Follows redirects
```

> Expected output: Location header points to http://google.com/, confirming bypass.

### Step 2: Verify Phishing Setup

**Context**: Ensure the target site loads and captures user interaction.

Browser action: Interact with the redirected page to simulate phishing success.

> Expected output: External site loads seamlessly after auth.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- phishing
- open-redirect
- exploitation
