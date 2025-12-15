---
data: openssl version -a
tags:
  - discovery
  - openssl
type: command
output: null
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.492Z'
id: c45ad980-fe66-4563-b220-5ece391426e9
verified: false
validated: true
submitted: true
---
# check-openssl-version

## Command

```cmd
openssl version -a
```

## Description

Retrieves detailed OpenSSL version information, including build config and OPENSSLDIR, to identify vulnerabilities like writable default paths on Windows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| version | Displays version info | No |
| -a | All details (built for, OPENSSLDIR) | Yes |

## Examples

### Basic Usage

```cmd
openssl version -a
```

### Advanced Usage

```cmd
openssl version -a | findstr OPENSSLDIR
```

## Expected Output

OpenSSL 1.1.1k  25 Mar 2021
built on: reproducible build, date unspecified
platform: mingw64
OPENSSLDIR: "C:/usr/local/ssl"

## Related

- [[Related Procedure]]
