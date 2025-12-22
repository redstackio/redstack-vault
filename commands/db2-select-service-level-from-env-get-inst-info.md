---
id: a02dbc20-06b1-436f-a82d-b2f3e04f3624
name: db2-select-service-level-from-env-get-inst-info
type: command
executor: sql
data: select service_level from table(sysproc.env_get_inst_info()) as instanceinfo
output: null
created_at: '2023-04-06T03:56:32.535738+00:00'
updated_at: '2023-04-10T20:21:57.272196+00:00'
platforms:
  - Database
  - DB2
tags:
  - db2
  - service-level
  - recon
verified: true
validated: true
---

# db2-select-service-level-from-env-get-inst-info

## Command

```sql
select service_level from table(sysproc.env_get_inst_info()) as instanceinfo
```

## Description

This SQL command invokes the SYSPROC.ENV_GET_INST_INFO() table function in DB2 to extract the service level of the database instance, indicating applied updates or fix packs. Ideal for pinpointing patch status during discovery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Table function call with alias; no inputs | N/A |

## Examples

### Basic Usage

```sql
select service_level from table(sysproc.env_get_inst_info()) as instanceinfo;
```

## Expected Output

```
SERVICE_LEVEL
-------------
SF31M
```

Output shows a string like 'SF31M' representing the fix pack level (e.g., Special Fix 31 Modification).

## Related

- [[procedures/Extract-DB2-Database-Version-Information]]
