---
id: 226d731c-5fe5-4bf4-9bf1-ea355aa3b2ed
name: chain-multiple-openquery-in-mssql
type: command
executor: sql
data: >-
  select version from openquery("$_LINK1",'select version from
  openquery("$_LINK2","select @@version as version")')
output: null
created_at: '2023-04-06T03:56:34.105354+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - lateral-movement
verified: true
validated: true
---

# chain-multiple-openquery-in-mssql

## Command

```sql
select version from openquery("$_LINK1",'select version from openquery("$_LINK2","select @@version as version")')
```

## Description

Chains nested OPENQUERY calls to execute queries across multiple linked servers, allowing traversal of trust chains to gather data from indirectly connected instances.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LINK1 | Name of the first linked server | Yes |
| $_LINK2 | Name of the second (nested) linked server | Yes |

## Examples

### Basic Chaining

```sql
select version from openquery("link1",'select version from openquery("link2","select @@version as version")')
```

## Expected Output

Version string from the deepest server, e.g.,

version
Microsoft SQL Server 2016...

Nested failures may return partial results or errors.

## Related

- [[procedures/Exploit-MSSQL-Trusted-Linked-Servers]]
- [[commands/execute-query-through-linked-server]]
