---
tags:
  - api-call
  - curl
  - hackerone
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-api-read-reports]]'
  - '[[commands/curl-api-assign-report]]'
  - '[[commands/curl-api-fetch-program]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:32:29.214Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 331c45f5-a542-4581-8a04-45ed872ba9bc
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Perform-API-Operations-with-Curl

## Summary

This procedure executes API requests using curl to simulate token usage, including reading reports, assigning report states, and fetching program details, confirming backend functionality while highlighting UI monitoring issues.

## Description

Targeted at HackerOne's API endpoints, this involves authenticated GET, POST, and PUT requests via curl. The scenario assumes a valid token from prior setup. Outcomes include successful data retrieval and modifications, with notifications generated in the backend. This demonstrates active token use without UI timestamp updates.

## Requirements

1. Valid API token from HackerOne
2. curl installed on the local machine
3. Knowledge of target program handle and report IDs

## Defense

Defensive measures and detection strategies:

- Log all API requests at the backend level for activity tracking
- Implement rate limiting on API endpoints to detect abuse
- Cross-verify UI displays with server-side logs for discrepancies

## Objectives

1. Trigger backend API activity with the token
2. Generate notifications for actions performed
3. Validate token's operational capabilities

## Instructions

### Step 1: Read Reports

**Context**: Fetch a list of reports to test read access.

**Command** ([[commands/curl-api-read-reports]]):
```bash
curl -H "Authorization: Token token=YOUR_TOKEN" https://api.hackerone.com/v1/reports
```

> This command authenticates with the token and retrieves report data in JSON. Expect a 200 OK response with report objects.

### Step 2: Assign Report State

**Context**: Modify a report state to test write access.

**Command** ([[commands/curl-api-assign-report]]):
```bash
curl -X POST -H "Authorization: Token token=YOUR_TOKEN" -d '{"report_id":123,"state":"triage"}' https://api.hackerone.com/v1/reports/123/state_changes
```

> Submits a state change for report ID 123. Expect confirmation JSON.

### Step 3: Fetch Program Details

**Context**: Retrieve program information to test endpoint access.

**Command** ([[commands/curl-api-fetch-program]]):
```bash
curl -H "Authorization: Token token=YOUR_TOKEN" https://api.hackerone.com/v1/programs/PROGRAM_HANDLE
```

> Pulls details for the specified program. Expect JSON with program data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Windows Command Shell (adapted for API scripting)

### Sub-Techniques


## Commands Used

- [[commands/curl-api-read-reports]]
- [[commands/curl-api-assign-report]]
- [[commands/curl-api-fetch-program]]

## Tools Used

- [[tools/curl]]

## Tags

- api-call
- curl
