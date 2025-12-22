---
id: ac-uuid-cache-poisoning-hav-xss
tags:
  - cache-poisoning
  - xss
  - waf-bypass
  - cookie-injection
  - account-takeover
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Malicious-hav-Cookie-with-WAF-Bypassing-XSS-Payload]]'
  - '[[procedures/Poison-Cache-by-Requesting-Vulnerable-Endpoint]]'
  - '[[procedures/Trigger-XSS-on-Victim-Access-to-Poisoned-Cache]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.487Z'
description: >-
  A multi-stage attack exploiting unsanitized reflection of the 'hav' cookie in
  a cacheable JavaScript file, bypassing WAF with double quotes, poisoning the
  cache to deliver stored XSS that steals session tokens.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Cache Poisoning via 'hav' Cookie Leading to Stored XSS and Account Takeover

Multi-stage attack chain demonstrating a complete attack workflow exploiting a web application's cache poisoning vulnerability to deliver stored XSS via the 'hav' cookie on abritel.fr.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Set Malicious Cookie] --> B[Poison Cache]
    B --> C[Trigger XSS on Victim]
    C --> D[Steal Session Token]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or a proxy like Burp Suite for cookie manipulation

### Target Environment

- Web platform (PHP-based site like abritel.fr)
- Access to set cookies via HTTP requests
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- No credentials needed; public-facing web application
- Ability to send crafted HTTP requests
- Victim interaction for final exploitation

## Detailed Attack Procedures

### Step 1: Set Malicious 'hav' Cookie
procedure: [[procedures/Set-Malicious-hav-Cookie-with-WAF-Bypassing-XSS-Payload]]

**Objective**: Craft and set a 'hav' cookie containing a WAF-bypassing XSS payload to exploit the unsanitized reflection.

**Instructions**: Use browser tools or a proxy to set the cookie with a payload that leverages double quote hiding by the server, such as `xss"</sc"ript><sv"g/onloa"d=aler"t(window.INITIAL_STATE.system.cookie)>`. This bypasses WAF rules blocking direct script tags.

**Expected Output**: Cookie set successfully in the request headers.

**Success Indicators**:
- Cookie value reflected in subsequent responses without sanitization
- No WAF block triggered

### Step 2: Poison Cache by Requesting Vulnerable Endpoint
procedure: [[procedures/Poison-Cache-by-Requesting-Vulnerable-Endpoint]]

**Objective**: Send a request to the cacheable endpoint with the poisoned cookie, causing the server to cache the malicious JavaScript response.

**Instructions**: Issue a GET request to `https://www.abritel.fr/annonces/location-vacances/france_midi-pyrenees_46_stcere_dt0.php.js` including the malicious 'hav' cookie. The reflection in `var hav="value"` will inject the XSS payload into the cached .js file.

**Expected Output**: Server responds with the .js file containing the reflected payload; subsequent requests from other users pull the poisoned cache.

**Success Indicators**:
- Response includes injected `<svg/onload=alert(...)>` after the bypassed quotes
- Cache hit confirmed on repeat requests

### Step 3: Trigger XSS on Victim Access to Poisoned Cache
procedure: [[procedures/Trigger-XSS-on-Victim-Access-to-Poisoned-Cache]]

**Objective**: Induce a victim to load the poisoned .js file, executing the XSS to steal their session cookie.

**Instructions**: Direct the victim to a page that loads the vulnerable .js endpoint (e.g., via a phishing link to abritel.fr listings). The cached XSS executes, accessing `window.INITIAL_STATE.system.cookie` to exfiltrate the session token, enabling account takeover.

**Expected Output**: JavaScript alert or network request exfiltrating the victim's cookie value.

**Success Indicators**:
- XSS payload executes in victim's browser
- Session token captured and usable for takeover

## Attack Chain Summary

### Key Achievements

1. Bypassed WAF using double quote obfuscation in cookie payload
2. Poisoned server cache to persist XSS across users
3. Achieved stored XSS leading to session theft and full account compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
