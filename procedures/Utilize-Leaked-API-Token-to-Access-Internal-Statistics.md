---
tags:
  - unauthorized-access
  - data-exfiltration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[T1078.004]]'
  - '[[Data from Information Repositories]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 1acfd7e4-320d-49a2-ba6e-14090048d243
created_at: '2025-12-14T17:32:39.181Z'
updated_at: '2025-12-14T17:32:39.181Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[T1078.004]]'
  - '[[Data from Information Repositories]]'
---
# Utilize-Leaked-API-Token-to-Access-Internal-Statistics

## Summary

This procedure uses the extracted API token to query internal endpoints on api.semrush.com, gaining unauthorized access to system statistics without legitimate credentials.

## Description

With the leaked token, attackers can impersonate internal services to fetch sensitive data like usage stats or server metrics. In Semrush's case, the token grants direct API access. Prerequisites: valid token; outcomes: retrieval of restricted information, demonstrating full impact of the disclosure.

## Requirements

1. Extracted API token
2. HTTP client (browser, curl, Postman)
3. Knowledge of API endpoints from JS code

## Defense

Defensive measures and detection strategies:

- Rotate tokens immediately upon leak detection
- Implement rate limiting and anomaly detection on API usage
- Use short-lived tokens and monitor for unusual access patterns (e.g., external IPs)

## Objectives

1. Authenticate with leaked token
2. Query internal stats endpoints
3. Collect and analyze response data

## Instructions

### Step 1: Prepare API Request

**Context**: Mimic internal calls using the token.

Identify endpoints from JS (e.g., /v1/stats). Use curl or Postman to set Authorization header.

### Step 2: Execute Request

**Context**: Send request to verify access.

Example: curl -H "Authorization: Bearer [TOKEN]" https://api.semrush.com/internal/stats

> Replace [TOKEN] with extracted value. Expected: JSON with stats data if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[T1078.004]]
- [[Data from Information Repositories]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[unauthorized-access]]
- [[data-exfiltration]]
