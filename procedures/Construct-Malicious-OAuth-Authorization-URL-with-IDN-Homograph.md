---
id: proc-semrush-url-craft-001
name: Construct-Malicious-OAuth-Authorization-URL-with-IDN-Homograph
type: procedure
verified: false
submitted: true
created_at: '2024-09-18T12:00:00Z'
updated_at: '2025-12-14T17:24:39.210Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - oauth
  - idn-homograph
  - url-crafting
commands:
  - '[[commands/curl-oauth-request]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Construct-Malicious-OAuth-Authorization-URL-with-IDN-Homograph

## Summary

This procedure crafts a malicious OAuth authorization URL for Semrush by embedding an IDN homograph in the redirect_uri parameter, exploiting the backend's failure to normalize domains and allowing redirection to an attacker-controlled endpoint.

## Description

In the Semrush OAuth flow, the /oauth2/authorize endpoint does not properly validate or normalize Internationalized Domain Names (IDNs) in the redirect_uri. By using a visually similar domain like 'oauth.šemrush.com' (punycode: oauth.xn--emrush-9jb.com), the backend treats it as equivalent to 'oauth.semrush.com'. The attacker registers the homograph domain in advance. This procedure assumes the attacker has Semrush credentials and focuses on URL construction to initiate the flow, leading to code leakage upon approval. Expected outcome: Backend accepts the invalid redirect_uri, prompting user approval.

## Requirements

1. Valid Semrush account credentials for authentication.
2. Registered attacker-controlled domain using IDN homograph (e.g., 'xn--emrush-9jb.com' via a domain registrar).
3. Web browser or curl for sending the request.
4. Knowledge of Semrush's OAuth client_id (e.g., 'seoquake') and scopes (user.info, projects.info, siteaudit.info).

## Defense

Defensive measures and detection strategies:

- Implement strict redirect_uri validation with IDN normalization (e.g., convert to punycode and exact-match against allowlist).
- Use domain suffix allowlisting instead of prefix matching.
- Monitor for unusual redirect_uris in OAuth logs and alert on non-ASCII characters.
- Employ tools like IDNA library in backend code for canonicalization.

## Objectives

1. Bypass redirect_uri validation to set up code redirection to attacker domain.
2. Initiate OAuth flow without triggering validation errors.
3. Prepare for code capture in subsequent approval step.

## Instructions

### Step 1: Prepare the Homograph Domain

**Context**: Register and set up the attacker-controlled domain to receive redirects. This ensures the homograph resolves to your server.

**Command** ([[commands/register-idn-domain]]):
```bash
# Use a domain registrar CLI or manual registration; example with whois simulation
whois xn--emrush-9jb.com  # Verify availability, then register via provider API
```

> Registers the punycode domain equivalent to 'šemrush.com'. Set up a simple HTTP server to log incoming requests.

### Step 2: Authenticate and Construct URL

**Context**: Log in to Semrush if needed, then build and send the OAuth request with the malicious redirect_uri.

**Command** ([[commands/curl-oauth-request]]):
```bash
curl -X GET "https://oauth.semrush.com/oauth2/authorize?response_type=code&scope=user.info,projects.info,siteaudit.info&client_id=seoquake&redirect_uri=https://oauth.šemrush.com/oauth2/success" -v -c cookies.txt
```

> Sends the request; -v shows verbose output to confirm no validation error. The redirect_uri uses the homograph. Expected output: HTML approval page from Semrush.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-oauth-request]]

## Tools Used


## Tags

- oauth
- idn-homograph
- url-crafting
