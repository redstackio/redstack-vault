---
tags:
  - code-review
  - sqli
  - graphql
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
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:26:00.322Z'
skill_level: advanced
impact_level: medium
detection_risk: low
sub_techniques: []
id: 4534e5d7-9fbc-4741-b95e-5e3a90c4719a
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Analyze-Code-for-SQL-Injection-Root-Cause

## Summary

This procedure details static code analysis to identify SQL injection vulnerabilities, focusing on GraphQL parameter handling in Ruby on Rails applications where inputs are directly interpolated into PostgreSQL queries without sanitization.

## Description

In the HackerOne case, analysis revealed that the embedded_submission_form_uuid parameter was unsafely used in SET SESSION queries (e.g., SET SESSION #{key} TO #{value}), allowing injection to switch schemas and execute arbitrary SQL. This was introduced in commit a6f976743368c29f8b4c0590079808e5583d4fb6 on September 3rd, 2018. The procedure assumes access to source code and requires understanding of Rails, GraphQL, and PostgreSQL. Outcomes include vulnerability confirmation and remediation recommendations like using ActiveRecord sanitization.

## Requirements

1. Source code access (e.g., Git repository)
2. Knowledge of Ruby on Rails and SQL
3. Development environment for testing code snippets

## Defense

Defensive measures and detection strategies:

- Enforce code reviews with static analysis tools like Brakeman or Snyk for SQLi patterns
- Use prepared statements and bind variables in all database interactions
- Implement web application firewalls (WAF) to block injection payloads

## Objectives

1. Identify unsanitized inputs in database queries
2. Trace vulnerability origin to specific code changes
3. Assess scope of impact on database schemas

## Instructions

### Step 1: Review GraphQL Resolver Code

**Context**: Examine how parameters are passed to database sessions.

**Command** (Git Log Search):

```bash
git log --grep="embedded_submission_form_uuid" --since="2018-09-01"
```

> Searches commit history for parameter mentions post-vulnerability introduction. Expected output: Commit a6f97674 showing unsafe interpolation.

### Step 2: Inspect Query Construction

**Context**: Look for direct string interpolation in SQL.

**Command** (Grep Codebase):

```bash
grep -r "SET SESSION" app/ | grep "embedded_submission_form_uuid"
```

> Finds lines with vulnerable query patterns. Expected output: Code snippets like execute("SET SESSION #{key} TO '#{value}'") without escaping.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- code-review
- sqli
- graphql
