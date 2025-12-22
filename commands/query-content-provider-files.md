---
data: 'content query --uri content://org.nextcloud/file'
tags:
  - content-provider
  - file-discovery
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:40.060Z'
id: 01252045-f622-4213-9569-7bd028501586
verified: false
validated: true
submitted: true
---
# query-content-provider-files

## Command

```bash
content query --uri content://org.nextcloud/file
```

## Description

Queries the Nextcloud file Content Provider to list synced file metadata, including names.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --uri | Provider URI for files | Yes |

## Examples

### Basic Usage

```bash
content query --uri content://org.nextcloud/file
```

## Expected Output

Rows with file details, e.g., name=/Documents/file.txt

## Related

- [[commands/query-content-provider-directory]]
