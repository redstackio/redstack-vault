---
tags:
  - log-analysis
  - discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - PostgreSQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T03:15:09.963Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 812d290a-0fb6-49d7-af36-f6b196392bab
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Discover-SQL-Syntax-Error-in-Backend-Logs

## Summary

This procedure involves monitoring backend logs to identify PostgreSQL syntax errors that indicate potential SQL injection vulnerabilities in web applications.

## Description

In a Ruby on Rails environment with GraphQL and PostgreSQL, backend logs can reveal PG::SyntaxError exceptions triggered by unsanitized inputs. This step was key in discovering the vulnerability on November 6th, 2018, by observing errors related to the `embedded_submission_form_uuid` parameter during schema switching.

## Requirements

1. Access to backend server logs (Rails and PostgreSQL)
2. Log monitoring tools or grep for pattern matching
3. Internal network access to the application server

## Defense

Defensive measures and detection strategies:

- Implement centralized logging with anomaly detection for SQL errors
- Use web application firewalls (WAF) to block suspicious queries
- Regularly audit logs for syntax exceptions

## Objectives

1. Identify indicators of SQL injection attempts
2. Pinpoint affected endpoints and parameters
3. Initiate vulnerability investigation

## Instructions

### Step 1: Monitor Backend Logs

**Context**: Scan logs for PostgreSQL exceptions to detect syntax issues from user inputs.

No specific command; manually review or use log aggregation tools to filter for "PG::SyntaxError".

> Look for entries timestamped around user interactions with the /graphql endpoint.

### Step 2: Analyze Exception Details

**Context**: Examine the error context to link it to GraphQL parameters.

No command; parse the stack trace to identify the interpolation point in SET SESSION statements.

> Confirm the error stems from unsanitized `embedded_submission_form_uuid`.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- log-analysis
- discovery
