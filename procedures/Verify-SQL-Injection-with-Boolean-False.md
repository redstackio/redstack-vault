---
tags:
  - sqli
  - boolean-based
  - verification
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-boolean-false-sqli]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 23ff0c84-75a1-47a1-bff2-6428e5d2bbd7
created_at: '2025-12-14T03:46:20.267Z'
updated_at: '2025-12-14T03:46:20.267Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-SQL-Injection-with-Boolean-False

## Summary

This procedure verifies SQL injection control by injecting a false boolean condition (AND '1'=='0') to restrict query results, ensuring the attacker can precisely manipulate the database output.

## Description

In the Khan Academy endpoint, this payload limits results to only English CSVs, confirming the injection alters the query logic without broader exposure. It builds on prior exploitation to validate the attack's reliability for targeted data extraction.

## Requirements

1. Successful tautology exploitation
2. Understanding of SQL boolean logic
3. HTTP request tool

## Defense

Defensive measures and detection strategies:

- Employ input whitelisting for parameters
- Use ORM frameworks like Django's to auto-parameterize
- Alert on query anomalies like false conditions in logs

## Objectives

1. Confirm query manipulation precision
2. Limit results to verify control
3. Assess potential for conditional data access

## Instructions

### Step 1: Inject False Condition

**Context**: Append AND '1'=='0 to the language parameter to make the condition false except for matching records.

**Command** ([[commands/curl-boolean-false-sqli]]):
```bash
curl -s "https://www.khanacademy.org/translations/videos/en'%20AND'1'=='0_youtube_stats.csv"
```

> Expect only English CSV data, proving the injection's influence on results.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-boolean-false-sqli]]

## Tools Used


## Tags

- [[sqli]]
- [[boolean-based]]
- [[verification]]
