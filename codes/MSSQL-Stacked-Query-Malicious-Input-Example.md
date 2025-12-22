---
id: 47c6a455-ccc6-4d4f-81a6-9e52d68c2401
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:33.894199+00:00'
updated_at: '2023-04-10T20:22:45.681066+00:00'
platforms:
  - SQL Server
tags:
  - sql-injection
  - stacked-query
  - malicious-payload
validated: true
---

# MSSQL-Stacked-Query-Malicious-Input-Example

## Code

```sql
ProductID=1; DROP members--
```

## Description

This SQL snippet represents a classic stacked query injection payload. It starts with a legitimate-looking parameter (ProductID=1) but appends a semicolon to separate statements, followed by a destructive DROP command on a 'members' table, and ends with a comment (--) to ignore any trailing query parts. When injected into an unsanitized input field, it can execute multiple statements, leading to data loss.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| ProductID | Placeholder for legitimate query parameter | 1 |
| members | Target table name for DROP (customize based on schema) | members |

## Usage

This code is used in penetration testing to demonstrate SQL injection vulnerabilities. Inject it into a web form or API parameter expecting a product ID, such as in a search query. For defensive testing, use it to validate prevention measures like parameterization—successful prevention will treat it as a single invalid value without executing the DROP.

## Detection

- Monitor application logs for queries containing semicolons (;) or comment sequences (--).
- Use database auditing to flag multi-statement executions from untrusted sources.
- Web application firewalls can signature-match patterns like '; DROP' or unusual SQL delimiters.
- Anomaly detection on query length or structure deviations from baselines.

## Related

- [[procedures/Prevent-MSSQL-Stacked-Query-Injection]]
