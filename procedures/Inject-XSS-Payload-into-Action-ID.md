---
tags:
  - xss
  - javascript
  - web
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-quora-xss-exploit]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:44.604Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 741c4e35-1ce6-4c71-9434-46293e52bf2a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Action-ID

## Summary

This procedure injects a JavaScript payload into the __e2e_action_id parameter of a Quora request, exploiting unescaped reflection in JSONP responses to execute arbitrary code on the victim's browser.

## Description

The __e2e_action_id is reflected without escaping in the JSONP callback as an argument to require('actions').finishAction(id, ...), allowing string breakout with payloads like ',alert(1),' to inject JS. Combined with channel targeting, this delivers XSS via victim's update polls. A similar issue exists with _lm_transaction_id in mutationDoneAfterVersion(). Prerequisites: Modified request; outcomes: Payload queued for execution, enabling session theft.

## Requirements

1. Modified channel-targeted request
2. Knowledge of reflection context (finishAction string)
3. Victim's active session for polling

## Defense

Defensive measures and detection strategies:

- Escape all reflected parameters in JSONP/JS responses
- Validate __e2e_action_id as alphanumeric only
- Content Security Policy to block inline JS execution

## Objectives

1. Break out of JSON string context
2. Inject and execute arbitrary JS
3. Achieve RCE in victim's browser

## Instructions

### Step 1: Craft Payload

**Context**: Set __e2e_action_id to escape and inject alert(1).

**Command** ([[commands/curl-quora-xss-exploit]]):
```bash
# In --data: change &__e2e_action_id=esl2xq4xyj& to &__e2e_action_id=',alert(1),'&
curl 'https://www.quora.com/webnode2/server_call_POST?_v=2rtUq6Z4HO9gWK&_m=edit' ... --data '...&__e2e_action_id=",alert(1),"&...'
```

> Expected output: Payload set; reflected as finishAction('',alert(1),'') in JSONP.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

-

## Commands Used

- [[commands/curl-quora-xss-exploit]]

## Tools Used

- [[tools/curl]]

## Tags

- xss
- javascript
