---
tags:
  - information-disclosure
  - pii-leak
  - json-endpoint
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-model-json-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:28.760Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 0354b725-a105-49dc-9e9c-5ee6d9a734f8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
---

# Access-Model-JSON-Endpoint-for-Additional-Leak

## Summary

This procedure accesses the unrestricted /?tpl=index2&model=json endpoint on xvcams.com to obtain supplementary model data in JSON format, potentially overlapping with PII from other APIs and exacerbating privacy violations through aggregated leakage.

## Description

By appending JSON-specific parameters like tpl=index2, model=json, and a timestamp (_) to the root URL, the endpoint serves raw model information without authentication or filtering. This indicates a broader misconfiguration in the site's PHP-based backend, allowing passive collection of data that could include names, IDs, or statuses. Ideal for chaining with other endpoints to build complete profiles; requires minimal setup beyond HTTP requests.

## Requirements

1. HTTPS access to xvcams.com
2. Basic HTTP GET capability
3. JSON handling for output analysis

## Defense

Defensive measures and detection strategies:

- Restrict JSON endpoints to authenticated sessions only
- Implement parameter validation to block tpl=model=json patterns
- Audit and remove legacy endpoints exposing internal data
- Use content security policies to prevent unauthorized JSON fetching

## Objectives

1. Gather additional model metadata
2. Correlate with PII from primary APIs
3. Assess systemic exposure in the application

## Instructions

### Step 1: Direct Access to JSON Endpoint

**Context**: Fetch the JSON model data using timestamped parameters to mimic legitimate requests.

**Command** ([[commands/curl-access-model-json-endpoint]]):
```bash
curl "https://www.xvcams.com/?tpl=index2&model=json&_=$(date +%s)" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

> Returns JSON with model details; inspect for sensitive fields like IDs or statuses confirming lack of controls.

### Step 2: Validate and Parse Response

**Context**: Confirm the data's utility by parsing for key elements.

**Command** ([[commands/curl-access-model-json-endpoint]]):
```bash
curl "https://www.xvcams.com/?tpl=index2&model=json&_=$(date +%s)" -H "User-Agent: Mozilla/5.0" | jq '.'
```

> Use jq to format; expected: Structured model objects. Cross-reference with other endpoint outputs for overlaps.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-model-json-endpoint]]

## Tools Used

- [[tools/Web-Browser]]

## Tags

- information-disclosure
- pii-leak
- json-endpoint

