---
tags:
  - logs
  - monitoring
  - discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:00.326Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: e0bc15bc-8d1a-49b5-a93a-38aa0e0ffbef
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Monitor-Backend-Logs-for-Errors

## Summary

This procedure involves scanning backend application logs for database-related errors, such as PostgreSQL PG::SyntaxError exceptions, to identify potential SQL injection entry points in web applications like Ruby on Rails with GraphQL.

## Description

In a typical attack or vulnerability assessment scenario, monitoring logs reveals anomalies from user inputs causing SQL syntax failures. For the HackerOne GraphQL endpoint, this uncovered unsanitized parameters leading to injection in SET SESSION queries for schema switching between public and secure PostgreSQL schemas. Prerequisites include access to server logs (e.g., nginx access logs and Rails application logs). Expected outcomes include pinpointing error timestamps and correlating them to requests, enabling further investigation without direct exploitation.

## Requirements

1. Access to backend infrastructure logs (nginx and Rails)
2. Log analysis tools or grep/regex capabilities
3. Knowledge of application stack (Rails, PostgreSQL)

## Defense

Defensive measures and detection strategies:

- Implement centralized logging with SIEM tools like ELK Stack for real-time anomaly detection
- Use parameterized queries and input sanitization to prevent syntax errors from injections
- Monitor for error spikes correlating to traffic patterns

## Objectives

1. Detect indicators of SQL injection attempts through error logs
2. Correlate errors to specific endpoints and parameters
3. Establish baseline for normal vs. anomalous log behavior

## Instructions

### Step 1: Scan Logs for Syntax Errors

**Context**: Search for PostgreSQL-specific exceptions indicating malformed SQL from unescaped inputs.

**Command** (Manual Log Review):

No specific command; use tail or grep on log files:

```bash
grep "PG::SyntaxError" /path/to/rails.log
```

> This command filters Rails logs for syntax errors, revealing issues like those from embedded_submission_form_uuid on November 6th, 2018. Expected output: Log lines with error details and request context.

### Step 2: Correlate to Requests

**Context**: Match error timestamps to access logs for request origins.

**Command** (Log Correlation):

```bash
grep "2018-11-06" /path/to/nginx/access.log | grep "/graphql"
```

> Cross-reference timestamps to identify requests triggering errors. Expected output: HTTP requests to /graphql with potential malicious parameters.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- logs
- monitoring
- discovery
