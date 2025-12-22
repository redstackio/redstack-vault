---
data: 'content query --uri content://org.nextcloud/dir/[dir ID]'
tags:
  - content-provider
  - directory-discovery
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:40.057Z'
id: c00b1e16-098e-4932-ac79-c17ba0eb8159
verified: false
validated: true
submitted: true
---
# query-content-provider-directory

## Command

```bash
content query --uri content://org.nextcloud/dir/[dir ID]
```

## Description

Queries a specific Nextcloud directory Content Provider using its ID to list folder contents.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --uri | URI with dir ID (e.g., content://org.nextcloud/dir/123) | Yes |

## Examples

### Basic Usage

```bash
content query --uri content://org.nextcloud/dir/123
```

## Expected Output

Directory entries, e.g., subfolder names and IDs.

## Related

- [[commands/query-content-provider-files]]
