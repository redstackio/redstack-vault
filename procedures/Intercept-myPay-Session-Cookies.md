---
id: proc-uuid-1
tags:
  - session-hijacking
  - cookie-interception
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:12.254Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Intercept-myPay-Session-Cookies

## Summary

This procedure captures valid session cookies from the DoD myPay system by intercepting legitimate requests, enabling authenticated access to internal endpoints like password reset without owning the original session.

## Description

In the context of exploiting the myPay system's improper authentication, this step involves accessing the myPay website and using a proxy or browser tools to extract session cookies (LastMRH_Session, F5_ST, MRHSession). These cookies allow subsequent requests to bypass basic session checks. Prerequisites include a browser with proxy capabilities and public access to https://mypay.dfas.mil. Expected outcome: Cookies that can be reused in crafted requests for account takeover.

## Requirements

1. Browser with developer tools or proxy (e.g., Burp Suite, but basic browser proxy suffices)
2. Public internet access to myPay site
3. No credentials needed for initial visit

## Defense

Defensive measures and detection strategies:

- Implement cookie security flags (HttpOnly, Secure, SameSite=Strict)
- Monitor for anomalous session usage from unfamiliar IPs
- Rate-limit session cookie usage on sensitive endpoints

## Objectives

1. Obtain reusable session tokens for authenticated requests
2. Enable exploitation of internal APIs without full login
3. Prepare for password reset bypass

## Instructions

### Step 1: Access myPay Site

**Context**: Visit the legitimate myPay login or home page to initiate a session.

Navigate to https://mypay.dfas.mil/ in a browser.

### Step 2: Intercept Request

**Context**: Capture cookies from any request during the visit, such as loading the page or submitting a form.

Use browser developer tools (Network tab) or a proxy to inspect and copy cookies: LastMRH_Session, F5_ST, MRHSession.

**Expected Output**: Cookies in format like 'LastMRH_Session=abc123; F5_ST=def456; MRHSession=ghi789...'

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- session-interception
- web-proxy
