---
id: c3g4h5i6-j7k8-9013-ghij-7890123456
data: ls -la /tmp/poc_file
tags:
  - verification
  - filesystem
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:26:27.872Z'
verified: false
validated: true
submitted: true
---
# ls-verify-file

## Command

```bash
ls -la /tmp/poc_file
```

## Description

Lists file details in a target directory to verify presence after exploitation, such as post-ZIP extraction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /tmp/poc_file | Path to check | Yes |

## Examples

### Basic Usage

```bash
ls -la /tmp/poc_file
```

### Advanced Usage

```bash
ls -la /tmp/ | grep poc
```

## Expected Output

-rw-r--r-- 1 www-data www-data 45 Oct 1 12:00 /tmp/poc_file

## Related

- [[Related Procedure: Verify-Arbitrary-File-Placement]]
