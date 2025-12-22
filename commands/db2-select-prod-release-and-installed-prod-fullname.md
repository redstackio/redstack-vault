---
id: ab729622-403c-40d1-b98b-7b7851aed442
name: db2-select-prod-release-and-installed-prod-fullname
type: command
executor: sql
data: >-
  select prod_release,installed_prod_fullname from
  table(sysproc.env_get_prod_info()) as productinfo
output: null
created_at: '2023-04-06T03:56:32.535829+00:00'
updated_at: '2023-04-10T20:21:57.272196+00:00'
platforms:
  - Database
  - DB2
tags:
  - db2
  - product-info
  - recon
verified: true
validated: true
---

# db2-select-prod-release-and-installed-prod-fullname

## Command

```sql
select prod_release, installed_prod_fullname from table(sysproc.env_get_prod_info()) as productinfo;
```

## Description

This SQL command calls the SYSPROC.ENV_GET_PROD_INFO() table function in DB2 to fetch the product release level and the full name of the installed DB2 product, helping identify the edition and release for targeted exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Table function with alias for output | N/A |

## Examples

### Basic Usage

```sql
select prod_release, installed_prod_fullname from table(sysproc.env_get_prod_info()) as productinfo;
```

## Expected Output

```
PROD_RELEASE                INSTALLED_PROD_FULLNAME
--------------------------- ----------------------------------------------------------------
11.5                        IBM DB2 Express-C 11.5 for Linux x86-64
```

Displays release like '11.5' and a descriptive name including edition and platform.

## Related

- [[procedures/Extract-DB2-Database-Version-Information]]
