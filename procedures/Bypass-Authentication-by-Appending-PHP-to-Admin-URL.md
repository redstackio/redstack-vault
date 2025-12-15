---
id: proc-uuid-001
tags:
  - auth-bypass
  - shopify
  - php
  - okta
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-fetch-admin-page]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:36.883Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Authentication-by-Appending-PHP-to-Admin-URL

## Summary

This procedure exploits an improper authentication mechanism in Shopify subdomains by appending '.php' to the /admin endpoint, bypassing the Okta redirect and granting unauthorized access to the admin dashboard, including exposure of the CSRF authenticity_token.

## Description

The vulnerability stems from inconsistent routing in the PHP-based application, where the standard /admin path enforces Okta authentication via redirect to https://shopify.okta.com, but /admin.php does not perform the same checks, allowing direct loading of administrative content. This enables unauthorized viewing of admin information and potential CSRF attacks using the exposed token. Target subdomains include datastories.shopify.com and data-stories-website.shopifycloud.com. No editing of sensitive data is possible without further authentication, but the exposure poses risks for reconnaissance and chained attacks.

## Requirements

1. Internet access to public Shopify subdomains
2. Web browser or curl for URL access
3. Knowledge of target subdomain (e.g., datastories.shopify.com)

## Defense

Defensive measures and detection strategies:

- Implement consistent authentication checks across all routing endpoints, including extension variations like .php
- Use web application firewalls (WAF) to detect and block anomalous URL patterns targeting admin paths
- Monitor access logs for direct hits to /admin.php without preceding Okta authentication
- Regularly audit routing configurations in PHP applications for bypass opportunities

## Objectives

1. Gain unauthorized access to the admin dashboard
2. Extract administrative information and CSRF tokens
3. Enable potential CSRF attacks on authenticated users

## Instructions

### Step 1: Identify Target Subdomain

**Context**: Locate vulnerable subdomains through reconnaissance, such as datastories.shopify.com or data-stories-website.shopifycloud.com.

No command required; use manual browsing or DNS tools to confirm subdomain existence.

### Step 2: Access Modified Admin URL

**Context**: Append '.php' to the /admin endpoint to bypass the authentication redirect.

**Command** ([[commands/curl-fetch-admin-page]]):
```bash
curl -s https://datastories.shopify.com/admin.php
```

> This command fetches the admin dashboard without authentication. Expected output includes HTML with admin elements and <meta name="csrf-param" content="authenticity_token" value="...">. If successful, no redirect headers (e.g., Location: https://shopify.okta.com) appear.

### Step 3: Verify Exposure

**Context**: Inspect the response for administrative content and CSRF token.

Use browser dev tools (Ctrl+U) or pipe curl output to grep:

```bash
curl -s https://datastories.shopify.com/admin.php | grep authenticity_token
```

> Expected output: Lines containing the CSRF token value, confirming exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-admin-page]]

## Tools Used


## Tags

- auth-bypass
- shopify
- php
- okta
