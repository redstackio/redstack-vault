---
id: proc-uuid-123
tags:
  - open-redirect
  - phishing
  - url-bypass
  - filter-bypass
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
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:23.487Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Phishing]]'
---
# Bypass-Open-Redirect-Filter-with-Malformed-URLs

## Summary

This procedure exploits an open redirect vulnerability in a web application's logout endpoint by crafting malformed returnTo parameters that evade URL validation filters, allowing redirection to arbitrary external sites for phishing attacks.

## Description

In the Zaption application, the logout endpoint at /logout accepts a returnTo parameter intended for post-logout redirects. Due to inadequate validation, the server does not properly normalize or filter malformed URLs, such as those with multiple consecutive slashes (e.g., ///evil.com) or misplaced protocol separators (e.g., http:///evil.com). When processed, the server issues a 302 redirect to the manipulated URL, which browsers resolve to the attacker's domain. This enables phishing by tricking users into visiting malicious sites, potentially leading to credential theft or malware delivery. The vulnerability was tested on Firefox 39.0 and latest Chrome, confirming cross-browser impact in a web environment.

## Requirements

1. Access to a web browser (Firefox or Chrome) or curl for testing.
2. Publicly accessible target endpoint (e.g., https://www.zaption.com/logout).
3. No authentication required for the logout endpoint.
4. Knowledge of target domain and a controlled malicious domain for testing (e.g., evil.com).

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation and normalization on redirect parameters, using whitelists for allowed domains.
- Canonicalize URLs by removing extra slashes and validating protocol positions before processing redirects.
- Monitor server logs for 302 responses to unusual or external domains in redirect parameters.
- Use Content Security Policy (CSP) headers to restrict navigations and detect anomalous redirects client-side.

## Objectives

1. Bypass redirect filters to force server-issued redirects to arbitrary external domains.
2. Demonstrate phishing potential by simulating user redirection to a malicious site.
3. Validate the exploit across multiple browsers without triggering security warnings.

## Instructions

### Step 1: Test Multiple Slashes Bypass

**Context**: Craft a returnTo parameter with multiple slashes to confuse the server's URL parsing, preventing filter application.

**Command** ([[commands/curl-test-redirect]]):
```bash
curl -i -L "https://www.zaption.com/logout?returnTo=///evil.com/"
```

> This command sends a GET request to the logout endpoint with the malformed parameter. The server responds with a 302 redirect to ///evil.com/, which curl follows (-L flag), resolving to http://evil.com/. Expected output includes the 302 status and final location to the external site. If successful, no filter blocks occur, confirming the bypass.

### Step 2: Test Misplaced Protocol Bypass

**Context**: Use a malformed protocol separator to evade validation, tricking the server into accepting the external domain.

**Command** ([[commands/curl-test-redirect]]):
```bash
curl -i -L "https://www.zaption.com/logout?returnTo=http:///evil.com/"
```

> Similar to Step 1, this tests http:///evil.com/, resulting in a 302 redirect. Browsers like Firefox 39.0 resolve this to the malicious domain. Success is indicated by the redirect without server-side rejection.

### Step 3: Validate in Browser

**Context**: Confirm the exploit in a real browser environment to simulate user impact.

**Instructions**: Manually navigate to https://www.zaption.com/logout?returnTo=///evil.com/ in Firefox or Chrome. Observe the automatic redirect to evil.com without alerts.

> No command needed; visual confirmation of redirect to the external site verifies phishing feasibility.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Phishing]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-redirect]]

## Tools Used


## Tags

- open-redirect
- phishing
- url-bypass
- filter-bypass
