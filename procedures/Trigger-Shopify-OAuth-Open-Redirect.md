---
tags:
  - open-redirect
  - invalid-scope
  - phishing
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-visit-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:35.490Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 78d8edea-26f8-409c-b8c5-92fbb6445263
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
---
# Trigger-Shopify-OAuth-Open-Redirect

## Summary

This procedure exploits the open redirection vulnerability in Shopify's OAuth by using an invalid scope parameter to bypass redirect URI hostname validation, redirecting users to an arbitrary external phishing site.

## Description

When an invalid scope (e.g., 'a') is provided in the OAuth authorize URL, Shopify fails to validate the redirect URI's hostname, allowing redirection to external domains. This enables phishing attacks where users are tricked into authorizing a malicious app on a fake Shopify page, leading to credential theft. Target is the /admin/oauth/authorize endpoint on a Shopify store. Prerequisites: App client ID and external phishing site. Expected outcome: Unvalidated redirect with error parameters appended, landing on attacker site.

## Requirements

1. Client ID from created app
2. Target store URL and invalid scope value
3. Attacker-controlled redirect target (e.g., https://www.facebook.com/abc)

## Defense

Defensive measures and detection strategies:

- Validate redirect URI hostname regardless of scope validity
- Log and alert on invalid scopes in OAuth requests
- Implement CSRF tokens and state parameters in OAuth flow
- Block or monitor redirects to non-whitelisted domains

## Objectives

1. Bypass redirect URI validation using invalid scope
2. Redirect user to phishing site mimicking Shopify
3. Facilitate malicious app authorization for account compromise

## Instructions

### Step 1: Construct Invalid Scope URL

**Context**: Modify the OAuth URL to include an invalid scope like 'a' while keeping the malicious redirect URI.

**Command** ([[commands/curl-visit-url]]):
```bash
curl -L "https://prans.myshopify.com/admin/oauth/authorize?client_id=616ce3efcd495007438000ad958a6629&scope=a&redirect_uri=https://www.facebook.com/abc" -o redirect_output.html
```

> The -L flag follows redirects. Expected output: Final response from https://www.facebook.com/abc with appended params like ?error=invalid_scope&hmac=07657fedf1815f84248dfc6c372ba002e3ea5041df849080269786ae732aed99&shop=prans.myshopify.com&signature=6ecc20da3eb66500d9245635ead45315&timestamp=1428607537.

### Step 2: Verify Redirection

**Context**: Confirm the bypass by checking the final URL and parameters.

No command; inspect redirect_output.html.

> Look for external domain access and error params. Expected output: Phishing page loaded successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[T1566.002]]

### Sub-Techniques


## Commands Used

- [[commands/curl-visit-url]]

## Tools Used


## Tags

- open-redirect
- invalid-scope
- phishing
- shopify
