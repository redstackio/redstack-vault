---
data: 'gzip -dc #{@archive_path} | wc -c'
tags:
  - validation
type: command
executor: bash
platforms:
  - Linux
id: f2a175d1-6567-42bd-ba2b-a52276f7566e
created_at: '2025-12-11T03:48:06.007Z'
updated_at: '2025-12-11T03:48:06.007Z'
verified: false
validated: true
submitted: true
---
# gzip-decompress-wc

## Command

```bash
gzip -dc #{@archive_path} | wc -c
```

## Description

Decompresses an archive and counts the bytes to validate size before extraction, vulnerable to injection if path is unsanitized.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `@archive_path` | Path to the archive file | Yes |

## Examples

### Basic Usage

```bash
gzip -dc /path/to/archive.gz | wc -c
```

## Expected Output

Decompressed size in bytes

## Related

- [[DecompressedArchiveSizeValidator]]
