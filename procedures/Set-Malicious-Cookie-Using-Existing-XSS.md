---
id: proc-uuid-001
name: Set-Malicious-Cookie-Using-Existing-XSS
tags:
  - xss
  - cookie-manipulation
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
updated_at: '2025-12-14T03:16:25.663Z'
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
# Set-Malicious-Cookie-Using-Existing-XSS

## Summary

This procedure exploits an existing cross-site scripting (XSS) vulnerability on a subdomain to inject JavaScript that sets a malicious cookie. The cookie includes a script payload in its name, scoped to the parent domain, enabling it to be visible and exploitable on other subdomains.

## Description

In a web environment with multiple subdomains under a shared domain (e.g., .af.mil), an XSS on one subdomain can be used to set cookies for the broader domain using the 'domain' attribute. This procedure targets endpoints like pop_up_frm.asp that reflect unsanitized parameters, allowing JavaScript execution to manipulate cookies. The outcome is a cookie with an embedded XSS payload that can be reflected elsewhere, leading to chained attacks. Prerequisites include access to the subdomain with the known XSS and browser capabilities for JavaScript execution.

## Requirements

1. Access to a subdomain with a reflected XSS vulnerability (e.g., https://example.mil/kc/main/pop_up_frm.asp?loc=...)
2. Browser with JavaScript enabled and developer tools for verification
3. Network connectivity to the target .mil domains

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected parameters in URLs to prevent XSS
- Implement Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous cookie settings via web application firewall (WAF) logs
- Use HttpOnly flags on sensitive cookies to prevent JavaScript access

## Objectives

1. Inject and execute JavaScript via existing XSS to set a domain-wide cookie
2. Embed a malicious payload in the cookie name for later reflection
3. Prepare for chained exploitation on authenticated endpoints

## Instructions

### Step 1: Identify and Access the Existing XSS Endpoint

**Context**: Locate the subdomain endpoint vulnerable to XSS, such as one that reflects the 'loc' parameter without sanitization.

Navigate to: https://example.mil/kc/main/pop_up_frm.asp?loc=javascript:alert(1)

Verify XSS by observing the alert execution.

### Step 2: Inject Payload to Set Malicious Cookie

**Context**: Craft a JavaScript payload that sets a cookie with the malicious name, using path=/ and domain=.af.mil for broad scope.

Execute the following JavaScript via the XSS:

```javascript
document.cookie = 'zzz<script>alert(document.domain)</script>=zzz;path=/;domain=.af.mil';
```

> This command sets a cookie named 'zzz<script>alert(document.domain)</script>' with value 'zzz', scoped to all .af.mil subdomains. Expected output: No visible response, but verifiable in browser cookies.

### Step 3: Verify Cookie Setting

**Context**: Confirm the cookie is set and visible across subdomains.

Open browser dev tools > Application > Cookies > Select .af.mil domain.

Look for the malicious cookie name.

**Expected Output**: Cookie listed with the embedded script payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- cookie-manipulation
