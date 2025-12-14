---
tags:
  - idor
  - data-leak
  - api-exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/zomato-leak-restaurant-data-post]]'
platforms:
  - Mobile API
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: a1a7ab43-818f-488e-863c-30639811343e
created_at: '2025-12-14T17:25:29.757Z'
updated_at: '2025-12-14T17:25:29.757Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Leak Restaurant Data via API Request

## Summary

This procedure sends an initial POST request to Zomato's API using an arbitrary res_id to leak restaurant data, demonstrating the absence of ownership checks in the endpoint.

## Description

The API endpoint /XX/XXXXX?res_id=XXXXX accepts arbitrary res_id without validation, returning sensitive data. This step confirms IDOR and gathers info for further chaining. Requires authenticated token and cookies.

## Requirements

1. Valid access_token and session cookies
2. cURL or equivalent for HTTP requests
3. Known res_id (arbitrary)

## Defense

Defensive measures and detection strategies:

- Implement server-side ownership verification (e.g., check user owns res_id)
- Log and alert on mismatched res_id/user_id pairs
- Use API gateways with input validation

## Objectives

1. Confirm arbitrary res_id access
2. Leak restaurant details for menu retrieval
3. Validate no auth restrictions

## Instructions

### Step 1: Craft and Send POST Request

**Context**: Use arbitrary res_id to probe the endpoint.

**Command** ([[commands/zomato-leak-restaurant-data-post]]):
```bash
curl -X POST "https://api.zomato.com/XX/XXXXX?res_id=XXXXX" \
  -H "Host: api.zomato.com" \
  -H "X-Device-Is-Rooted: 0" \
  -H "Cookie: <COOKIES>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "access_token=<your token>&client_id=zomato_ios_v2"
```

> Sends request with token; expected output: JSON with restaurant data.

### Step 2: Analyze Response

**Context**: Check for leaked info.

> Parse response for details like menu hints.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/zomato-leak-restaurant-data-post]]

## Tools Used


## Tags

- [[idor]]
- [[data-leak]]
