---
tags:
  - data-extraction
  - database
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/sqlmap-tamper-htmlencode]]'
platforms:
  - Web
  - Microsoft Dynamics AX
techniques:
  - '[[Network Sniffing]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: a9d4f02d-d795-4657-9346-1689915f1b11
created_at: '2025-12-11T06:10:30.790Z'
updated_at: '2025-12-11T06:10:30.790Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1040]]'
---
# Assess and Extract Database Contents

## Summary

This procedure assesses database structure and extracts sensitive data using known schemas.

## Description

Based on Microsoft Dynamics AX documentation, query main tables to extract accounting data.

## Requirements

1. Exploitable SQL injection
2. Knowledge of database schema
3. Tool like sqlmap for dumping

## Defense

Defensive measures and detection strategies:

- Database query logging
- Anomaly detection for large data extractions

## Objectives

1. Enumerate tables and columns
2. Extract sensitive entries
3. Assess impact

## Instructions

### Step 1: Research Schema

**Context**: Identify key tables from documentation.

Review Microsoft Dynamics AX docs for table names.

### Step 2: Dump Data

**Context**: Use sqlmap to extract entries.

Run sqlmap with dump options targeting identified tables.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Network Sniffing]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/sqlmap]]

## Tags

- [[data-extraction]]
- [[database]]
