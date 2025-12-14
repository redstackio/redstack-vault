---
data: >-
  ./configure --with-openssl --disable-shared --enable-debug
  --enable-maintainer-mode
tags:
  - configure
  - build
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.037Z'
id: 7f84823b-5fd9-44f1-94a1-7a20054fb5fa
verified: false
validated: true
submitted: true
---
# configure-curl

## Command

```bash
./configure --with-openssl --disable-shared --enable-debug --enable-maintainer-mode
```

## Description

Configures curl build with OpenSSL, static libs, debug, and maintainer options for vulnerability reproduction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --with-openssl | Enable OpenSSL | Yes |
| --disable-shared | Static build | Yes |
| --enable-debug | Debug symbols | Yes |
| --enable-maintainer-mode | Maintainer features | Yes |

## Examples

### Basic Usage

```bash
./configure --with-openssl --disable-shared --enable-debug --enable-maintainer-mode
```

## Expected Output

Configuration summary, 'now type make'.

## Related

- [[commands/make-parallel]]
- [[procedures/Clone-and-Build-curl-with-AddressSanitizer]]
