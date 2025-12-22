---
id: f963d9e5-2f5b-4f2b-982c-87a6524f06d5
name: Extract-MySQL-Version-and-Schema-via-Blind-Substring-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.557722+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Web Shell]]'
sub_techniques: []
tags:
  - mysql-injection
  - blind-sqli
  - substring-extraction
  - database-enumeration
commands: []
platforms:
  - Web
  - MySQL
tools: []
validated: true
---

# Extract-MySQL-Version-and-Schema-via-Blind-Substring-Injection

## Summary

This procedure demonstrates how to perform blind SQL injection on a MySQL database using substring equivalent functions to extract the database version and schema information character by character. By injecting payloads that leverage functions like SUBSTRING, LEFT, RIGHT, ASCII, and MID, attackers can infer data from boolean responses without direct output, enabling reconnaissance of the target's database structure for further exploitation.

## Description

Blind SQL injection occurs when an application reveals no direct error messages or data from queries, but differences in response time or content (e.g., true/false conditions) allow inference of information. This technique targets MySQL databases vulnerable to injection in user inputs, such as search fields or login forms. The procedure uses equivalent substring extraction methods to bypass potential filtering of specific functions like SUBSTRING, employing alternatives such as LEFT, RIGHT, MID, and ASCII conversions to deduce the MySQL version (e.g., '5.7.XX') and schema details (e.g., table and column names from information_schema). This is particularly useful in web applications where direct query dumping is blocked, allowing attackers to map the database for subsequent data extraction or privilege escalation. The target environment is typically a web app with a MySQL backend, accessible via HTTP parameters or POST data.

## Requirements

1. Valid injection point in the web application (e.g., a parameter vulnerable to SQLi, confirmed via basic tests like appending ' AND 1=1 --').
2. Knowledge of the base query structure or parameter position for injection.
3. Tools for sending and observing HTTP requests (e.g., browser, Burp Suite, or curl) to detect boolean response differences.
4. Patience for iterative character-by-character extraction, as blind techniques require multiple requests per byte.

## Defense

- Implement strict input validation and sanitization to reject suspicious characters or patterns common in SQLi payloads.
- Use prepared statements and parameterized queries in application code to separate SQL logic from user input.
- Enable MySQL query logging and monitor for anomalous queries, especially those accessing information_schema or using substring functions.
- Deploy web application firewalls (WAFs) tuned to detect blind injection patterns, such as repeated conditional queries.

## Objectives

1. Determine the MySQL server version to assess potential vulnerabilities and compatible exploits.
2. Enumerate database schema, including table and column names, to identify sensitive data locations.
3. Gather infrastructure details for targeted follow-on attacks, such as credential extraction or privilege escalation.

## Instructions

### Step 1: Confirm Blind Injection Vulnerability and Prepare Base Payload

**Context**: Identify a parameter vulnerable to blind SQLi by testing conditional statements that alter responses based on true/false outcomes. This step ensures the injection point works for boolean-based inference before proceeding to extraction.

Append a basic test payload to the vulnerable parameter (e.g., ?id=1) to verify:

```sql
?id=1 AND 1=1 --
```

Observe if the response differs from a false condition:

```sql
?id=1 AND 1=2 --
```

If responses vary (e.g., page loads vs. error or delay), proceed. Use a proxy tool to automate request sending and response comparison.

### Step 2: Extract MySQL Version Using Substring Equivalents

**Context**: Query the version() function character by character using alternative substring methods to bypass potential filters. Start with the first character and iterate through positions (1 to length of version string, typically 10-15 chars). For each position, test ASCII values from 32 to 126 until a true response confirms the character.

Use the following payloads, adapting the position (e.g., 1,1 for first char) and comparison value (e.g., =5 for char '5'):

Reference the extraction payloads: [[codes/MySQL-Blind-Substring-Version-Extraction-Payloads]]

Example for first character assuming version starts with '5':

```sql
?id=1 AND SUBSTRING(version(),1,1)='5'
```

If SUBSTRING is filtered, try equivalents:

```sql
?id=1 AND LEFT(version(),1)='5'
?id=1 AND RIGHT(LEFT(version(),1),1)='5'
?id=1 AND ASCII(LOWER(SUBSTR(version(),1,1)))=53
?id=1 AND (SELECT MID(version(),1,1)='5')
```

Send requests iteratively, noting true responses to build the version string (e.g., '5.7.34').

### Step 3: Enumerate Schema Tables Using Substring on information_schema

**Context**: Once version is known, extract table names from information_schema.tables. Query row by row and character by character, similar to version extraction. Limit to current database if possible (e.g., WHERE table_schema=DATABASE()). Start with first table's first character.

Use payloads like:

```sql
?id=1 AND (SELECT SUBSTR(table_name,1,1) FROM information_schema.tables WHERE table_schema=DATABASE() LIMIT 0,1) > 'A'
```

Iterate comparisons (>'A', ='B', etc.) for each position until the full name is inferred (e.g., 'users'). Repeat for subsequent tables by adjusting LIMIT (1,1; 2,1; etc.). If > operator is filtered, use = with ASCII.

### Step 4: Enumerate Schema Columns

**Context**: For each discovered table, extract column names from information_schema.columns. This reveals data types and potential sensitive fields (e.g., passwords). Filter by table_name in the query.

Example payload for first column of 'users' table:

```sql
?id=1 AND (SELECT SUBSTR(column_name,1,1) FROM information_schema.columns WHERE table_name='users' LIMIT 0,1) = 'i'
```

Build character by character, then move to next columns with LIMIT offsets. Verify extraction by noting consistent true/false patterns across requests.

### Step 5: Validate and Document Extracted Information

**Context**: Compile the inferred version and schema into a usable format. Cross-verify by testing a known query (e.g., extracting a single known char) to ensure accuracy.

Review the built strings for completeness. If extraction is slow, script the process using a tool like sqlmap (though manual for learning). Success is confirmed when schema matches expected MySQL structures or reveals exploitable elements like admin tables.
