---
id: c99aedf4-0bab-4bcd-b969-01d893f387b1
name: go-get-go-socks5-package
type: command
executor: bash
data: go get github.com/armon/go-socks5
output: null
created_at: '2023-04-06T03:56:22.907818Z'
updated_at: '2023-04-10T20:25:18.397562Z'
platforms:
  - Linux
tags:
  - go
  - dependency
verified: true
validated: true
---

# go-get-go-socks5-package

## Command

```bash
go get github.com/armon/go-socks5
```

## Description

Downloads and installs the go-socks5 library for SOCKS5 proxy support in revsocks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| github.com/armon/go-socks5 | Package URL | Yes |

## Examples

### Basic Usage

```bash
go get github.com/armon/go-socks5
```

## Expected Output

go: downloading github.com/armon/go-socks5 v...
...
go: added github.com/armon/go-socks5

## Related

- [[procedures/Reverse-SOCKS-Proxy-Pivoting]]
