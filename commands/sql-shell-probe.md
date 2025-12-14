---
id: cmd-uuid-7
data: >-
  SELECT user(); SELECT @@version; SELECT @@basedir; SELECT @@port; SELECT
  @@hostname;
tags:
  - sqli
  - probe
type: command
output: >-
  System variables like user 'ntmsender'@'localhost', version '5.6.36', hostname
  '███████'
executor: sql
platforms:
  - Web
  - MySQL
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.933Z'
verified: false
validated: true
submitted: true
---
# SQL Shell Probe

## Command

```bash
# In sqlmap --sql-shell:
SELECT user(); SELECT @@version; SELECT @@basedir; SELECT @@port; SELECT @@hostname;
```

## Description

Interactive SQL queries in sqlmap shell to extract MySQL system details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| SELECT user() | Current user | No |
| SELECT @@version | DB version | No |
| SELECT @@basedir | Base directory | No |
| SELECT @@port | Listening port | No |
| SELECT @@hostname | Server hostname | No |

## Examples

### Basic Usage

```bash
# As above
```

## Expected Output

Query results revealing system info for shared access confirmation.

## Related

- [[procedures/Probe-Database-Details-Shared-Access]]
