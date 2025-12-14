---
id: proc-uuid-2
tags:
  - sqli
  - stacked-queries
  - modx
type: procedure
tools:
  - '[[tools/Burp-Repeater]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/Attempt-Stacked-SQL-Injection-in-URL]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:47.404Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-SQL-Injection-with-Stacked-Queries

## Summary

This procedure confirms exploitable SQL injection by injecting a stacked query payload into the URL, attempting to append additional SQL commands to the 404 logging INSERT statement in MODx CMS.

## Description

Following the syntax error confirmation, this step tests for stacked queries by closing the original INSERT and adding a new command, such as a SELECT. The payload /Campin/qsdqsd',(commands here),1,1,1)# exploits the VALUES clause. Limitations include server timeouts and rate limiting, which may cause 503 errors. The target environment is MODx with MySQL, and success enables arbitrary SQL execution for data manipulation.

## Requirements

1. Confirmed SQLi from prior step
2. HTTP proxy tool like Burp Repeater
3. Awareness of server response times to avoid bans

## Defense

Defensive measures and detection strategies:

- Parameterize all SQL queries to prevent injection
- Enable query logging and alert on stacked or anomalous SQL patterns
- Implement input validation to reject suspicious URL characters (e.g., parentheses, commas)
- Use intrusion detection systems to flag repeated error page requests

## Objectives

1. Validate ability to execute additional SQL beyond error triggering
2. Assess potential for data exfiltration or modification
3. Identify exploitation limits like timeouts

## Instructions

### Step 1: Inject Stacked Payload

**Context**: Modify the URL to close the string and inject a simple stacked query, replacing '(commands here)' with a test like (SELECT 1).

**Command** ([[commands/Attempt-Stacked-SQL-Injection-in-URL]]):
```bash
curl -X GET "http://smarthistory.khanacademy.org/Campin/qsdqsd',(SELECT 1),1,1,1)#" -H "Host: smarthistory.khanacademy.org" --connect-timeout 30
```

> The # comments out the rest of the query. Expected output is either successful execution (no error) or a modified error indicating injection, though testing may hit 503 due to slow responses.

### Step 2: Evaluate Response and Iterate

**Context**: If timeout occurs, reduce payload complexity or use slower request intervals.

**Command** (Manual adjustment):
```bash
# Repeat with simpler payload if needed, e.g., remove SELECT
```

> Success if response differs from syntax error, suggesting stacked execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/Attempt-Stacked-SQL-Injection-in-URL]]

## Tools Used

- [[tools/Burp-Repeater]]

## Tags

- [[sqli]]
- [[stacked]]
