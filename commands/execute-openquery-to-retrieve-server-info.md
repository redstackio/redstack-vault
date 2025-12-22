---
type: command
executor: sql
data: >-
  SELECT * FROM OPENQUERY("$_LINKED_SERVER", 'SELECT * FROM
  master..sysservers');\nSELECT @@version FROM OPENQUERY("$_LINKED_SERVER",
  'SELECT @@version AS version');\n\n-- Chain multiple OPENQUERY for deeper
  traversal\nSELECT @@version FROM OPENQUERY("$_LINKED_SERVER_1", 'SELECT
  @@version FROM OPENQUERY("$_LINKED_SERVER_2", "SELECT @@version AS
  version")');
output: null
platforms:
  - Windows
tags:
  - sql
  - reconnaissance
  - lateral-movement
verified: true
validated: true
---

# execute-openquery-to-retrieve-server-info

## Command

```sql
SELECT * FROM OPENQUERY("$_LINKED_SERVER", 'SELECT * FROM master..sysservers');
SELECT @@version FROM OPENQUERY("$_LINKED_SERVER", 'SELECT @@version AS version');

-- Chain multiple OPENQUERY for deeper traversal
SELECT @@version FROM OPENQUERY("$_LINKED_SERVER_1", 'SELECT @@version FROM OPENQUERY("$_LINKED_SERVER_2", "SELECT @@version AS version")');
```

## Description

This command uses OPENQUERY to pass through SELECT statements to a linked SQL Server, retrieving system server information and version details. It supports chaining for multi-hop queries, useful for initial reconnaissance in lateral movement scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LINKED_SERVER | Name of the linked server (e.g., dcorp-sql1) | Yes |
| $_LINKED_SERVER_1 | First linked server in chain | Yes (for chaining) |
| $_LINKED_SERVER_2 | Second linked server in chain | Yes (for chaining) |

## Examples

### Basic Usage

```sql
SELECT * FROM OPENQUERY("linkedserver", 'SELECT * FROM master..sysservers');
```

### Chained Usage

```sql
SELECT @@version FROM OPENQUERY("link1", 'SELECT @@version FROM OPENQUERY("link2", "SELECT @@version AS version")');
```

## Expected Output

A result set table with columns like SRV_NAME, SRV_PROVIDER, and STATUS for sysservers, or a single column with version string like "Microsoft SQL Server 2019 (RTM-CU18) (KB5006357) - 15.0.4198.2 (X64)" for @@version. Chained queries return nested version info.

## Related

- [[procedures/Execute-Queries-via-Linked-SQL-Servers]]
