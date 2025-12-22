---
id: d174829e-4ff7-49cd-b7f3-3c26071347cf
name: enumerate-database-names-with-sqlmap
type: procedure
verified: true
submitted: true
created_at: '2020-08-19T17:15:14.214665+00:00'
updated_at: '2023-05-26T15:59:24.087020+00:00'
platforms:
  - Web
tags:
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/sqli]]'
  - '[[tags/SQL Injection]]'
  - '[[tags/Web Applications]]'
commands:
  - '[[commands/sqlmap-enumerate-databases]]'
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
validated: true
---

# Enumerate Database Names with SQLMap

## Summary

This procedure uses SQLMap, an automated tool for exploiting SQL injection vulnerabilities, to enumerate the names of databases on a target web application's backend database server. It is particularly useful in penetration testing scenarios where a SQL injection point has been identified in a GET parameter, allowing attackers to extract database schema information for further exploitation.

## Description

SQL injection (SQLi) vulnerabilities in web applications can allow unauthorized access to underlying database structures. Once a vulnerable parameter is identified, SQLMap can automate the detection and exploitation process to list available databases without manual payload crafting. This procedure assumes a time-based blind SQLi vulnerability in a search parameter, as commonly found in e-commerce or content management systems. The technique exploits the application's interaction with a MySQL backend (or similar) to infer database names through delayed responses or error messages. Successful execution reveals databases like 'information_schema', which contains metadata, and custom application databases, enabling subsequent enumeration of tables, columns, and data.

## Requirements

1. A vulnerable web application URL with a SQLi-prone parameter (e.g., a search field accepting GET requests).
2. Network access to the target application (no authentication required for initial injection points).
3. SQLMap tool installed on the attacker's machine (see [[tools/sqlmap]] for installation).
4. Basic knowledge of the target's technology stack (e.g., PHP/Apache with MySQL backend).
5. Optional: Prior session file from SQLMap if resuming a previous scan.

## Defense

Defensive measures and detection strategies:

- Implement prepared statements and parameterized queries in application code to prevent SQLi.
- Use web application firewalls (WAFs) like ModSecurity to detect and block SQLMap-like payloads.
- Enable database logging to monitor anomalous queries, such as SLEEP() functions in time-based attacks.
- Regularly scan for vulnerabilities using tools like OWASP ZAP or Nessus.

## Objectives

1. Confirm the presence of a SQL injection vulnerability in the target parameter.
2. Extract a list of database names from the backend DBMS.
3. Identify potential high-value databases for further enumeration (e.g., user or application-specific DBs).
4. Expected outcome: A complete list of accessible databases, enabling targeted data extraction.

## Instructions

### Step 1: Identify and Verify the Vulnerable Endpoint

**Context**: Before enumerating databases, confirm the URL and parameter are vulnerable to SQLi. This step involves basic testing to ensure SQLMap can interact properly, avoiding false positives.

Use manual testing or a preliminary SQLMap scan to detect the injection type (e.g., time-based blind).

**Command** ([[commands/sqlmap-detect-injection]]):
```bash
sqlmap -u 'http://example.com/search.php?term=test' --batch --level=1
```

> This command tests the 'term' parameter for vulnerabilities. The --batch flag runs without prompts, and --level=1 performs basic tests. Expected output includes detection of injection types like 'AND/OR time-based blind' if vulnerable. If confirmed, proceed; otherwise, identify another parameter.

### Step 2: Enumerate Database Names

**Context**: With the vulnerability confirmed, use SQLMap to query the backend DBMS for database names. This exploits the injection to fetch metadata, resuming from any prior session if available.

**Command** ([[commands/sqlmap-enumerate-databases]]):
```bash
sqlmap -u 'http://example.com/search.php?term=' --dbs --batch
```

> Replace the URL with the target endpoint. The --dbs flag specifically enumerates databases. SQLMap will detect the DBMS (e.g., MySQL), test the injection, and list databases. If a session file exists (from Step 1), it resumes automatically. Watch for warnings about empty parameters and redirects.

### Step 3: Interpret and Validate Results

**Context**: Review the output to confirm success and note key databases for follow-up actions, such as table enumeration.

Manually inspect the listed databases and cross-reference with known application schemas.

**Command** (No specific command; use output from Step 2):

> Expected results include system databases like 'information_schema' and application-specific ones (e.g., 'vjdb', 'ads'). Success is indicated by a list without errors. If fewer than expected databases appear, increase --level or use --risk=2 for deeper probing. Save output to a file with -o for documentation.
