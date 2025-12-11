---
tags:
  - account-takeover
type: procedure
tools:
  - '[[tools/Google-Tag-Manager]]'
  - '[[tools/Chrome-Browser]]'
  - '[[tools/PHP]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/postmessage-oauthdone]]'
  - '[[commands/fetch-logged-tokens]]'
  - '[[commands/php-log-querystring]]'
  - '[[commands/php-parse-logs]]'
  - '[[commands/history-pushstate-monitor]]'
  - '[[commands/top-postmessage-relay]]'
  - '[[commands/parent-onmessage-listener]]'
  - '[[commands/setinterval-monitor]]'
  - '[[commands/sanitize-oauth-params]]'
platforms:
  - Web
techniques:
  - '[[Use Alternate Authentication Material]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: d8214e0a-11b5-42ff-a8de-3a0faf3ef3a0
created_at: '2025-12-11T06:10:22.342Z'
updated_at: '2025-12-11T06:10:22.342Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1550]]'
---
# Hijack Account with Stolen Tokens

## Summary

This procedure uses the stolen OAuth code, id_token, and state to complete sign-in as the victim on Reddit.

## Description

From the attacker's Apple sign-in popup, post the stolen payload via postMessage to hijack the session and gain full account access.

## Requirements

1. Stolen tokens from prior step.
2. Open Apple sign-in popup in browser.
3. Console access for execution.

## Defense

Defensive measures and detection strategies:

- Validate OAuth states and tokens strictly.
- Monitor for anomalous sign-in attempts.

## Objectives

1. Inject stolen tokens into sign-in flow.
2. Achieve full account takeover.
3. Verify access to victim's account.

## Instructions

### Step 1: Inject Stolen Payload

**Context**: Post message from popup to opener window.

Execute [[commands/postmessage-oauthdone]] in console:

```javascript
opener.postMessage('{method:"oauthDone",data:{authorization:{code:code,id_token:id_token,state:state}}}',"*");
```

### Step 2: Verify Hijack

**Context**: Confirm successful sign-in as victim.

Check Reddit session for victim's account access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques

## Commands Used

- [[commands/postmessage-oauthdone]]

## Tools Used

- [[tools/Chrome-Browser]]

## Tags

- [[account-takeover]]
