---
id: e3067bfb-0c3d-4f09-8830-e4ec80133dfd
name: Prevent-MSSQL-Stacked-Query-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.895774+00:00'
updated_at: '2023-04-10T20:22:45.653938+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - mssql-injection
  - stacked-query
  - sql-injection-prevention
commands: []
platforms:
  - Windows
  - SQL Server
tools: []
validated: true
---

# Prevent-MSSQL-Stacked-Query-Injection

## Summary

This procedure outlines defensive measures to prevent MSSQL stacked query injection attacks, where attackers append multiple SQL statements separated by semicolons to execute unauthorized actions like data modification or extraction. By implementing input validation, parameterized queries, and access controls, organizations can mitigate risks associated with untrusted user input in SQL statements.

## Description

MSSQL stacked query injection occurs when an application fails to properly sanitize user input, allowing attackers to inject additional SQL commands into a single query execution. For example, an attacker might append '; DROP TABLE users --' to a legitimate query to delete data. This technique exploits vulnerabilities in dynamic SQL construction and can lead to data breaches, unauthorized modifications, or full database compromise. This procedure focuses on preventive strategies tailored for Microsoft SQL Server environments, including code-level protections and configuration best practices. It assumes a development or administrative context where application code or database configurations can be modified to enforce secure query handling.

## Requirements

1. Administrative or developer access to the application codebase and database server.
2. Familiarity with SQL Server Management Studio (SSMS) or similar tools for testing queries.
3. Access to modify database user permissions and roles.
4. Knowledge of the application's query construction patterns, particularly those involving user input.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation to reject or escape special characters like semicolons (;), double dashes (--), and other SQL delimiters.
- Enforce parameterized queries or stored procedures to separate SQL logic from user data, preventing injection of additional statements.
- Apply least privilege principles by granting database users minimal permissions (e.g., read-only for queries, no DDL rights for SELECT operations).
- Enable SQL Server auditing and logging to monitor for anomalous query patterns, such as multiple statements in a single execution.
- Use web application firewalls (WAF) with SQL injection rules to block suspicious payloads at the network layer.

## Objectives

1. Block execution of unauthorized multiple SQL statements from user input.
2. Protect database integrity by preventing data deletion, modification, or exfiltration via stacked queries.
3. Ensure application availability by avoiding denial-of-service from destructive injections.
4. Maintain compliance with security standards like OWASP Top 10 for injection prevention.

## Instructions

### Step 1: Review and Identify Vulnerable Query Patterns

**Context**: Begin by auditing existing SQL queries in the application to identify areas where user input is directly concatenated into statements, which enables stacked injections.

Examine code for patterns like 'SELECT * FROM products WHERE id = ' + userInput, which could allow appended commands.

> Look for dynamic SQL construction in languages like C#, PHP, or Java. Use tools like static code analyzers (e.g., SonarQube) to flag potential injection points.

### Step 2: Implement Parameterized Queries

**Context**: Replace concatenated queries with parameterized versions to ensure user input is treated as data, not executable code, preventing stacked statement execution.

For example, in .NET with SqlCommand:

```csharp
using (SqlCommand cmd = new SqlCommand("SELECT * FROM products WHERE id = @id", connection))
{
    cmd.Parameters.AddWithValue("@id", userInput);
    SqlDataReader reader = cmd.ExecuteReader();
}
```

> This binds userInput to @id as a parameter, so even if it contains '; DROP TABLE --', it won't execute as a separate statement. Test by attempting to inject the example payload from [[codes/MSSQL-Stacked-Query-Malicious-Input-Example]]; the query should fail safely without executing the DROP.

### Step 3: Enforce Least Privilege Access

**Context**: Limit the permissions of the database account used by the application to reduce the impact of any successful injection.

In SSMS, alter the user role:

```sql
ALTER ROLE db_datareader ADD MEMBER app_user;
DENY ALTER ON SCHEMA::dbo TO app_user;
DENY DELETE ON SCHEMA::dbo TO app_user;
```

> This grants read access but denies destructive operations like DROP or ALTER. Verify by logging in as app_user and attempting a DROP statement; it should return a permission denied error.

### Step 4: Enable Query Logging and Validation

**Context**: Configure SQL Server to log all queries and implement server-side validation to detect and block stacked attempts.

Enable auditing:

```sql
CREATE SERVER AUDIT sql_injection_audit TO FILE (FILEPATH = 'C:\Audit\');
ALTER SERVER AUDIT sql_injection_audit WITH (STATE = ON);
CREATE DATABASE AUDIT SPECIFICATION db_audit FOR SERVER AUDIT sql_injection_audit ADD (DATABASE_OPERATION (INSERT, UPDATE, DELETE));
```

> Review logs for queries containing multiple semicolons or suspicious patterns. Integrate with SIEM tools for real-time alerts on potential injections.

### Step 5: Test and Validate Prevention

**Context**: Simulate injection attempts to confirm the defenses are effective.

Use a testing framework like SQLMap or manual payloads to probe endpoints. For instance, submit the malicious input from [[codes/MSSQL-Stacked-Query-Malicious-Input-Example]] via a vulnerable form.

> Expected success: The query executes only the intended SELECT, with no additional statements processed. No data loss or errors indicating execution of DROP.
