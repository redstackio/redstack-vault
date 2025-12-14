---
tags:
  - idor
  - menu-retrieval
  - api-exploit
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/zomato-get-special-menus-post]]'
platforms:
  - Mobile API
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: efdbc4de-d309-472d-80e4-1a87fcc8f475
created_at: '2025-12-14T17:25:29.754Z'
updated_at: '2025-12-14T17:25:29.754Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Retrieve Special Menu IDs

## Summary

This procedure chains from data leakage to send a POST request retrieving special menus for an arbitrary restaurant, extracting menu_set_id for deactivation.

## Description

Using the res_id from prior steps, POST to XXX/XXXXX.php with type=SPECIAL fetches menu details without ownership checks, leaking menu_set_id. This prepares the final exploit.

## Requirements

1. res_id and user_id from reconnaissance
2. Authenticated session
3. HTTP client for POST

## Defense

Defensive measures and detection strategies:

- Validate requester ownership before menu queries
- Rate-limit menu retrieval endpoints
- Audit logs for unauthorized menu access attempts

## Objectives

1. Fetch special menus using arbitrary res_id
2. Extract menu_set_id
3. Confirm IDOR in menu endpoint

## Instructions

### Step 1: Send Retrieval Request

**Context**: Use obtained IDs to get menus.

**Command** ([[commands/zomato-get-special-menus-post]]):
```bash
curl -X POST "https://api.zomato.com/XXX/XXXXX.php" \
  -d "user_id=XXXX&type=SPECIAL&request_type=get-special-menus&res_id=XXXXX"
```

> Expected output: Menu list with menu_set_id=XXXX.

### Step 2: Parse for IDs

**Context**: Identify target menu_set_id.

> Look for active menus in response.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/zomato-get-special-menus-post]]

## Tools Used


## Tags

- [[idor]]
- [[menu-retrieval]]
