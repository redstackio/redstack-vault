---
id: proc-identify-sqli-endpoint-zomato
tags:
  - sqli
  - recon
  - web
type: procedure
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-boolean-sqli-test]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:26.305Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable Endpoint for SQLi

## Summary

This procedure identifies the vulnerable endpoint and parameter in Zomato's application where the 'brids' JSON array can be manipulated for SQL injection, setting the stage for blind exploitation.

## Description

In the context of Zomato's web application, the endpoint /█████.php?res_id={RES_ID} processes POST requests with action=show_support_breakups and a brids JSON array. Insufficient sanitization allows SQL payloads to be injected via string concatenation in backend queries, leading to boolean-based blind SQLi. This step focuses on confirming endpoint accessibility without triggering alerts.

## Requirements

1. Valid restaurant ID ({RES_ID}) from Zomato
2. Active PHPSESSID cookie for session
3. Network access to www.zomato.com
4. Curl or similar HTTP client

## Defense

Defensive measures and detection strategies:

- Implement prepared statements or parameterized queries for JSON inputs
- Use web application firewalls (WAF) to detect SQL keywords like OR, MID, LIKE in payloads
- Log and monitor anomalous HTTP status codes (e.g., frequent 500s)

## Objectives

1. Confirm endpoint responds to legitimate requests
2. Verify brids parameter accepts JSON arrays
3. Establish baseline for payload testing

## Instructions

### Step 1: Send Baseline Request

**Context**: Test the endpoint with a non-malicious payload to ensure accessibility.

**Command** ([[commands/curl-boolean-sqli-test]]):
```bash
curl -X POST "https://www.zomato.com/█████.php?res_id={RES_ID}" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data "action=show_support_breakups&brids=[\"test\"]"
```

> This sends a simple JSON array in brids. Expected output: 200 OK with normal response body.

### Step 2: Validate Parameter Processing

**Context**: Ensure the backend processes the JSON without errors.

**Command** ([[commands/curl-boolean-sqli-test]]):
```bash
curl -X POST "https://www.zomato.com/█████.php?res_id={RES_ID}" \
  -H "Cookie: PHPSESSID={SESSION_COOKIE};" \
  --data "action=show_support_breakups&brids=[\"1\",\"2\"]"
```

> Expected output: Successful processing, confirming JSON array handling.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-boolean-sqli-test]]

## Tools Used


## Tags

- [[sqli]]
- [[recon]]
