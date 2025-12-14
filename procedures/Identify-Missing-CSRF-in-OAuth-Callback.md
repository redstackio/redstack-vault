---
id: proc-identify-csrf-oauth
tags:
  - csrf
  - oauth
  - inspection
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
updated_at: '2025-12-14T17:24:35.277Z'
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
# Identify-Missing-CSRF-in-OAuth-Callback

## Summary

This procedure involves inspecting the OAuth callback endpoint in Shopify's Pinterest integration to identify the lack of a state parameter, confirming a CSRF vulnerability that allows forged requests.

## Description

In the context of Shopify's Pinterest account attachment feature, the OAuth callback at https://pinterest-commerce.shopifyapps.com/auth/pinterest/callback?code=... processes authorization codes without validating a state parameter. This omission enables attackers to forge requests using a victim's authenticated session, leading to unauthorized actions. The procedure uses browser inspection to verify the vulnerability, applicable in web-based OAuth flows lacking anti-CSRF measures. Expected outcome is confirmation of the flaw, setting up exploitation.

## Requirements

1. Access to a Shopify account with Pinterest integration enabled
2. Browser with developer tools (e.g., Chrome DevTools)
3. Basic knowledge of OAuth flows and network inspection

## Defense

Defensive measures and detection strategies:

- Implement state parameters in all OAuth callbacks with server-side validation
- Use CSRF tokens in forms and validate on submission
- Monitor for anomalous OAuth attachments in application logs

## Objectives

1. Confirm absence of CSRF protection in the callback endpoint
2. Document the vulnerable URL and parameters
3. Prepare for exploitation by noting session requirements

## Instructions

### Step 1: Initiate OAuth Flow

**Context**: Start the Pinterest account attachment process in Shopify to trigger the callback and inspect it.

Navigate to the Shopify admin panel, go to the Pinterest app integration, and click to attach a Pinterest account. Monitor the Network tab in browser dev tools for the redirect to Pinterest and back to the callback.

**Expected Output**: See the callback request with only ?code= parameter, no ?state=.

### Step 2: Verify Lack of Validation

**Context**: Test if the endpoint accepts requests without state by simulating a direct access.

Use the browser console or a tool like curl to send a request to the callback URL with a dummy code, including your session cookie. Observe if it processes without error.

Example test request:

```bash
curl -X GET "https://pinterest-commerce.shopifyapps.com/auth/pinterest/callback?code=DUMMY_CODE" -H "Cookie: your_shopify_session=SESSION_VALUE"
```

> This command simulates the callback; successful response without state validation indicates the vulnerability.

**Expected Output**: Server accepts the request and may return an attachment confirmation or error unrelated to CSRF.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[oauth]]
