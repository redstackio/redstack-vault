---
data: >-
  wget -q https://curl.se/download/curl-8.16.0.tar.gz && tar -xzf
  curl-8.16.0.tar.gz
tags:
  - download
  - extract
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:19.115Z'
id: b409d359-6f16-48a8-bc3d-43185ec277f3
verified: false
validated: true
submitted: true
---
# wget-download-curl-source

## Command

```bash
wget -q https://curl.se/download/curl-8.16.0.tar.gz && tar -xzf curl-8.16.0.tar.gz
```

## Description

Downloads the curl 8.16.0 source tarball quietly and extracts it using tar, preparing the build directory for compilation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-q` | Quiet mode for wget, suppresses output | Yes |
| URL | Source download URL | Yes |
| `-xzf` | Extract tar.gz: x=extract, z=gzip, f=file | Yes |

## Examples

### Basic Usage

```bash
wget -q https://curl.se/download/curl-8.16.0.tar.gz && tar -xzf curl-8.16.0.tar.gz
```

### Advanced Usage

```bash
wget -qO- https://curl.se/download/curl-8.16.0.tar.gz | tar -xzf -
```

## Expected Output

Source code extracted to curl-8.16.0 directory; no console output due to -q.

## Related

- [[commands/configure-curl-build]]
