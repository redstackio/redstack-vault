---
data: >-
  select * from oc_appconfig where appid='core' and
  configkey='encryption_enabled';
tags:
  - sql
  - nextcloud
  - verification
type: command
output: null
executor: sql
platforms:
  - Linux
  - Database
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:49.407Z'
id: abe1ed30-08d7-495e-bb1e-38f84e5ffa43
verified: false
validated: true
submitted: true
---
# sql-query-nextcloud-encryption-setting

## Command

```sql
select * from oc_appconfig where appid='core' and configkey='encryption_enabled';
```

## Description

This SQL query retrieves the encryption_enabled configuration from Nextcloud's oc_appconfig table to verify changes post-exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `appid='core'` | Filters to core app configs | Yes |
| `configkey='encryption_enabled'` | Targets the encryption setting | Yes |

## Examples

### Basic Usage

```sql
select * from oc_appconfig where appid='core' and configkey='encryption_enabled';
```

### Advanced Usage

Add LIMIT 1 if multiple rows possible:

```sql
select * from oc_appconfig where appid='core' and configkey='encryption_enabled' LIMIT 1;
```

## Expected Output

Rows like:

| appid | configkey | configvalue |
|-------|------------|-------------|
| core  | encryption_enabled | no |

## Related

- [[procedures/Verify-Encryption-Setting-in-Database]]
