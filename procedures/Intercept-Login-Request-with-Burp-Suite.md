---
tags:
  - burp-suite
  - intercept
  - asp-net
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-simulate-login]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:12.215Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 30476055-a846-40c4-93b2-d9af4a4ce1a5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Login-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to simulate a failed login attempt with the victim's email, intercepting the response to extract valid ASP.NET state values like __VIEWSTATE and __EVENTVALIDATION for use in password reset requests.

## Description

ASP.NET applications rely on __VIEWSTATE and __EVENTVALIDATION for form integrity, which are generated per session or page load. By attempting a login with a random password, an attacker can obtain fresh tokens without alerting the user. This is done via proxy interception in Burp Suite, targeting the /Login.aspx endpoint. The attack assumes no rate limiting on login attempts and works in unauthenticated contexts.

## Requirements

1. Burp Suite installed and configured as a proxy (e.g., browser traffic routed through 127.0.0.1:8080)
2. Victim's email address
3. Random password for failed login simulation
4. Target URL accessible

## Defense

Defensive measures and detection strategies:

- Enforce rate limiting on login attempts per IP/email
- Invalidate __VIEWSTATE after failed logins or short TTL
- Log and alert on repeated failed logins from the same IP
- Use CSRF tokens separate from ViewState

## Objectives

1. Simulate login to trigger page state generation
2. Intercept and extract __VIEWSTATE and __EVENTVALIDATION
3. Avoid actual authentication to remain stealthy

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up interception to capture requests and responses.

**Command** ([[commands/curl-simulate-login]]):
```bash
curl -x 127.0.0.1:8080 -X POST https://example.mil/Login.aspx \
  -d "txtUserName=victim@example.com&txtPassword=random123&btnLogin=Login" \
  -v -c cookies.txt
```

> Route through Burp proxy. In Burp, enable Intercept on Proxy tab. Expected output: Paused request in Burp for modification if needed, then response with HTML containing state values.

### Step 2: Extract State Tokens

**Context**: From the intercepted response, copy __VIEWSTATE and __EVENTVALIDATION.

**Command** ([[commands/curl-simulate-login]]):
```bash
# After interception, inspect response in Burp or save to file
grep -oP '__VIEWSTATE="\K[^"]*' response.html
grep -oP '__EVENTVALIDATION="\K[^"]*' response.html
```

> Use grep on the saved response to extract tokens. Expected output: Base64-encoded strings for each token.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-simulate-login]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[tools/Burp-Suite]]
- [[intercept]]
