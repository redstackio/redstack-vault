---
id: proc-test-shop-redirect
tags:
  - open-redirect
  - phishing
  - shopify
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
updated_at: '2025-12-14T17:24:26.668Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Phishing]]'
---
# Test-Open-Redirect-in-Shop-Parameter

## Summary

This procedure tests the 'shop' parameter in the Shopify Alexa app callback URL for open redirect vulnerability by substituting an arbitrary domain, allowing redirects to malicious sites for phishing.

## Description

The callback endpoint https://assistant-client.meteorapp.com/shopify/callback does not validate the 'shop' parameter, permitting any domain value. By replacing the legitimate shop domain with a malicious one (e.g., evil.com), the endpoint redirects users to the attacker-controlled site during app installation, facilitating phishing attacks. This was resolved by Shopify adding domain validation.

## Requirements

1. Captured legitimate callback parameters from prior observation
2. Control over a test domain for redirect target
3. Curl or browser to send modified requests

## Defense

Defensive measures and detection strategies:

- Validate 'shop' parameter against whitelisted Shopify domains
- Log and alert on redirects to non-Shopify domains
- Educate users on verifying app installation URLs

## Objectives

1. Confirm lack of validation by forcing redirect to arbitrary URL
2. Demonstrate phishing potential during installation
3. Report findings for remediation

## Instructions

### Step 1: Modify Shop Parameter

**Context**: Alter the 'shop' value in the callback URL to an arbitrary domain while keeping other parameters intact.

**Command** ([[commands/curl-test-redirect]]):
```bash
curl -v -L "https://assistant-client.meteorapp.com/shopify/callback?code=6aae881ab9c4f12d5b264e6c871a108a&hmac=6109806a12b0439d6a2dce2d547344eb1c2c53e9691259f39eefbb93b9c9c97b&shop=evil.com&timestamp=1494008598"
```

> The -L flag follows redirects. Expected output: 302 status with Location: https://evil.com, confirming open redirect.

### Step 2: Verify Redirect

**Context**: Follow the redirect and ensure it lands on the malicious domain without errors.

Inspect the final response body or use browser to simulate user flow.

> Success if no validation blocks the redirect; potential for phishing page load.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Phishing]] Phishing

### Sub-Techniques


## Commands Used

- [[commands/curl-test-redirect]]

## Tools Used


## Tags

- open-redirect
- phishing
- shopify
