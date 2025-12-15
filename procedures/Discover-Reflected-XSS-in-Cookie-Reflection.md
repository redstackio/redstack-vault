---
tags:
  - xss
  - discovery
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Browser-Dev-Tools]]'
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
updated_at: '2025-12-14T17:33:34.347Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: d4fa35ff-6fc5-477b-abad-4a281155d868
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover Reflected XSS in Cookie Reflection

## Summary

This procedure identifies a reflected XSS vulnerability where the 'guvo' cookie value is unescaped and injected into JavaScript objects like window.ySitRepParams and window.yelp.guv on Yelp pages, allowing arbitrary JS execution.

## Description

The vulnerability occurs because the backend reflects the 'guvo' cookie value directly into client-side JavaScript without proper escaping. By setting a test payload in the 'guvo' cookie and observing its execution on pages like www.yelp.com or biz.yelp.com/login, attackers can confirm the issue. This is typically discovered using browser developer tools to inspect global window objects and Burp Suite to manipulate cookies during requests. Prerequisites include access to the target domain and basic web debugging knowledge. Expected outcome: Confirmation of XSS via alert or console log execution.

## Requirements

1. Network access to *.yelp.com
2. Browser with dev tools (e.g., Chrome)
3. Burp Suite for cookie manipulation
4. No authentication required

## Defense

Defensive measures and detection strategies:

- Sanitize and escape cookie values before JS injection (e.g., use JSON.stringify or HTML entities)
- Implement Content Security Policy (CSP) to restrict inline scripts
- Monitor for anomalous cookie values in logs
- Use WAF rules to block suspicious query parameters like 'canary'

## Objectives

1. Confirm unescaped cookie reflection in JS contexts
2. Identify affected pages (e.g., login, homepage)
3. Establish foundation for payload smuggling

## Instructions

### Step 1: Set Test Cookie

**Context**: Manually set a 'guvo' cookie with a simple XSS payload to test reflection.

**Command** (Browser or Burp):
Set cookie 'guvo=<script>alert(1)</script>' via browser dev tools or Burp Repeater.

```javascript
// In browser console
document.cookie = 'guvo=<script>alert(1)</script>';
```

> Navigate to www.yelp.com; check if alert triggers. Expected: JS execution without escaping.

### Step 2: Inspect Reflection

**Context**: Use dev tools to verify injection into window objects.

**Command** (Dev Tools):

```javascript
// In console
console.log(window.ySitRepParams); console.log(window.yelp.guv);
```

> Look for unescaped payload in object values. Expected: Raw HTML/JS visible and executable.

### Step 3: Confirm with Burp

**Context**: Intercept requests to manipulate and observe.

**Command** (Burp Suite):
Add 'Cookie: guvo=<script>console.log("XSS")</script>' in request headers to biz.yelp.com/login.

> Forward request and check response/console. Expected: Console log fires.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Browser-Dev-Tools]]

## Tags

- xss
- discovery
- cookie
