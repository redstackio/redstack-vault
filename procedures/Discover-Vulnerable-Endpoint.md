---
tags:
  - sql-injection
  - vulnerability-discovery
type: procedure
tools:
  - '[[tools/Akamai-WAF]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 4e2fa313-ab58-4ec5-9bbe-c8253f4bfee3
created_at: '2025-12-11T03:48:05.944Z'
updated_at: '2025-12-11T03:48:05.944Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Discover Vulnerable Endpoint

## Summary

This procedure involves identifying potentially vulnerable parameters in a web endpoint, such as countryFilter[] in report_xml.php, by sending test requests to detect SQL injection points.

## Description

In this attack scenario, the target is a PHP-based web application protected by Akamai WAF with a SQL database backend. The procedure tests for unvalidated parameters that allow SQL payload injection, leading to blind SQLi exploitation. Expected outcomes include error responses or behavioral changes indicating vulnerability.

## Requirements

1. Access to the target URL (e.g., https://target.com/report_xml.php)
2. HTTP client tool like curl
3. Basic knowledge of SQL syntax

## Defense

Defensive measures and detection strategies:

- Implement input validation and prepared statements in PHP
- Monitor WAF logs for suspicious parameter values

## Objectives

1. Confirm injectable parameter
2. Observe response differences
3. Prepare for further exploitation

## Instructions

### Step 1: Send Baseline Request

**Context**: Establish normal endpoint behavior.

**Command** ([[commands/curl-inject-sqli-payload]]):

```bash
curl "https://target.com/report_xml.php?countryFilter[]=normal_value"
```

> This retrieves the standard response for comparison.

### Step 2: Test for Injection

**Context**: Introduce potential SQL-breaking characters to detect errors.

**Command** ([[commands/curl-inject-sqli-payload]]):

```bash
curl "https://target.com/report_xml.php?countryFilter[]='"
```

> Look for SQL error messages or unexpected behavior in the response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-inject-sqli-payload]]
- [[commands/curl-inject-sqli-payload]]

## Tools Used

- [[commands/curl-inject-sqli-payload]]

## Tags

- #sql-injection
- #vulnerability-discovery
