---
id: proc-trigger-shopify-admin-redirect
tags:
  - open-redirect
  - phishing
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
  - '[[Drive-by Compromise]]'
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:26.478Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[T1566.002]]'
---
# Trigger-Shopify-Admin-Redirect

## Summary

This procedure triggers an open redirect in Shopify's admin endpoint by accessing https://www.shopify.com/admin/* with a tampered 'last_shop' cookie, forcing the server to redirect to an arbitrary attacker-controlled domain. It enables phishing by making the redirect appear legitimate from Shopify.

## Description

Without validation, the server uses the 'last_shop' cookie value directly for redirects, allowing attackers to specify external domains. This can trick users into entering credentials on fake sites. The attack assumes the cookie is already set and requires only a visit to the admin URL. Outcomes include successful redirection and potential data theft via phishing.

## Requirements

1. Pre-set malicious 'last_shop' cookie from prior procedure
2. Network access to Shopify and attacker domain
3. Victim interaction to visit the admin page

## Defense

Defensive measures and detection strategies:

- Validate redirect URLs against a whitelist of trusted domains
- Log all redirects and flag external or unexpected destinations
- Educate users on verifying URLs before following redirects

## Objectives

1. Force redirect to malicious domain
2. Impersonate Shopify for phishing
3. Capture user data on attacker site

## Instructions

### Step 1: Load Cookie Jar

**Context**: Ensure the tampered cookie is available for the request.

No command; use previously saved cookies.txt.

### Step 2: Access Admin Endpoint

**Context**: Visit the vulnerable URL to trigger the redirect based on the cookie.

**Command** ([[commands/curl-set-cookie-and-visit]]):
```bash
curl -b cookies.txt -L https://www.shopify.com/admin/ -v
```

> Follows redirects (-L) and verbose output (-v) to observe the flow. Expected output: 302 redirect to https://attacker.com/admin/*, then 200 from attacker site.

### Step 3: Validate Redirect

**Context**: Confirm the phishing page loads.

Inspect the final URL in browser or curl output to ensure redirection occurred.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[T1566.002]]

### Sub-Techniques


## Commands Used

- [[commands/curl-set-cookie-and-visit]]

## Tools Used


## Tags

- [[open-redirect]]
- [[Phishing]]
