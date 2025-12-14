---
id: cmd-010
data: >-
  ./configure --enable-debug --enable-maintainer-mode --enable-websockets
  --with-openssl --disable-shared --enable-static
tags:
  - build
  - config
type: command
output: Configuration summary
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.054Z'
verified: false
validated: true
submitted: true
---
# configure-curl-build

## Command

```bash
./configure --enable-debug --enable-maintainer-mode --enable-websockets --with-openssl --disable-shared --enable-static
```

## Description

Configures cURL build with debug, WebSockets, OpenSSL, and static libraries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--enable-debug` | Debug mode | Yes |
| `--enable-websockets` | WebSocket support | Yes |
| `--with-openssl` | Use OpenSSL | Yes |

## Examples

### Basic Usage

```bash
./configure --enable-debug --with-openssl
```

## Expected Output

Configuration summary with enabled features.

## Related

- [[commands/make-parallel-build]]
