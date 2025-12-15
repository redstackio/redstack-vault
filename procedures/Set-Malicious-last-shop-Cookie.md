---
id: proc-set-malicious-last-shop-cookie
tags:
  - cookie-manipulation
  - open-redirect
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-set-cookie-and-visit]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Pass the Hash]]'
updated_at: '2025-12-14T17:24:26.489Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Pass the Hash]]'
---
# Set-Malicious-last-shop-Cookie

## Summary

This procedure manipulates the 'last_shop' cookie in Shopify's domain to contain an arbitrary attacker-controlled URL, bypassing validation and setting up for an open redirect attack. It is primarily used in phishing scenarios to trick users into visiting malicious sites under the guise of legitimate Shopify navigation.

## Description

The Shopify admin endpoint at https://www.shopify.com/admin/* relies on the 'last_shop' cookie to determine redirect destinations without validating the input. An attacker can set this cookie to any domain, such as https://attacker.com, causing subsequent visits to redirect there. This requires no authentication and can be done via browser tools or HTTP requests. Prerequisites include access to the victim's browser session or a way to inject the cookie (e.g., via prior XSS). Expected outcomes include successful cookie persistence and preparation for phishing.

## Requirements

1. Access to browser developer tools or curl for cookie setting
2. Valid Shopify domain access (no login required)
3. Attacker-controlled domain ready for hosting phishing content

## Defense

Defensive measures and detection strategies:

- Implement strict cookie validation on server-side, whitelisting allowed domains
- Use HttpOnly and Secure flags on sensitive cookies to prevent client-side tampering
- Monitor for anomalous redirects in access logs and alert on non-Shopify domains

## Objectives

1. Tamper with 'last_shop' cookie to arbitrary value
2. Ensure cookie is set for the Shopify domain
3. Prepare for redirect exploitation without detection

## Instructions

### Step 1: Prepare Attacker Domain

**Context**: Ensure your malicious site is hosted and mimics Shopify to enhance phishing success.

No command needed; host a phishing page at https://attacker.com/admin/.

### Step 2: Set the Cookie

**Context**: Use curl or browser to inject the malicious value into the 'last_shop' cookie.

**Command** ([[commands/curl-set-cookie-and-visit]]):
```bash
curl -c cookies.txt -b "last_shop=https://attacker.com" -H "Host: www.shopify.com" https://www.shopify.com/admin/auth
```

> This command creates a cookie jar file and sets the 'last_shop' cookie to the attacker domain while accessing a Shopify admin path. Expected output: HTTP response without errors, cookie saved in cookies.txt.

### Step 3: Verify Cookie Setting

**Context**: Confirm the cookie is applied correctly.

**Command** ([[commands/curl-set-cookie-and-visit]]):
```bash
curl -b cookies.txt https://www.shopify.com -I
```

> Inspects headers to verify cookie presence. Expected output: 200 OK or redirect, with cookie in request headers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Pass the Hash]]

### Sub-Techniques


## Commands Used

- [[commands/curl-set-cookie-and-visit]]

## Tools Used


## Tags

- [[cookie-manipulation]]
- [[open-redirect]]
