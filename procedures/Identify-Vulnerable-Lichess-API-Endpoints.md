---
id: proc-lichess-identify-001
tags:
  - endpoint-enumeration
  - ssrf
  - api
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-endpoint-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:46:14.708Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Vulnerable-Lichess-API-Endpoints

## Summary

This procedure enumerates public Lichess API endpoints that accept the 'players' parameter, confirming they are unauthenticated and vulnerable to SSRF exploitation.

## Description

Lichess exposes several game export endpoints that process the 'players' query parameter without authentication. By testing these, attackers can identify vectors for SSRF, such as forcing requests to internal networks or cloud metadata services. This step builds on code review to validate live endpoints.

## Requirements

1. Public access to lichess.org
2. Tool for HTTP requests (e.g., curl)
3. Knowledge of Lichess game IDs (obtainable via browsing)

## Defense

Defensive measures and detection strategies:

- Rate-limit public API endpoints to prevent abuse
- Log and monitor anomalous query parameters like 'players'
- Implement WAF rules to block suspicious URL patterns in queries

## Objectives

1. List exploitable endpoints
2. Verify parameter acceptance
3. Assess authentication requirements

## Instructions

### Step 1: Test Game Export Endpoint

**Context**: Check /game/export/[GAME_ID] for 'players' support.

**Command** ([[commands/curl-endpoint-test]]):
```bash
curl "https://lichess.org/game/export/[GAME_ID]?players=test" -v
```

> Replace [GAME_ID] with a valid ID (e.g., from lichess.org/export/game). Expected output: 200 OK with game data, confirming parameter processing.

### Step 2: Test Bulk Export Endpoints

**Context**: Validate /api/games/export/_ids and /api/games/user/[USERNAME].

**Command** ([[commands/curl-endpoint-test]]):
```bash
curl "https://lichess.org/api/games/export/_ids?players=test" -v
curl "https://lichess.org/api/games/user/[USERNAME]?players=test" -v
```

> Use a real username. Expected output: Responses without auth errors.

### Step 3: Document Endpoints

**Context**: Compile list for exploitation.

Note all endpoints that accept and process 'players' without validation.

**Expected Output**: Endpoint inventory.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-endpoint-test]]

## Tools Used


## Tags

- endpoint-enumeration
- api
- ssrf
