---
id: proc-query-json-activity-id
tags:
  - api-disclosure
  - json
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/get-reports-json]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.572Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Query-JSON-Endpoint-for-Latest-Activity-ID

## Summary

This procedure uses the HackerOne JSON API endpoint to retrieve the latest_activity_id from a report, disclosing internal team activity details to unauthorized participants.

## Description

Exploiting lack of access controls, an unauthorized participant queries the public-facing /reports/<report-id>.json endpoint. This leaks the latest_activity_id, which correlates to private comments and assignments. The attack targets HackerOne's JSON API, requiring participant authentication via cookies. Outcomes include exposure of internal IDs for potential correlation attacks.

## Requirements

1. Attacker's session cookie from HackerOne login
2. Target report ID
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Implement participant-specific access controls on JSON responses
- Null sensitive fields like latest_activity_id for non-team users
- Monitor API queries for unusual participant access patterns

## Objectives

1. Retrieve internal activity ID
2. Confirm disclosure vulnerability
3. Gather data for further analysis

## Instructions

### Step 1: Prepare Authentication

**Context**: Ensure the request uses the attacker's session to simulate participant access.

Obtain the session cookie by logging in as attacker and extracting from browser dev tools.

> Cookie format: _hackerone_session=abc123...

### Step 2: Execute JSON Query

**Context**: Send GET request to fetch report details including the leaked field.

**Command** ([[commands/get-reports-json]]):
```bash
curl -H "Cookie: <attacker-cookie>" "https://hackerone.com/reports/<report-id>.json"
```

> The response JSON includes "latest_activity_id": "internal-id-value", exposing team actions.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/get-reports-json]]

## Tools Used


## Tags

- api-disclosure
- json
- hackerone
