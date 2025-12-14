---
tags:
  - xss
  - waf-bypass
  - url-encoding
  - payload-crafting
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.144Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: b307eca0-4d17-49a5-b164-037a87f0160c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Double-Encoded-XSS-Payload-for-WAF-Bypass

## Summary

This procedure involves manually constructing and double URL-encoding an XSS payload to inject malicious attributes into a web page's canonical link tag, specifically designed to evade WAF filters that block double quotes during SQLi or XSS attempts.

## Description

In the context of Starbucks websites, the 404 error pages fail to sanitize user-supplied URL paths when populating the href attribute of the <link rel="canonical"> tag. By crafting a payload that starts with junk text, injects via double quotes, adds an accesskey for triggering, and an onclick handler for JavaScript execution, attackers can reflect the payload. Double encoding (%25 instead of % for quotes) prevents WAF redirection. This targets reflected XSS requiring no authentication but user interaction.

## Requirements

1. Knowledge of target domain structure (e.g., Starbucks .co.uk)
2. Understanding of URL encoding (single and double)
3. Access to a text editor or encoding tool for payload construction
4. Target must have a WAF filtering double quotes

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding for all URL parameters in error pages
- Use Content Security Policy (CSP) to block inline JavaScript execution
- Monitor for anomalous 404 requests with encoded payloads via WAF logs
- Validate and canonicalize URLs server-side before insertion into HTML attributes

## Objectives

1. Create a payload that injects 'accesskey="x" onclick="confirm`1"' into the link tag
2. Double-encode to bypass WAF
3. Ensure payload reflects without breaking the page

## Instructions

### Step 1: Construct Base Payload

**Context**: Build the raw injection string using double quotes to break out of the href attribute, adding triggerable attributes.

No command required; manually assemble:

Raw payload example: htp8bi2zcg" accesskey='x' onclick='confirm`1`' //2injectiontrme47nbfq/blonde/bright-sky-blend/ground=1

> This junk prefix (htp8bi2zcg) avoids path conflicts, " closes the href, accesskey enables keyboard trigger, onclick runs JS, and trailing junk maintains URL validity.

### Step 2: Apply Double URL Encoding

**Context**: Encode the payload twice to evade WAF detection of %22 (single-encoded quote).

No command; use a browser dev tools or online encoder:

Double-encoded: %2522%2520accesskey=%2527x%2527%2520onclick=%2527confirm%601%60%2527%2520//2injectiontrme47nbfq/blonde/bright-sky-blend/ground=1

> First encoding turns " to %22, space to %20, etc.; second turns % to %25, resulting in %2522 for ". Test incrementally to confirm WAF bypass.

### Step 3: Validate Encoding

**Context**: Ensure the full URL doesn't trigger WAF prematurely.

Append to base URL: https://www.starbucks.co.uk/htp8bi2zcg + encoded part.

> Expected: No redirect or block; payload ready for delivery.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- waf-bypass
- payload-crafting
