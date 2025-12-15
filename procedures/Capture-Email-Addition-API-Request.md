---
id: proc-uuid-002
tags:
  - api
  - intercept
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/add-email-api-post]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:22.805Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-Email-Addition-API-Request

## Summary

This procedure intercepts the HTTP POST request sent when adding an email via the Mozilla Monitor web interface, capturing essential headers and payload for later replay and modification.

## Description

The email addition feature uses a POST to /api/v1/user/email with JSON payload containing the email address. Capturing this reveals session cookies, CSRF tokens, and other auth details needed for exploitation. This is performed in a staging environment to avoid production impact.

## Requirements

1. Burp Suite installed and running as a proxy
2. Browser proxy configured to 127.0.0.1:8080
3. Authenticated session in Mozilla Monitor

## Defense

Defensive measures and detection strategies:

- Enforce strict CSRF token validation
- Monitor for unusual proxy-like User-Agent strings
- Log all API access with IP and session tracking

## Objectives

1. Obtain the exact API request format
2. Extract dynamic tokens (CSRF, cookies)
3. Replicate the request for testing

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to intercept traffic from the browser.

Launch Burp Suite and ensure the proxy listener is active on port 8080.

> Expected: Browser traffic routes through Burp.

### Step 2: Trigger Email Addition

**Context**: Perform a manual addition to capture the request.

Navigate to /user/settings, enter an email, and submit.

**Command** ([[commands/add-email-api-post]]):
```bash
curl -X POST https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/api/v1/user/email \
  -H "Cookie: connect.sid=█████; _ga=GA1.1.518394987.16793330654" \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0" \
  -H "X-Csrf-Token: 0787d9f55701a244aa8f68401f2dc6aebb55a1b83ee2930743ba1324314b5c2cb87fafa7bac74afd8d4660feff2ce33d5b38fb949478c5b9f32430e863ced6b4" \
  -H "Content-Type: application/json" \
  -H "Referer: https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/user/settings" \
  -d '{"email":"example@email.com"}'
```

> Expected: Intercepted request shows POST with JSON body and auth headers; response is 200 OK.

### Step 3: Save Request

**Context**: Forward the request in Burp and copy it for Intruder.

Right-click the request in Burp Proxy and select "Send to Intruder".

> Expected: Request template ready for payload configuration.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/add-email-api-post]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- api
- intercept
- web
