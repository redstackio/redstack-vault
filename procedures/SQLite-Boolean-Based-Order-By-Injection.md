---
id: ce1253ab-87b8-4ce3-8052-bc4f02ee17d7
name: SQLite-Boolean-Based-Order-By-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.094838+00:00'
updated_at: '2023-04-10T20:24:28.458022+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/boolean-based]]'
  - '[[tags/order-by]]'
  - '[[tags/sqlite-injection]]'
  - '[[tags/sqli]]'
commands: []
platforms:
  - Web
  - SQLite
tools: []
validated: true
---

# SQLite-Boolean-Based-Order-By-Injection

## Summary

SQLite Boolean-Based Order By Injection is a blind SQL injection technique that leverages the ORDER BY clause in SQLite queries to extract sensitive information, such as table names, column data, or other database contents, without directly observing query results. By injecting conditional logic into the ORDER BY clause, an attacker can influence the sorting behavior based on boolean conditions derived from database queries, allowing bit-by-bit or character-by-character data extraction through observable changes in response times, order, or error patterns.

## Description

This procedure targets web applications using SQLite as the backend database where user input is improperly sanitized and concatenated into SQL queries, particularly those involving ORDER BY clauses for sorting results. SQLite, being a file-based, serverless database commonly embedded in applications, is vulnerable to injection if queries are not parameterized. The technique exploits the ORDER BY clause by injecting a CASE WHEN statement that evaluates a boolean condition against database metadata (e.g., from sqlite_master) or user tables. If the condition is true, the results are sorted one way (e.g., ascending); if false, another way (e.g., descending). By observing the sorted output or response differences, attackers infer data values iteratively.

Common scenarios include extracting table structures from sqlite_master or dumping user credentials from application tables. This is particularly effective in blind scenarios where no direct error messages are returned, but sorting artifacts are visible. Prerequisites include identifying an injectable parameter (e.g., a search or sort field) and confirming SQLite usage via fingerprinting (e.g., version-specific errors). The procedure assumes a GET or POST parameter vulnerable to injection and focuses on extracting the first table name as an example, but it can be adapted for broader enumeration.

## Requirements

1. Network access to a web application with a reflected or stored input field that influences an ORDER BY clause in a SQLite-backed query.
2. A proxy tool like Burp Suite to intercept and modify requests for precise injection testing.
3. Knowledge of the base query structure, ideally confirmed via error-based testing or union-based probes to determine column count.
4. A way to observe sorting changes, such as distinct response content, page layouts, or timings in high-load scenarios.

## Defense

Defensive measures and detection strategies:

- Use parameterized queries or prepared statements in application code to separate SQL logic from user input.
- Implement web application firewalls (WAFs) with SQLite-specific injection signatures to block anomalous ORDER BY payloads.
- Enable database logging and monitor for unusual query patterns, such as frequent CASE WHEN usage or accesses to sqlite_master.
- Sanitize and validate all inputs, rejecting non-alphanumeric sort directives.
- Regularly audit application code for direct SQL concatenation and conduct SQLi penetration testing.

## Objectives

1. Identify and confirm a vulnerable ORDER BY injection point in a SQLite-based web application.
2. Extract database metadata, such as table names, by using boolean conditions to influence query sorting.
3. Infer sensitive data character-by-character through iterative boolean tests on the sorted output.
4. Achieve reconnaissance or data exfiltration without triggering direct errors.

## Instructions

### Step 1: Confirm Vulnerability and Column Count

**Context**: Begin by verifying the injection point in the ORDER BY clause and determining the number of columns in the original query, as this sets the baseline for payload construction. Append a large ORDER BY number (e.g., ORDER BY 100) to see if it causes an error indicating the maximum sortable columns.

**Why**: SQLite will error if the ORDER BY exceeds the query's column count, confirming the vulnerability and exact number (e.g., if ORDER BY 5 works but 6 fails, there are 5 columns).

Use a browser or proxy to test the parameter:

```sql
' ORDER BY 1--
' ORDER BY 5--
' ORDER BY 6--
```

**Expected Output**: Successful sorts for valid column counts; an error like "no such column" or empty results for invalid ones, confirming 5 columns in this example.

### Step 2: Craft Boolean Condition for Data Extraction

**Context**: Construct a CASE WHEN payload to test boolean conditions against database content, such as the first character of the first user table name from sqlite_master. Replace placeholders with specific values for iterative testing (e.g., test ASCII values 65-122 for letters).

**Why**: The boolean evaluation (true/false) dictates the sort order, allowing inference of data via observable differences in response (e.g., ascending vs. descending sort).

Use the following code snippet [[codes/SQLite-Order-By-Boolean-Injection-Snippet]] injected into the vulnerable parameter:

**Code** ([[codes/SQLite-Order-By-Boolean-Injection-Snippet]]):

```sql
CASE WHEN (SELECT hex(substr(sql,1,1)) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' limit 1 offset 0) = hex('some_char') THEN <order_element_1> ELSE <order_element_2> END
```

Inject as: `?sort=users.id,' ORDER BY [payload] ASC--`

For example, to test if the first character is 'u' (hex 75):

```sql
CASE WHEN (SELECT hex(substr(sql,1,1)) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' limit 1 offset 0) = hex('u') THEN 1 ELSE 2 END
```

**Expected Output**: If true, results sort by column 1 (e.g., ascending IDs); if false, by column 2 (e.g., descending names). Observe the page layout or content order to determine truth value.

### Step 3: Iterate to Extract Full Data

**Context**: Repeat Step 2 for each character position (substr(sql, position, 1)) and possible values, building the extracted string incrementally (e.g., first char 'u', second 's', etc., to reveal 'users').

**Why**: Boolean-based extraction requires binary search or exhaustive testing per character, but ORDER BY provides a reliable oracle without errors.

Adapt the payload by changing substr position and hex('char'):

```sql
CASE WHEN (SELECT hex(substr(sql,2,1)) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' limit 1 offset 0) = hex('s') THEN 1 ELSE 2 END
```

Continue until the full table name (or desired data) is reconstructed.

**Expected Output**: Consistent sort behavior matching the boolean result, allowing reconstruction of the string (e.g., after tests, table name 'users' confirmed).

### Step 4: Verify and Expand Extraction

**Context**: Once a table name is extracted, adapt the payload to query that table's columns or data, using similar boolean logic.

**Why**: This escalates from metadata extraction to actual data theft, such as usernames or hashes.

Example for extracting first column name:

```sql
CASE WHEN (SELECT hex(substr(sql,1,1)) FROM sqlite_master WHERE type='table' and name='users') = hex('i') THEN 1 ELSE 2 END
```

**Expected Output**: Boolean-confirmed characters building column names like 'id', then pivot to data extraction with COUNT or SUBSTR on user tables.

**Success Indicators**:
- Sort order changes predictably based on injected conditions.
- Extracted characters form valid database artifacts (e.g., table names like 'users').
- No application errors, indicating blind but successful inference.
