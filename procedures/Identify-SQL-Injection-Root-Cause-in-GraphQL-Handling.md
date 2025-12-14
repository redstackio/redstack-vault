---
tags:
  - code-analysis
  - root-cause
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
updated_at: '2025-12-14T03:15:09.960Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 00c22abc-291c-4d80-98e6-0310495bf39f
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Identify-SQL-Injection-Root-Cause-in-GraphQL-Handling

## Summary

This procedure analyzes application code to determine the root cause of SQL injection, focusing on unsanitized GraphQL parameters interpolated into database queries.

## Description

The vulnerability arises from directly using the `embedded_submission_form_uuid` parameter in PostgreSQL SET SESSION statements for schema switching, without sanitization. This allows attackers to inject SQL commands, potentially switching schemas and extracting data from secure areas.

## Requirements

1. Source code access to Ruby on Rails application
2. Knowledge of GraphQL and PostgreSQL integration
3. Development environment for code review

## Defense

Defensive measures and detection strategies:

- Enforce input sanitization and parameterized queries
- Use schema-specific connection pooling instead of dynamic SET SESSION
- Conduct static code analysis for injection points

## Objectives

1. Locate the vulnerable code path
2. Understand the injection mechanism
3. Assess potential impact on database schemas

## Instructions

### Step 1: Review GraphQL Parameter Handling

**Context**: Examine how parameters are processed before database interaction.

No command; inspect the code building the `safe_query` for session parameters.

> Identify lack of sanitization in `embedded_submission_form_uuid` usage.

### Step 2: Trace to Database Layer

**Context**: Follow the flow to PostgreSQL SET SESSION execution.

No command; analyze the design decision to use raw parameters over sanitized fields.

> Confirm injection enables arbitrary SQL in the secure schema context.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- code-analysis
- root-cause
