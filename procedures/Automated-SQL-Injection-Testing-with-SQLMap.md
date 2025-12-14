---
id: 6b00f846-7a8d-42ea-bbac-6f4ad46016e2
name: Automated-SQL-Injection-Testing-with-SQLMap
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:09.863Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - sqli
  - testing
  - automation
commands:
  - '[[commands/sqlmap-boolean-blind-test]]'
platforms:
  - Web
tools:
  - '[[tools/sqlmap]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Automated-SQL-Injection-Testing-with-SQLMap

## Summary

This procedure uses SQLMap to perform automated testing for SQL injection vulnerabilities in a web application, focusing on high-risk payloads and all injection points including HTTP headers, to detect boolean-based blind SQLi in the User-Agent header.

## Description

In a scenario targeting a Microsoft SharePoint application with a MySQL backend, this procedure scans the target URL for injection points by simulating requests with randomized User-Agents and aggressive payloads. It identifies vulnerabilities through response analysis without requiring direct error feedback, suitable for blind exploitation. Prerequisites include network access to the target and SQLMap installed on a Linux or Windows system.

## Requirements

1. Network access to the target HTTPS endpoint (e.g., https://target.mil/)
2. SQLMap tool installed and configured
3. Basic understanding of HTTP requests and headers

## Defense

Defensive measures and detection strategies:

- Implement parameterized queries and input sanitization for all headers, including User-Agent
- Use web application firewalls (WAF) to detect anomalous SQL payloads in headers
- Monitor for unusual response times or patterns indicative of blind SQLi attempts

## Objectives

1. Detect SQL injection points in the application
2. Identify boolean-based blind vulnerabilities
3. Gather initial evidence for further exploitation

## Instructions

### Step 1: Launch SQLMap Scan

**Context**: Initiate the automated scan with high risk and level to thoroughly test headers like User-Agent.

**Command** ([[commands/sqlmap-boolean-blind-test]]):
```bash
sqlmap --url https://target.mil/ --random-agent -risk 3 --level 5 --batch
```

> This command targets the specified URL, randomizes the User-Agent to avoid detection, sets the highest risk (3) for aggressive payloads, level 5 to test all vectors including headers, and runs in batch mode for automation. Expected output includes detection logs showing injectable parameters and vulnerability type.

### Step 2: Review Scan Results

**Context**: Analyze SQLMap output for confirmed injection points.

No specific command; parse the console output or logs for mentions of User-Agent as injectable.

> Look for indicators like 'parameter: User-Agent (POST/GET/headers)' and 'type: boolean-based blind'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqlmap-boolean-blind-test]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- [[sqli]]
- [[testing]]
- [[automation]]
