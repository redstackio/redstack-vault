---
id: 6f6a8c08-abda-4d29-a50c-d7915a1b4c46
name: execute-query-through-linked-server
type: command
executor: sql
data: |-
  select * from openquery("dcorp-sql1", 'select * from master..sysservers')
  select version from openquery("linkedserver", 'select @@version as version');
output: null
created_at: '2023-04-06T03:56:34.105254+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - lateral-movement
verified: true
validated: true
---

# execute-query-through-linked-server

## Command

```sql
select * from openquery("$_LINKED_SERVER", 'select * from master..sysservers')
select version from openquery("$_LINKED_SERVER", 'select @@version as version');
```

## Description

Executes pass-through queries on a linked MSSQL server to retrieve information like linked servers or version details, verifying and exploiting the trust relationship.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LINKED_SERVER | Name of the linked server (e.g., dcorp-sql1) | Yes |

## Examples

### Basic Usage

```sql
select * from openquery("dcorp-sql1", 'select * from master..sysservers')
```

### Version Check

```sql
select version from openquery("linkedserver", 'select @@version as version');
```

## Expected Output

Results from the remote query, e.g., for version:

version
Microsoft SQL Server 2019 (RTM-CU12) (KB5023695) - 15.0.2101.7 (X64)

Errors if link is invalid or permissions insufficient.

## Related

- [[procedures/Exploit-MSSQL-Trusted-Linked-Servers]]
- [[commands/find-linked-servers-in-mssql]]
