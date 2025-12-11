---
tags:
  - sql-injection
  - automation
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
  - '[[Network Sniffing]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 8f987548-3e1a-476a-a846-8505a82c6339
created_at: '2025-12-11T06:10:30.794Z'
updated_at: '2025-12-11T06:10:30.794Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1040]]'
---
# Automate SQL Injection with sqlmap

## Summary

This procedure automates SQL injection exploitation using sqlmap with tampering for XML compatibility.

## Description

sqlmap is used to detect and exploit the vulnerability, extracting database details like version and structure.

## Requirements

1. Installed sqlmap
2. Target URL and injectable parameter
3. Knowledge of XML encoding

## Defense

Defensive measures and detection strategies:

- Input validation and sanitization
- Intrusion detection for sqlmap user-agents

## Objectives

1. Confirm vulnerability automatically
2. Extract database metadata
3. Prepare for data dumping

## Instructions

### Step 1: Run sqlmap with Tamper

**Context**: Automate injection with HTML encoding.

Execute [[commands/sqlmap-tamper-htmlencode]]:

```bash
sqlmap --tamper htmlencode
```

> This handles XML entity encoding for payloads.

### Step 2: Extract Version

**Context**: Query database version.

Use sqlmap options to dump version information.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Network Sniffing]]

### Sub-Techniques



## Commands Used

- [[commands/sqlmap-tamper-htmlencode]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- [[sql-injection]]
- [[automation]]
