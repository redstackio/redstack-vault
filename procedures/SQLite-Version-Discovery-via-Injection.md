---
id: ad1bb7f8-0cb3-48ca-9603-bc47f133bece
name: SQLite-Version-Discovery-via-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:36.945053+00:00'
updated_at: '2023-04-10T20:24:31.601109+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - sqlite-injection
  - version-discovery
commands:
  - '[[codes/SQLite-Version-Query]]'
platforms:
  - Linux
  - Windows
  - macOS
  - Web
tools: []
validated: true
---

# SQLite-Version-Discovery-via-Injection

## Summary

This procedure demonstrates how to discover the version of an SQLite database through a SQL injection vulnerability in an application. By injecting a simple SQL query, attackers can retrieve the SQLite version string, which helps identify potential vulnerabilities specific to that version and tailor further exploitation efforts.

## Description

SQLite is a lightweight, embedded SQL database engine commonly used in web applications, mobile apps, and desktop software. When an application fails to properly sanitize user inputs, attackers can inject malicious SQL queries to manipulate the database. Discovering the SQLite version is a critical reconnaissance step in SQL injection attacks, as different versions may have known exploits, such as buffer overflows or privilege escalation paths. This procedure assumes an identified injection point (e.g., in a login form or search field) and focuses on extracting the version using the built-in sqlite_version() function. Success reveals the version in the format 'X.Y.Z', enabling targeted attacks like version-specific payload crafting or chaining to data exfiltration.

## Requirements

1. Identified SQL injection vulnerability in an application using SQLite as the backend.
2. Network access to the vulnerable application (e.g., via browser or proxy like Burp Suite).
3. Basic knowledge of SQL syntax and injection techniques to craft and deliver the payload.
4. Tools for intercepting and modifying HTTP requests if the injection is over the web (e.g., [[tools/Burp-Suite]] or browser developer tools).

## Defense

- Keep SQLite libraries updated to the latest version to patch known vulnerabilities.
- Implement strict input validation, prepared statements, and parameterized queries to prevent SQL injection.
- Use web application firewalls (WAFs) to detect and block anomalous SQL queries.
- Monitor database logs for unusual queries, such as calls to sqlite_version(), and enable query whitelisting.

## Objectives

1. Inject a SQL query to retrieve the SQLite database version.
2. Analyze the version to identify exploitable vulnerabilities.
3. Use the version information to select or adapt subsequent attack payloads.

## Instructions

### Step 1: Identify Injection Point and Test Basic Injection

**Context**: Locate a user-controllable input field vulnerable to SQL injection, such as a search box or URL parameter. Test with a simple payload like a single quote (') to confirm error-based injection, which may reveal SQLite-specific errors confirming the backend.

**Command** (use a tool like sqlmap or manual injection via curl):

First, confirm injection with a basic test using [[codes/SQLite-Version-Query]] embedded in the payload.

For manual web injection, append the payload to the vulnerable parameter, e.g., in a GET request: `search=' UNION SELECT sqlite_version();--`

> This step verifies the injection point responds to SQL and begins extracting metadata. If using an automated tool, specify the injection parameter; manually, observe for SQL errors like "near \"'": syntax error" which indicate SQLite.

### Step 2: Inject the Version Query Payload

**Context**: Once injection is confirmed, craft a payload that executes the sqlite_version() function. This function returns the compile-time SQLite version without requiring elevated privileges, making it ideal for initial discovery.

**Code** ([[codes/SQLite-Version-Query]]):

```sql
select sqlite_version();
```

Embed this in your injection payload, e.g., `'; select sqlite_version(); --` for string-based inputs or UNION-based for query stacking.

**Command** ([[codes/SQLite-Version-Query]]):

```sql
select sqlite_version();
```

> Deliver the payload via the application's interface or HTTP request. For example, using curl for a GET injection: `curl "http://target.com/search?q=';+select+sqlite_version();--"`. The response should include the version string if successful, often in error messages or reflected output.

### Step 3: Verify and Analyze Output

**Context**: Parse the application's response for the version string. If error-based, it may appear in a database error; if blind, use conditional payloads to infer the version character-by-character.

No specific command here; inspect the HTTP response body or use string matching in tools like Burp.

> Expected version format: '3.36.0' or similar. Cross-reference with CVE databases (e.g., search for "SQLite 3.36.0 vulnerability") to identify issues like CVE-2022-35737 for older versions.

### Step 4: Mitigate Detection and Escalate

**Context**: If the query succeeds, note any logging or rate-limiting. Proceed to version-specific exploits, such as attaching databases or executing system commands if the version supports it.

> Success confirms the version; failure may indicate sanitization—try variations like hex-encoding the query.
