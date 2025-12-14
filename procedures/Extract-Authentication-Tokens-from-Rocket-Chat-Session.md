---
id: proc-rocket-extract-tokens
tags:
  - token-extraction
  - session-hijacking
  - rocket-chat
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:58.335Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Extract-Authentication-Tokens-from-Rocket-Chat-Session

## Summary

This procedure involves inspecting an active Rocket.Chat session to extract the rc_uid and rc_token, enabling scripted API requests for further exploitation like blind regex searches.

## Description

Following authentication, tokens are stored in browser cookies or headers. This step targets the web session in Rocket.Chat to harvest these for use in Python scripts. The approach uses browser dev tools, with outcomes being usable tokens for authenticated endpoints. Requires an active low-privilege session.

## Requirements

1. Active authenticated session in browser
2. Browser with developer tools (e.g., Chrome DevTools)
3. Basic knowledge of HTTP headers and cookies

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS to protect token transmission
- Rotate tokens frequently and monitor for unusual API usage
- Log and alert on token extraction attempts via dev tools patterns

## Objectives

1. Obtain rc_uid for user identification
2. Secure rc_token for API authentication
3. Prepare for scripted attacks without re-authentication

## Instructions

### Step 1: Open Developer Tools

**Context**: Access session details post-login.

In the browser, press F12 or right-click > Inspect to open DevTools.

### Step 2: Inspect Cookies or Headers

**Context**: Locate and copy token values.

Navigate to Application > Cookies or Network tab, find requests to Rocket.Chat API, and copy rc_uid (user ID) and rc_token from headers/cookies.

> Example values: rc_uid = "user123", rc_token = "abc123def456...". Paste into a secure note for scripting.

### Step 3: Validate Tokens

**Context**: Test tokens in a simple API call.

Use a tool like curl to verify: Send a GET to /api/v1/me with X-Auth-Token and X-User-Id headers using the extracted values.

> Expected: JSON response with user details if valid.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[token-extraction]]
- [[session-hijacking]]
