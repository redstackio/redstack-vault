---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.055399+00:00'
updated_at: '2023-04-10T20:24:30.423621+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Boolean-Enumerating-Table-Name]]'
  - '[[tags/SQLite-Injection]]'
commands: []
platforms:
  - Databases
  - SQLite
tools: []
validated: true
---

# SQLite-Boolean-Table-Enumeration

## Summary

SQLite Boolean Table Enumeration is an injection technique that allows an attacker to enumerate table names within an SQLite database using a boolean-based SQL injection attack. This technique is useful when the attacker has limited knowledge of the database schema and wants to discover the names of tables that may contain sensitive information. By leveraging queries against the sqlite_master table, the attacker first determines the length of a table name and then uses binary search to guess each character, relying on observable differences in application responses for true/false conditions.

## Description

In a boolean-based SQL injection scenario, the attacker injects conditions into a vulnerable query parameter where the application's response varies based on whether the condition evaluates to true or false (e.g., a normal page load for true, an error or blank page for false). For SQLite databases, the sqlite_master system table stores metadata about tables, including their names in the tbl_name column. This procedure targets user-created tables (excluding system tables starting with 'sqlite_'). The process begins by querying the length of the first non-system table's name, testing integer values until a true response is observed. Once the length is known, binary search is applied to each character position: the attacker guesses the ASCII value of the character at that position by injecting conditions that compare it to midpoint values in the printable ASCII range (typically 32-126), narrowing down until the exact character is identified. This method is stealthy as it doesn't require error-based leakage and works against blind injection points. It assumes the attacker has identified a confirmed boolean SQLi vulnerability in an application backed by SQLite.

## Requirements

1. Confirmed boolean-based SQL injection vulnerability in an application using SQLite as the backend database.
2. Ability to observe differential responses from the application (e.g., via time delays, content differences, or status codes) to distinguish true/false conditions.
3. Knowledge of the injection point (e.g., a URL parameter, POST field, or cookie value).
4. Optional: A proxy tool like Burp Suite to craft and replay requests systematically.

## Defense

Defensive measures and detection strategies:

- Use parameterized queries or prepared statements to prevent SQL injection attacks by separating code from user input.
- Implement proper input validation and sanitization to reject or escape malicious payloads.
- Restrict database access to authorized personnel only and run applications with least privilege to limit damage from injections.
- Enable database logging and monitor for anomalous queries accessing system tables like sqlite_master.
- Deploy web application firewalls (WAFs) tuned to detect injection patterns, including boolean conditions and metadata queries.

## Objectives

1. Identify the length of the first user table name in the SQLite database.
2. Enumerate the exact characters of the table name using binary search.
3. Discover potential tables containing sensitive data for further exploitation.
4. Expected outcome: Full table name(s) reconstructed, enabling targeted follow-on attacks like data extraction.

## Instructions

### Step 1: Confirm Boolean SQL Injection and Determine Table Name Length

**Context**: Begin by verifying the injection point supports boolean conditions, then inject a payload to query the length of the first non-system table name. Test sequential integer values (e.g., 1 to 30) as the expected length until the application responds with a 'true' condition, indicating a match. This step isolates the target table from system ones using the WHERE clause.

**Code** ([[codes/SQLite-Table-Name-Length-Boolean-Query]]):

```sql
and (SELECT length(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name not like 'sqlite_%' limit 1 offset 0)=table_name_length_number
```

> Append this payload to the vulnerable parameter (e.g., id=1' [payload] --). Replace 'table_name_length_number' with test values like 5, 6, etc. A 'true' response (normal page) confirms the length; 'false' (error/different page) means try the next value. Why: This avoids guessing full names by first bounding the search space. Expected: After 1-30 tests, identify the length (common table names are 5-15 characters).

### Step 2: Enumerate Each Character Using Binary Search

**Context**: With the table name length known (e.g., 8 characters), for each position (1 to length), perform binary search on the printable ASCII range (low=32 for space, high=126 for ~). Calculate midpoint = (low + high) / 2, inject a condition to check if the character's ASCII value is greater than the midpoint. If true, set low = midpoint + 1; if false, high = midpoint - 1. Repeat until low == high, revealing the character. Convert the final ASCII value back to the character (e.g., 97 = 'a'). This typically takes 7-8 guesses per character due to the 95-character range.

**Code** ([[codes/SQLite-Table-Name-Character-Ascii-Comparison-Query]]):

```sql
and (SELECT case when ascii(substr(tbl_name, position, 1)) > ascii_value then 1 else 0 end FROM sqlite_master WHERE type='table' and tbl_name not like 'sqlite_%' limit 1 offset 0)=1
```

> Inject as ' [payload] --, replacing 'position' with the current character position (e.g., 1) and 'ascii_value' with the midpoint (e.g., 79). A true response means the character is higher; false means lower or equal. Why: Binary search efficiently narrows possibilities without leaking data directly. Expected: After iterations, reconstruct the full name (e.g., 'users'). If multiple tables, increment 'offset' in the query to target the next (e.g., offset 1 for second table).

### Step 3: Verify and Document Discovered Tables

**Context**: Once the table name is fully enumerated, test it in a simple injection to confirm (e.g., inject 'and exists(select * from [table_name])'). If valid, note it for further enumeration (e.g., columns via similar techniques on pragma_table_info). Decision point: If the first table is irrelevant, repeat for offset 1, 2, etc., until sensitive tables are found or a limit is hit.

> No specific code needed; use a basic existence check: 'and (select count(*) from [enumerated_table_name])>0 --'. Expected: True confirms the table exists and is accessible.
