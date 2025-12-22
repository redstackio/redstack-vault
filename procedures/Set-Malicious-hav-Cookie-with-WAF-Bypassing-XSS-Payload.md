---
id: proc-uuid-set-hav-cookie
tags:
  - waf-bypass
  - xss-payload
  - cookie-injection
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
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.470Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Set-Malicious-hav-Cookie-with-WAF-Bypassing-XSS-Payload

## Summary

This procedure crafts and sets a malicious 'hav' cookie value containing an XSS payload designed to bypass the WAF on abritel.fr by exploiting the server's handling of double quotes, enabling injection of script tags into reflected content.

## Description

The 'hav' cookie is reflected unsanitized in a JavaScript file response. The WAF blocks direct XSS patterns like `</script>`, but by using double quotes (e.g., `xss"</sc"ript>`), the server hides the quotes, allowing the payload to form complete tags like `<svg/onload=alert(...)>` after reflection. This step prepares the payload for cache poisoning, targeting PHP-based web apps with caching.

## Requirements

1. Access to HTTP request tools (browser or proxy) to set custom cookies
2. Knowledge of the target endpoint (e.g., abritel.fr)
3. No authentication required for public endpoints

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected cookie values server-side
- Implement strict CSP to block inline script execution
- Monitor for anomalous cookie values and WAF logs for bypass attempts

## Objectives

1. Inject a WAF-bypassing XSS payload into the 'hav' cookie
2. Ensure reflection without blocking
3. Prepare for cache poisoning in subsequent steps

## Instructions

### Step 1: Craft the Payload

**Context**: Build the obfuscated XSS payload using double quotes to split blocked strings, targeting the reflection point in `var hav="value"`.

Use a payload like: `xss"</sc"ript><sv"g/onloa"d=aler"t(window.INITIAL_STATE.system.cookie)>`

This results in reflected output like `var hav="xss"</sc"ript><sv"g/onloa"d=aler"t(...)">`, where hidden quotes allow `<svg/onload=alert(...)>` to execute.

### Step 2: Set the Cookie

**Context**: Attach the payload as the 'hav' cookie value in an HTTP request to test reflection.

Send a request with header: `Cookie: hav=xss"</sc"ript><sv"g/onloa"d=aler"t(1)>`

> Inspect the response for reflection in the .js file; success if payload appears without WAF block.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- N/A

## Commands Used

- N/A

## Tools Used

- N/A

## Tags

- [[waf-bypass]]
- [[xss]]
- [[cookie-manipulation]]
