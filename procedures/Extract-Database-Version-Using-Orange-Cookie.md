---
tags:
  - sqli
  - time-based
  - exfiltration
  - mysql
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.840Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 4ae9fe08-0c1f-48ac-bcb2-1a7dfd533cd6
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract Database Version Using Orange Cookie

## Summary

This procedure uses conditional SLEEP payloads in the 'orange' cookie to infer the MySQL database version character-by-character via response timing on Zomato's login page, enabling reconnaissance for further exploitation.

## Description

Building on confirmed time-based SQLi, this employs binary search with IF statements and MID(VERSION(),pos,len) to test each character. For example, payloads check if the first character is '5' by sleeping on match. Delays confirm true conditions, allowing reconstruction of the version string (e.g., 5.7.XX). This is a data exfiltration technique in blind scenarios, targeting cookie-processed queries. Prerequisites: working time-based injection; outcomes: full version disclosure.

## Requirements

1. Script or manual iteration for binary search (e.g., test ASCII ranges)
2. Consistent baseline timing to distinguish delays
3. Understanding of MySQL VERSION() function

## Defense

Defensive measures and detection strategies:

- Disable or restrict VERSION() exposure in queries
- Implement query whitelisting to block SLEEP/IF in user inputs
- Alert on repeated delayed responses from same IP

## Objectives

1. Probe database metadata
2. Reconstruct version via timing oracle
3. Identify DBMS for tailored attacks

## Instructions

### Step 1: Test First Character

**Context**: Use conditional payload to check position 1.

Inject '1'=IF(MID(VERSION(),1,1)=1,SLEEP(10),0)='1' into 'orange' and time response.

**Expected Output**: Delay if char is '1', no delay otherwise.

### Step 2: Iterate for Full Version

**Context**: Binary search subsequent positions (e.g., pos=2, chars 0-9,a-z).

Use '1'=IF(MID(VERSION(),1,1)=5,SLEEP(10),0)='1' and adjust until full string inferred.

**Expected Output**: Delays mapping to version like '5.7.32'.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- sqli
- time-based
- exfiltration
- mysql
