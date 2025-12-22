---
id: c4981e8f-17e8-445d-98d2-a897e2c025ef
name: db2-select-service-level-and-bld-level-from-env-inst-info
type: command
executor: sql
data: 'select service_level,bld_level from sysibmadm.env_inst_info'
output: null
created_at: '2023-04-06T03:56:32.535901+00:00'
updated_at: '2023-04-10T20:21:57.272196+00:00'
platforms:
  - Database
  - DB2
tags:
  - db2
  - build-level
  - recon
verified: true
validated: true
---

# db2-select-service-level-and-bld-level-from-env-inst-info

## Command

```sql
select service_level, bld_level from sysibmadm.env_inst_info;
```

## Description

This SQL command queries the SYSIBMADM.ENV_INST_INFO administrative view in DB2 to obtain the service level and build level of the instance, providing detailed update and compilation information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Direct SELECT from admin view | N/A |

## Examples

### Basic Usage

```sql
select service_level, bld_level from sysibmadm.env_inst_info;
```

## Expected Output

```
SERVICE_LEVEL               BLD_LEVEL
---------------------------- ----------
SF31M                       s1908101300
```

Returns service level (e.g., 'SF31M') and build timestamp (e.g., 's1908101300' for 2019-08-10).

## Related

- [[procedures/Extract-DB2-Database-Version-Information]]
