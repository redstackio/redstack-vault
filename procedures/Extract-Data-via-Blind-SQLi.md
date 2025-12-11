---
tags:
  - data-exfiltration
  - blind-sqli
type: procedure
tools:
  - '[[tools/Akamai-WAF]]'
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: ae8a213e-eb43-489f-a737-6bf151ba6dae
created_at: '2025-12-11T03:48:05.942Z'
updated_at: '2025-12-11T03:48:05.942Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1190]]'
---
# Extract Data via Blind SQLi

## Summary

This procedure uses blind SQL injection techniques to extract data from a database when direct output is not visible, applied after bypassing protections like Akamai WAF.

## Description

In a web environment with SQL backend, blind SQLi relies on boolean or time-based responses to infer data. This is used to read sensitive information from a single database, as in the Valve report.

## Requirements

1. Confirmed blind SQLi vulnerability
2. Tool like sqlmap for automation
3. Patience for time-based extractions

## Defense

Defensive measures and detection strategies:

- Parameterize all SQL queries
- Rate-limit requests to detect enumeration attempts

## Objectives

1. Dump database structure and content
2. Exfiltrate specific data
3. Achieve critical impact

## Instructions

### Step 1: Automate with sqlmap

**Context**: Use sqlmap for efficient data dumping.

**Command** ([[commands/sqlmap-blind-exploit]]):

```bash
sqlmap -u "https://target.com/report_xml.php?countryFilter[]=1" --batch --dump
```

> This automates boolean/time-based queries to extract data.

### Step 2: Manual Time-Based Extraction

**Context**: Manually query data bits using delays.

**Command** ([[commands/curl-inject-sqli-payload]]):

```bash
curl "https://target.com/report_xml.php?countryFilter[]=1' AND IF(1=1, SLEEP(5), 0) --"
```

> Measure response time to infer true/false.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/sqlmap-blind-exploit]]
- [[commands/curl-inject-sqli-payload]]

## Tools Used

- [[commands/sqlmap-blind-exploit]]
- [[commands/curl-inject-sqli-payload]]

## Tags

- #data-exfiltration
- [[commands/curl-inject-sqli-payload]]
