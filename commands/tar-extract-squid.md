---
id: cmd-tar-extract-squid-2023
data: tar zxf SQUID_4_8.tar.gz
tags:
  - extract
type: command
output: Extracted directory squid-SQUID_4_8/
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.967Z'
verified: false
validated: true
submitted: true
---
# tar-extract-squid

## Command

```bash
tar zxf SQUID_4_8.tar.gz
```

## Description

Extracts the gzipped tar archive of Squid source code, creating the source directory for building.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `z` | Decompress gzip | Yes |
| `x` | Extract files | Yes |
| `f` | Specify archive file | Yes |
| `SQUID_4_8.tar.gz` | Input file | Yes |

## Examples

### Basic Usage

```bash
tar zxf SQUID_4_8.tar.gz
```

### Advanced Usage

```bash
tar zxf SQUID_4_8.tar.gz -C /path/to/dir
```

## Expected Output

Files extracted silently; `squid-SQUID_4_8/` directory created with source tree.

## Related

- [[commands/wget-squid-source]]
- [[procedures/Setup-Environment-and-Download-Squid-Source]]
