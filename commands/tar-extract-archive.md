---
type: command
executor: bash
data: tar -xf file.tar
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Unix
tags:
  - extraction
  - tar
verified: true
validated: true
---

# tar-extract-archive

## Command

```bash
tar -xf $_ARCHIVE_FILE
```

## Description

Extracts files from a TAR archive without preserving file permissions or modification times. Use this for basic unpacking in preparation for injection testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -x | Extract files from archive | Yes |
| -f | Specify the archive file | Yes |
| $_ARCHIVE_FILE | Path to the TAR file (e.g., malicious.tar) | Yes |

## Examples

### Basic Usage

```bash
tar -xf sample.tar
```

### Advanced Usage

```bash
tar -xf sample.tar -C /tmp/extracted/
```

## Expected Output

No output on success; files appear in the current directory. Errors if archive is corrupted: "tar: This does not look like a tar archive."

## Related

- [[procedures/TAR-Argument-Injection]]
