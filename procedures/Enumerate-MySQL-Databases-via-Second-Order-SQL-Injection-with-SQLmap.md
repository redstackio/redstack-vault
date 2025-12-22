---
type: procedure
description: >-
  Use SQLmap to exploit second-order SQL injection vulnerabilities in a web
  application to enumerate databases and structures in a MySQL backend.
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - sql-injection
  - second-order-injection
  - sqlmap
  - mysql
  - database-enumeration
commands:
  - '[[commands/sqlmap-second-order-injection-with-request-file]]'
  - '[[commands/sqlmap-enumerate-databases-in-specific-db]]'
tools:
  - '[[tools/sqlmap]]'
platforms:
  - Web
  - Linux
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Enumerate-MySQL-Databases-via-Second-Order-SQL-Injection-with-SQLmap

## Summary

This procedure demonstrates how to use SQLmap to automate the detection and exploitation of second-order SQL injection vulnerabilities in a web application backed by MySQL, focusing on enumerating database names, tables, and columns to facilitate further data extraction or privilege escalation.

## Description

Second-order SQL injection occurs when user input is stored in the database and later retrieved and executed in a SQL query, often evading first-order detection. SQLmap automates the identification of such vulnerabilities by analyzing HTTP requests and injecting payloads. This procedure targets MySQL databases, common in web applications like Joomla, to enumerate schema information. The attack assumes an injectable endpoint has been identified via manual testing or automated scanning. Successful enumeration reveals database structures, enabling targeted data theft or command execution.

## Requirements

1. Network access to the target web application.
2. A captured HTTP request file (e.g., from Burp Suite) containing the injectable parameter.
3. SQLmap installed on the attacker's system (Kali Linux recommended).
4. Basic knowledge of HTTP requests and SQL syntax for troubleshooting.

## Defense

- Implement prepared statements and parameterized queries to prevent SQL injection.
- Use web application firewalls (WAFs) to detect anomalous SQL patterns in requests.
- Conduct regular input validation and output encoding on stored data.
- Monitor database logs for unusual queries and limit database user privileges to read-only where possible.

## Objectives

1. Detect and confirm second-order SQL injection in the target application.
2. Enumerate all accessible databases on the MySQL server.
3. Identify tables and columns within a specific database for further exploitation.
4. Gather schema information to support data exfiltration or RCE.

## Instructions

### Step 1: Test for Second-Order Injection Using Request File

**Context**: Begin by loading a captured HTTP request into SQLmap and specifying the second-order injection mode. This step identifies if the endpoint is vulnerable and prepares for enumeration. Use a request file (e.g., r.txt) from a proxy tool capturing a POST or GET with injectable parameters.

**Command** ([[commands/sqlmap-second-order-injection-with-request-file]]):
```bash
python sqlmap.py -r /tmp/r.txt --dbms=MySQL --second-order "http://targetapp/wishlist" -v 3
```

> This command loads the request from r.txt, targets MySQL, enables second-order mode by specifying the delayed execution URL, and sets verbosity to 3 for detailed output. It will attempt injections and report if the vulnerability is confirmed. Expected output includes confirmation messages like "second-order injection confirmed" and initial payload tests.

### Step 2: Enumerate Databases in a Specific Schema

**Context**: Once vulnerability is confirmed, target a known database (e.g., from application context like 'joomla') to list all databases or drill down. This step uses the second-order flag to exploit stored inputs and reveals the full database inventory.

**Command** ([[commands/sqlmap-enumerate-databases-in-specific-db]]):
```bash
sqlmap -r 1.txt --dbms=MySQL --second-order "http://<IP/domain>/joomla/administrator/index.php" -D "joomla" --dbs
```

> This command uses request file 1.txt, specifies MySQL and second-order mode with the execution URL, targets the 'joomla' database, and enumerates all databases (--dbs). If successful, it outputs a list of database names. For further enumeration, add --tables or --columns flags in subsequent runs.
