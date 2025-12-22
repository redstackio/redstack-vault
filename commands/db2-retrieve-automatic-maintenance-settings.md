---
id: 721f2334-9bc9-426d-b48b-b6c2b1b1ce64
name: db2-retrieve-automatic-maintenance-settings
type: command
executor: sql
data: >-
  select dbpartitionnum, name, value from sysibmadm.dbcfg where name like
  'auto_%';
output: null
created_at: '2023-04-06T03:56:33.204927+00:00'
updated_at: '2023-04-10T20:22:01.198376+00:00'
platforms:
  - Linux
tags:
  - database
  - db2
  - configuration
verified: true
validated: true
---

# db2-retrieve-automatic-maintenance-settings

## Command

```sql
select dbpartitionnum, name, value from sysibmadm.dbcfg where name like 'auto_%';
```

## Description

This SQL command retrieves automatic maintenance settings (parameters starting with 'auto_') from the in-memory database configuration for all partitions in a DB2 environment. Use it during discovery to identify maintenance policies that may indicate system behavior or vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The query uses a fixed LIKE pattern for 'auto_%' names; no user parameters. | N/A |

## Examples

### Basic Usage

```sql
select dbpartitionnum, name, value from sysibmadm.dbcfg where name like 'auto_%';
```

### Advanced Usage

In a multi-partition setup, pipe to grep for specific params:

```sql
select dbpartitionnum, name, value from sysibmadm.dbcfg where name like 'auto_%' | grep 'auto_reorg';
```

## Expected Output

A table listing partition numbers, parameter names (e.g., AUTO_REORG, AUTO_RUNSTATS), and their values (e.g., ON, OFF, or specific thresholds). Example:

DBPARTITIONNUM | NAME          | VALUE
0               | AUTO_REORG    | ON
1               | AUTO_MAINT    | OFF

Success is indicated by returned rows without privilege errors.

## Related

- [[procedures/DB2-Configuration-Parameters-Retrieval]]
