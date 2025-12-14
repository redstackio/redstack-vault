---
id: proc-craft-shopify-url
tags:
  - open-redirect
  - url-crafting
  - shopify
type: procedure
tools: []
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
updated_at: '2025-12-14T17:24:30.656Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-Shopify-Login-URL

## Summary

This procedure involves constructing a malicious login URL for Shopify's endpoint by manipulating the return_to parameter to include an attacker-controlled domain, exploiting the lack of validation for arbitrary redirects.

## Description

In the context of Shopify's login at https://ecommerce.shopify.com/accounts, the return_to parameter is used to specify a post-login redirect URL. Due to insufficient validation, attackers can set this to an external domain like @evil.com by URL-encoding the @ symbol as %40. When a victim logs in via this URL, they are redirected to the malicious site after authentication, allowing for phishing or session hijacking. This targets web users with Shopify access and requires no special tools, only basic URL knowledge.

## Requirements

1. Access to an attacker-controlled domain (e.g., evil.com) to host the malicious redirect target
2. Knowledge of the target login endpoint: https://ecommerce.shopify.com/accounts
3. Basic understanding of URL encoding (e.g., %40 for @)

## Defense

Defensive measures and detection strategies:

- Validate return_to parameters to ensure they match whitelisted domains or relative paths
- Implement redirect confirmation prompts for external URLs
- Monitor for unusual redirect patterns in application logs

## Objectives

1. Create a functional malicious URL that evades basic validation
2. Set up for post-authentication redirection to steal data
3. Enable phishing attacks on authenticated users

## Instructions

### Step 1: Identify Base Endpoint

**Context**: Start with the legitimate Shopify login URL to ensure the base is correct.

No command needed; manually note https://ecommerce.shopify.com/accounts as the base.

> This ensures the login page loads legitimately, building victim trust.

### Step 2: Append and Encode Malicious Parameter

**Context**: Add the return_to parameter with the encoded malicious domain to trigger the open redirect.

Manually construct:

```url
https://ecommerce.shopify.com/accounts?return_to=%40evil.com/
```

> The %40 decodes to @, making the redirect resolve to evil.com. Test the URL in a browser to confirm it loads the login page without errors.

### Step 3: Verify URL Functionality

**Context**: Test the crafted URL to ensure it accepts credentials but redirects maliciously.

Access the URL in a test browser, enter dummy credentials, and observe the redirect to evil.com upon "success."

> Expected: Login form appears; post-submit redirect to malicious site.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- open-redirect
- shopify
- url-manipulation
