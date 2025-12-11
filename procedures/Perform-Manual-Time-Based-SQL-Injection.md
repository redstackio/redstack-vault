---
tags:
  - sql-injection
  - blind
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/sqlmap-tamper-htmlencode]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 74a489f8-098d-471b-bd0c-4e6f266b37c8
created_at: '2025-12-11T06:10:30.800Z'
updated_at: '2025-12-11T06:10:30.800Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1190]]'
---
# Perform Manual Time-Based SQL Injection

## Summary

This procedure manually tests blind SQL injection using time-delay payloads.

## Description

Time-based injections confirm vulnerabilities when error messages are suppressed by observing response delays.

## Requirements

1. Confirmed injectable parameter
2. Ability to measure response times
3. Payload crafting knowledge

## Defense

Defensive measures and detection strategies:

- Rate limiting on endpoints
- WAF rules for SQL patterns

## Objectives

1. Induce observable delays
2. Validate blind injection
3. Prepare for automation

## Instructions

### Step 1: Craft Delay Payload

**Context**: Inject delay functions like WAITFOR.

Use payload: ' WAITFOR DELAY '00:00:10'--

### Step 2: Measure Response

**Context**: Time the server response.

Upload and confirm delay occurs.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[sql-injection]]
- [[blind]]
