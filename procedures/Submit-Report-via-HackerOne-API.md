---
tags:
  - auth-bypass
  - api
  - curl
  - hackerone
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-hackerone-report-submission]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:48.311Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7077d978-48e9-4c43-b4bb-f4b4ec9d1e46
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Report-via-HackerOne-API

## Summary

This procedure uses a sandbox-generated API key to submit a vulnerability report via the HackerOne REST API, bypassing UI-enforced bans on the account.

## Description

The root cause is that API authentication via keys does not check for user-level bans applied through UI/GraphQL. Use curl to POST to /v1/hackers/reports with JSON payload including team_handle, title, vulnerability details, etc. This allows banned users to spam reports to any program, undermining ban effectiveness. Target: api.hackerone.com over HTTPS.

## Requirements

1. API key from sandbox program
2. curl installed
3. Knowledge of target team_handle

## Defense

Defensive measures and detection strategies:

- Synchronize ban status across API and UI
- Rate-limit API submissions per user/key
- Validate API keys against ban lists

## Objectives

1. Bypass ban to submit report
2. Target specific programs
3. Expected outcome: Report created via API

## Instructions

### Step 1: Prepare API Request

**Context**: Reference HackerOne API docs for endpoint and payload structure.

**Command** ([[commands/curl-hackerone-report-submission]]):
```bash
curl "https://api.hackerone.com/v1/hackers/reports" -X POST -u "testhackerone-creative:pYnONekvxUTvHbKF7Jp64qh9STIhhdXvKmefWOeR8YU=" -H 'Content-Type: application/json' -H 'Accept: application/json' -d @- <<EOD { "data": { "type": "report", "attributes": { "team_handle": "HackerOne-test_h1b", "title": "string", "vulnerability_information": "test tst tst", "impact": "tst tst", "severity_rating": "none", "weakness_id": 1 } } } EOD
```

> This authenticates with -u (username:api_key), sets JSON headers, and sends payload. Expected output: 201 Created with report data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-hackerone-report-submission]]

## Tools Used

- [[tools/curl]]

## Tags

- auth-bypass
- api
- curl
- hackerone
