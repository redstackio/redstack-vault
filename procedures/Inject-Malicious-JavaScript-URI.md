---
tags:
  - xss
  - payload-injection
  - javascript-uri
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:30.576Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 68ba7237-e91b-4dde-be5d-21a8b23ed213
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-JavaScript-URI

## Summary

This procedure modifies an intercepted API request to replace a benign link with a malicious javascript: URI, exploiting the lack of protocol validation in Infogram's media update endpoint to store an XSS payload.

## Description

Targeting the `/api/infographics/update/[project_id]` endpoint, this procedure intercepts the POST request during link insertion, alters the URL parameter to a javascript: scheme (e.g., javascript:alert(document.domain)), and forwards it. The server stores the payload without sanitization, enabling stored XSS. Prerequisites include an active interception setup; outcomes include persistent malicious links in the infographic.

## Requirements

1. Intercepted API request from prior setup
2. Knowledge of the request structure (JSON body with link field)
3. Web debugger with modification capabilities
4. Valid Infogram session

## Defense

Defensive measures and detection strategies:

- Validate all URLs to enforce http[s]:// schemes only on the server-side
- Sanitize inputs using allowlists for protocols in media links
- Monitor for javascript: or other dangerous schemes in logs
- Use WAF rules to block non-standard URI schemes

## Objectives

1. Bypass protocol validation by injecting javascript: URI
2. Store the payload server-side for persistence
3. Enable client-side execution upon user interaction

## Instructions

### Step 1: Locate Payload Field

**Context**: Identify the modifiable link parameter in the request.

In the intercepted POST body, find the JSON field containing the benign URL (e.g., {"link": "http://google.com"}).

> Request example: POST https://infogram.com/api/infographics/update/[project_id] with Content-Type: application/json.

### Step 2: Modify to Malicious URI

**Context**: Replace with XSS payload.

Edit the link value to "javascript:alert(document.domain)".

> This injects executable JavaScript; for real attacks, use payloads like stealing cookies via document.cookie.

### Step 3: Forward Request

**Context**: Submit the altered request to the server.

Click 'Forward' in the debugger to send the modified POST.

> Server responds with 200 OK if accepted, storing the payload.

### Step 4: Verify Storage

**Context**: Confirm the change persisted.

Refresh the infographic editor and check the media link.

> Success: Link now shows as javascript: URI (though UI may not display it directly).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- stored-xss
- uri-injection
