---
id: 9519aaa4-05d2-44ee-a8ac-92457a9b7c8b
name: go-get-go-ntlmssp-package
type: command
executor: bash
data: go get github.com/kost/go-ntlmssp
output: null
created_at: '2023-04-06T03:56:22.907863Z'
updated_at: '2023-04-10T20:25:18.397562Z'
platforms:
  - Linux
tags:
  - go
  - dependency
verified: true
validated: true
---

# go-get-go-ntlmssp-package

## Command

```bash
go get github.com/kost/go-ntlmssp
```

## Description

Downloads and installs the go-ntlmssp library for NTLM authentication support in revsocks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| github.com/kost/go-ntlmssp | Package URL | Yes |

## Examples

### Basic Usage

```bash
go get github.com/kost/go-ntlmssp
```

## Expected Output

go: downloading github.com/kost/go-ntlmssp v...
...
go: added github.com/kost/go-ntlmssp

## Related

- [[procedures/Reverse-SOCKS-Proxy-Pivoting]]
