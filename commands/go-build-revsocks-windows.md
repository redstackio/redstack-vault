---
id: bb452153-9c11-461f-aea4-fe6d1635214a
name: go-build-revsocks-windows
type: command
executor: bash
data: GOOS=windows GOARCH=amd64 go build -ldflags="-s -w"
output: null
created_at: '2023-04-06T03:56:22.907951Z'
updated_at: '2023-04-10T20:25:18.397562Z'
platforms:
  - Windows
tags:
  - build
  - go
  - cross-compile
verified: true
validated: true
---

# go-build-revsocks-windows

## Command

```bash
GOOS=windows GOARCH=amd64 go build -ldflags="-s -w"
```

## Description

Cross-compiles revsocks for Windows AMD64 with optimizations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| GOOS=windows | Target OS | Yes |
| GOARCH=amd64 | Target architecture | Yes |
| -ldflags="-s -w" | Strip symbols | No |

## Examples

### Basic Usage

```bash
GOOS=windows GOARCH=amd64 go build -ldflags="-s -w"
```

## Expected Output

No output; generates `revsocks.exe`.

## Related

- [[procedures/Reverse-SOCKS-Proxy-Pivoting]]
