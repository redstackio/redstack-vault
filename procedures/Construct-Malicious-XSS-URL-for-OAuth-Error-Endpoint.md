---
tags:
  - xss
  - reflected-xss
  - url-construction
type: procedure
tools:
  - '[[tools/Firefox-Browser]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:38.921Z'
sub_techniques: []
id: 178c7972-3d63-4495-b6a7-1a48146534c5
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Construct-Malicious-XSS-URL-for-OAuth-Error-Endpoint

## Summary

This procedure involves crafting a malicious URL targeting the ORY Hydra OAuth 2.0 error endpoint, injecting an XSS payload into query parameters that are reflected without sanitization, enabling JavaScript execution upon page load.

## Description

In the context of the auth2.zomato.com OAuth error endpoint, parameters like error, error_description, and error_hint are directly inserted into the HTML response. By URL-encoding a malicious HTML element such as a marquee tag with an onfinish event handler calling confirm(document.cookie), an attacker can execute JavaScript to steal cookies. This is useful for phishing attacks where victims are tricked into visiting the URL during an OAuth flow error, leading to session hijacking.

## Requirements

1. Knowledge of the target endpoint: https://auth2.zomato.com/oauth2/fallbacks/error
2. Basic understanding of URL encoding and HTML/JavaScript payloads
3. Access to a text editor or browser for URL construction

## Defense

Defensive measures and detection strategies:

- Implement output encoding for all user-controlled inputs in HTML contexts (e.g., use HTML entity encoding)
- Validate and sanitize query parameters before reflection
- Deploy Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous error endpoint accesses with suspicious query strings

## Objectives

1. Create a functional XSS payload URL for the OAuth error endpoint
2. Ensure the payload evades basic filtering and executes reliably
3. Prepare the URL for phishing delivery to authenticated users

## Instructions

### Step 1: Identify Vulnerable Parameters

**Context**: Determine which query parameters are reflected without sanitization in the error page HTML.

From testing, use error, error_description, and error_hint as they are inserted directly.

### Step 2: Craft the Payload

**Context**: Design a JavaScript payload that executes upon page render, such as displaying cookies in a confirm dialog for proof-of-concept.

Construct the payload: <marquee loop=1 width=0 onfinish=confirm(document.cookie)>XSS</marquee>. URL-encode it for the error_hint parameter: %3Cmarquee%20loop%3d1%20width%3d0%20onfinish%3dconfirm(document.cookie)%3EXSS%3C%2fmarquee%3E.

### Step 3: Assemble the Full URL

**Context**: Combine the endpoint with benign parameters and the malicious one.

Full URL: https://auth2.zomato.com/oauth2/fallbacks/error?error=xss&error_description=xsssy&error_hint=%3Cmarquee%20loop%3d1%20width%3d0%20onfinish%3dconfirm(document.cookie)%3EXSS%3C%2fmarquee%3E

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-Browser]]

## Tags

- xss
- oauth
- payload-crafting
