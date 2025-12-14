---
id: proc-open-redirect-uber-trigger-125000
tags:
  - open-redirect
  - path-traversal
  - phishing
  - web-vulnerability
type: procedure
tools:
  - '[[tools/Chrome-Browser]]'
  - '[[tools/Firefox-Browser]]'
  - '[[tools/Internet-Explorer-11]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:27.041Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Open-Redirect-in-m-uber-com-via-Path-Traversal

## Summary

This procedure exploits an open redirect vulnerability in Uber's m.uber.com subdomain by crafting a malformed URL that leverages path traversal flaws in the outdated expressjs/serve-static middleware, allowing attackers to redirect users to arbitrary external domains for phishing or bypassing controls.

## Description

The vulnerability stems from an outdated version of the serve-static middleware in Express.js, which mishandles certain URL path encodings like `//youtube.com/%2F..`. When a user accesses such a URL on https://m.uber.com/, the server responds with a 303 See Other status and a Location header pointing to the injected domain (e.g., //youtube.com/%2F..). This enables phishing attacks by tricking users into visiting malicious sites disguised as legitimate redirects. The issue was reported in March 2016 and documented in serve-static GitHub issue #26. No authentication is required, making it accessible to anyone with a browser.

## Requirements

1. Web browser (e.g., Chrome, Firefox, or Internet Explorer 11) with developer tools for inspecting responses
2. Public internet access to https://m.uber.com/
3. Knowledge of URL encoding (%2F for /) and path traversal basics

## Defense

Defensive measures and detection strategies:

- Update expressjs/serve-static to the latest version to fix path handling issues
- Implement URL validation on redirects to whitelist allowed domains
- Monitor server logs for anomalous 303 responses with external Location headers
- Use Content Security Policy (CSP) headers to restrict navigation

## Objectives

1. Redirect users from a trusted domain (m.uber.com) to a controlled malicious site
2. Facilitate phishing by mimicking legitimate redirects
3. Bypass any client-side security checks relying on the origin domain

## Instructions

### Step 1: Craft the Malformed URL

**Context**: Construct a URL that exploits the path traversal vulnerability in serve-static by injecting an external domain after a double slash and using encoded traversal sequences.

Navigate directly in the browser address bar to:

```plaintext
https://m.uber.com//youtube.com/%2F..
```

> This URL tricks the middleware into interpreting the path as leading to an external resource, resulting in a redirect. Replace 'youtube.com' with any target domain for testing.

### Step 2: Access the URL and Observe Response

**Context**: Load the URL in a browser to trigger the server-side redirect and verify the vulnerability.

Open the browser's developer tools (Network tab) and load the URL. The server will respond with:

- HTTP/1.1 303 See Other
- Location: //youtube.com/%2F..

> The browser follows the redirect to the external site. In a real attack, host a phishing page on the target domain to capture credentials or deliver malware.

### Step 3: Validate the Redirect

**Context**: Confirm the impact by checking if the redirect occurs across different browsers and inspecting the Location header.

Test in multiple browsers (Chrome, Firefox, IE11). Successful validation shows consistent redirection without errors.

> Expected outcome: User is seamlessly redirected, potentially unaware of the origin manipulation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Browser]]
- [[tools/Firefox-Browser]]
- [[tools/Internet-Explorer-11]]

## Tags

- open-redirect
- path-traversal
- phishing
- web-vulnerability
