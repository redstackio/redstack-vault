---
id: proc-004
tags:
  - api-bypass
  - updates-disclosure
  - hackerone
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-hackerone-api-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:47.290Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Retrieve-Unauthorized-Program-Updates-via-API

## Summary

This procedure extends the API bypass to fetch updates for an unauthorized HackerOne program, disclosing potentially sensitive change logs and announcements using a low-privilege key.

## Description

Similar to policy retrieval, the updates endpoint (e.g., https://api.hackerone.com/v1/hackers/programs/{program_handle}/updates) fails to enforce proper access controls. Query it with the low-perm API key to obtain a list of updates, which may contain confidential information about program changes, vulnerabilities, or policy adjustments.

## Requirements

1. Low-privilege API key
2. Unauthorized program handle
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Apply consistent authorization checks to all API endpoints
- Monitor API access patterns for cross-program queries
- Encrypt or redact sensitive fields in update responses

## Objectives

1. Access unauthorized update history
2. Gather insights into program evolution
3. Expose sensitive operational data

## Instructions

### Step 1: Identify Updates Endpoint

**Context**: Confirm the API path for updates.

Use /v1/hackers/programs/{handle}/updates for the query.

### Step 2: Execute Updates Query

**Context**: Retrieve the list of updates.

**Command** ([[commands/curl-hackerone-api-query]]):
```bash
curl "https://api.hackerone.com/v1/hackers/programs/askcmsakmdfksqa_h1b/updates" -X GET -u "██████=" -H 'Accept: application/json'
```

> This sends a GET request authenticated with the key, expecting a JSON array of updates. Successful output includes unauthorized entries with timestamps and content.

### Step 3: Review Retrieved Data

**Context**: Check for sensitive information.

Examine the response for details like policy changes or internal notes.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-hackerone-api-query]]

## Tools Used

- [[tools/curl]]

## Tags

- api-bypass
- updates-disclosure
- hackerone
