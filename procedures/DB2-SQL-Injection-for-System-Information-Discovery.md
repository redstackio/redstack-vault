---
type: procedure
description: >-
  Exploit SQL injection vulnerabilities in DB2 databases to execute a query that
  retrieves system environment information including OS name, version, release,
  and hostname.
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.156000+00:00'
updated_at: '2023-04-10T20:22:02.267615+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/DB2 Cheatsheet]]'
  - '[[tags/DB2 Injection]]'
  - '[[tags/Hostname/IP and OS INFO]]'
commands:
  - '[[commands/db2-query-system-environment-info]]'
tools: []
platforms:
  - Linux
  - Windows
  - Database
skill_level: intermediate
impact_level: medium
detection_risk: high
validated: true
---

# DB2-SQL-Injection-for-System-Information-Discovery

## Summary

This procedure demonstrates how to exploit SQL injection vulnerabilities in IBM DB2 databases to execute a specialized query that extracts system environment details, such as the operating system name, version, release level, and hostname. This discovery technique allows attackers to gather critical infrastructure information for further reconnaissance or targeted exploitation, typically requiring privileges executable within stored procedures or user-defined functions (UDFs).

## Description

DB2 SQL injection involves injecting malicious SQL code into input fields or parameters that are not properly sanitized, allowing execution of arbitrary queries on the database server. In this case, the target is the sysibmadm.env_sys_info system table, which stores environmental data about the host system running the DB2 instance. This information is valuable for attackers to understand the underlying OS (e.g., AIX, Linux, Windows), its patch level, and the server's identity, aiding in privilege escalation, lateral movement, or custom exploit development.

The procedure assumes a blind or error-based SQL injection point has been identified, such as in a web application's login form or search parameter connected to a DB2 backend. Execution requires the injected query to run with sufficient privileges, often limited to procedural contexts. Successful execution compromises system confidentiality and can chain into broader attacks like command execution if combined with other DB2 features.

## Requirements

1. Valid SQL injection vulnerability in a DB2-connected application (e.g., unsanitized user input in a web form).
2. Network access to the target DB2 instance (default port 50000/TCP).
3. Tools for crafting and sending injection payloads, such as [[tools/sqlmap]] or Burp Suite.
4. Basic knowledge of DB2 SQL syntax and injection techniques (e.g., union-based, time-based, or error-based).
5. The DB2 instance must allow execution from procedures or UDFs; direct ad-hoc queries may be restricted.

## Defense

- Apply the latest DB2 patches to mitigate known injection vulnerabilities (e.g., via IBM Fix Central).
- Use prepared statements and parameterized queries in application code to prevent injection.
- Implement web application firewalls (WAFs) with DB2-specific rules to detect anomalous SQL patterns.
- Enable DB2 auditing and monitor logs for unauthorized access to sysibmadm tables or procedural executions.
- Limit database user privileges to least-required levels and disable unnecessary system table access.

## Objectives

1. Identify and confirm a SQL injection entry point in the DB2 application.
2. Inject and execute a query to retrieve host system details.
3. Interpret the output to inform subsequent attack planning, such as OS-specific exploits.
4. Maintain stealth by using blind injection if direct output is unavailable.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Locate a vulnerable parameter in the application that interacts with the DB2 backend, such as a search field or URL parameter. Test for injection by appending a single quote (') and observing errors or delays indicating SQL parsing issues.

**Command** (use a generic SQLi tester like [[commands/sqlmap-basic-test]]):

```bash
sqlmap -u "http://target.com/search?q=test" --dbms=ibm --technique=B
```

> This step confirms DB2 as the backend and the injection type (e.g., boolean-based blind). Expected output includes error messages referencing DB2 syntax or successful payload confirmation. If no errors, try time-based delays with DB2-specific functions like SLEEP.

### Step 2: Craft the Injection Payload

**Context**: Build a payload that closes the original query and appends the target SELECT statement. For union-based injection, match the number of columns in the original query. Use comments (--) to terminate the injected string.

**Code** ([[codes/DB2-System-Environment-Query-SQL]]):

```sql
select os_name,os_version,os_release,host_name from sysibmadm.env_sys_info -- requires priv
```

> Embed this code into the payload, e.g., for a search parameter: q=' UNION SELECT os_name,os_version,os_release,host_name FROM sysibmadm.env_sys_info --. This step requires adjusting for the application's query structure. Expected output: No immediate response in blind scenarios, but confirmation via conditional responses (e.g., true/false pages).

### Step 3: Execute the Injected Query

**Context**: Send the crafted payload via the identified vector. If using a tool like sqlmap, automate extraction; otherwise, use manual requests with a proxy.

**Command** ([[commands/db2-query-system-environment-info]]):

```sql
select os_name,os_version,os_release,host_name from sysibmadm.env_sys_info -- requires priv
```

> Deliver this via the injection point, e.g., in a POST request body or URL. In procedural contexts, wrap it in a CREATE PROCEDURE if needed. Expected output: Retrieved values, such as OS_NAME: 'Linux', OS_VERSION: '4.18.0', HOST_NAME: 'dbserver01'. If privileges are insufficient, expect DB2 error -551 (authorization failure).

### Step 4: Extract and Verify Output

**Context**: Parse the response for the system details. In error-based injection, errors may leak data; in blind, use conditional payloads to infer character-by-character.

**Command** (use extraction tool like [[commands/sqlmap-extract-data]]):

```bash
sqlmap -u "http://target.com/search?q=test" --dbms=ibm --dump -T sysibmadm.env_sys_info -C os_name,os_version,os_release,host_name
```

> This automates dumping the columns. Success is indicated by populated data in the output file or console. Cross-verify by chaining with other discovery queries if partial data is obtained.

### Step 5: Clean Up and Assess Impact

**Context**: Remove any temporary artifacts (e.g., created UDFs) and document findings for next steps, like OS-specific enumeration.

No specific command needed, but monitor for alerts. Expected outcome: Full system profile without triggering obvious defenses.
