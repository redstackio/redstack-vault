---
id: cdf98df3-55c7-4146-92e1-4da7ee903ca0
type: procedure
verified: true
submitted: true
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - owasp
  - owasp-top-10
  - sql
  - sqli
  - sql-injection
  - web-applications
commands:
  - '[[commands/sql-injection-order-by-column-count]]'
  - '[[commands/sql-injection-union-select-nulls]]'
  - '[[commands/sql-injection-union-concatenate-data]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Union SQL Injection to Retrieve Multiple Values in a Single Column

## Summary

This procedure outlines how to perform a UNION-based SQL injection attack to extract multiple pieces of data (such as usernames and passwords) from a database by concatenating them into a single output column. It is particularly useful in scenarios where the vulnerable application only displays data from one column, allowing attackers to bypass this limitation and exfiltrate sensitive information from other tables.

## Description

UNION SQL injection exploits a vulnerability in web applications that fail to properly sanitize user input in SQL queries, typically in GET or POST parameters. By appending a UNION SELECT statement, an attacker can combine results from the original query with data from other tables. This procedure first determines the number of columns in the original query using ORDER BY clauses to identify error points, then uses NULL values in a UNION SELECT to map which columns are visible in the application's output. Finally, it concatenates desired data (e.g., using || for Oracle/PostgreSQL or CONCAT for MySQL) into a single visible column for retrieval. This technique targets web applications backed by relational databases like MySQL, PostgreSQL, or Oracle, assuming the injection point is in a searchable parameter like 'category'. Success depends on the database type and application logic, with outputs displayed in the application's response.

## Requirements

1. Network access to the target web application (e.g., via browser or proxy).
2. A vulnerable SQL injection point, such as a GET parameter in a search or filter function.
3. Tools like [[tools/Burp-Suite]] for intercepting and modifying requests, or curl for direct injection.
4. Basic knowledge of the target database type (e.g., MySQL uses CONCAT(), PostgreSQL/Oracle use ||).
5. No authentication required if the injection point is unauthenticated, but credentials may be needed for authenticated areas.

## Defense

Defensive measures and detection strategies:

- Use prepared statements or parameterized queries to separate SQL code from user input.
- Implement a Web Application Firewall (WAF) to detect and block common SQL injection patterns like UNION SELECT or ORDER BY.
- Sanitize and validate all user inputs, rejecting suspicious characters like ' , --, or ||.
- Enable database logging to monitor anomalous queries, and use intrusion detection systems (IDS) to flag concatenated SELECTs.
- Regularly audit application code and conduct penetration testing to identify injection points.

## Objectives

1. Confirm the presence of a SQL injection vulnerability in a web parameter.
2. Determine the number of columns in the original query to craft a valid UNION statement.
3. Identify which output columns are visible in the application's response.
4. Extract sensitive data by concatenating multiple fields into a single visible column.
5. Retrieve and parse the exfiltrated data for further use, such as credential harvesting.

## Instructions

### Step 1: Identify the Vulnerable Parameter

**Context**: Locate a parameter susceptible to SQL injection, such as a 'category' in a URL query string (e.g., http://target.com/search?category=books). Test for basic injection by appending a single quote (') to trigger a SQL error, confirming the parameter influences the query.

Navigate to the application in a browser or use [[tools/Burp-Suite]] to intercept requests. Append ' to the parameter value and submit. If an SQL error (e.g., syntax error near '') appears, the parameter is vulnerable.

**Expected Output**: Database error message indicating unescaped input, such as "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1".

### Step 2: Determine the Number of Columns

**Context**: Use an ORDER BY clause to probe the number of columns in the original SELECT query. Increment the column number until an error occurs, revealing the exact count needed for the UNION SELECT to match.

**Command** ([[commands/sql-injection-order-by-column-count]]):
```bash
curl "http://$_TARGET_URL?$_PARAM=1' ORDER BY $_COLUMN_NUM--" -v
```

> This command sends a GET request with an ORDER BY clause. Start with $_COLUMN_NUM=1 and increase (e.g., 2, 3, ...) until a "Unknown column" or similar error is returned. The last successful response (no error) indicates the column count (e.g., if ORDER BY 5 succeeds but 6 fails, there are 5 columns). Use -v for verbose output to inspect HTTP responses.

**Expected Output**: Successful responses return normal page content; failure shows a database error like "ORDER BY items must appear in the select list" or "Unknown column".

### Step 3: Map Visible Columns with NULLs

**Context**: Craft a UNION SELECT with NULL values to determine which positions in the result set are displayed by the application. This step ensures the payload aligns with visible output columns.

**Command** ([[commands/sql-injection-union-select-nulls]]):
```bash
curl "http://$_TARGET_URL?$_PARAM=-1' UNION SELECT $_NULL_COUNT--" -v
```

> Replace $_NULL_COUNT with comma-separated NULLs matching the column count (e.g., for 3 columns: NULL,NULL,NULL). Submit variations to see where NULL appears in the output. The position where NULL displays indicates a visible column.

**Expected Output**: Application response showing NULL in specific positions, e.g., a table row with "NULL" in the category field, confirming that column is injectable.

### Step 4: Concatenate and Retrieve Data

**Context**: Once columns are mapped, use UNION SELECT to pull data from target tables (e.g., users) and concatenate multiple fields into a single visible column using database-specific operators (|| for PostgreSQL/Oracle, CONCAT() for MySQL).

**Command** ([[commands/sql-injection-union-concatenate-data]]):
```bash
curl "http://$_TARGET_URL?$_PARAM=-1' UNION SELECT NULL, username||'~'||password FROM $_TABLE_NAME--" -v
```

> Adjust NULL positions based on Step 3 (e.g., NULL in non-visible columns). Use a delimiter like '~' to separate values. Query system tables if table names are unknown (e.g., information_schema.tables in MySQL). Repeat for pagination if results are limited.

**Expected Output**: Application displays concatenated data in the visible column, e.g., "admin~password123" in the category field, allowing parsing of usernames and passwords.

### Step 5: Verify and Parse Results

**Context**: Confirm data integrity and extract individual values. If errors occur, adjust for database specifics (e.g., use GROUP_CONCAT for MySQL to handle multiple rows).

Manually parse the output by splitting on the delimiter. If no data appears, verify table/column names via error-based injection or blind techniques.

**Expected Output**: List of concatenated records, e.g., multiple rows showing "user1~pass1", "user2~pass2".
