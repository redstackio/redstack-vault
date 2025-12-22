---
id: ff8fe5e4-acfa-4163-949e-8355e7cd58af
name: find-linked-servers-in-mssql
type: command
executor: sql
data: select * from master..sysservers
output: null
created_at: '2023-04-06T03:56:34.105203+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - discovery
verified: true
validated: true
---

# find-linked-servers-in-mssql

## Command

```sql
select * from master..sysservers
```

## Description

This SQL command queries the master database to list all configured linked servers on the current MSSQL instance, revealing trusted connections for potential lateral movement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; runs on the connected MSSQL instance | Yes |

## Examples

### Basic Usage

```sql
select * from master..sysservers
```

### With Filtering (Optional Extension)

```sql
select name, srvproduct, provider from master..sysservers where isremote = 0
```

## Expected Output

A table with columns like srvid, name, network_name, status, etc. For example:

| srvid | name | network_name | status |
|-------|------|--------------|--------|
| 0 | dcorp-sql1 | dcorp-sql1.dcorp.com | 68 |

Empty results mean no linked servers are configured.

## Related

- [[procedures/Exploit-MSSQL-Trusted-Linked-Servers]]
- [[commands/execute-query-through-linked-server]]
