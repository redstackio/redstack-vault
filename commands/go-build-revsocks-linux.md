---
id: 840adc9a-5bbd-446e-bfd2-9f96c113e821
name: go-build-revsocks-linux
type: command
executor: bash
data: go build -ldflags="-s -w"
output: null
created_at: '2023-04-06T03:56:22.907639Z'
updated_at: '2023-04-10T20:25:18.397562Z'
platforms:
  - Linux
tags:
  - build
  - go
verified: true
validated: true
---

# go-build-revsocks-linux

## Command

```bash
go build -ldflags="-s -w"
```

## Description

Compiles the revsocks source into a Linux executable with symbol stripping for reduced size.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ldflags="-s -w" | Strip debug info and symbols | No |

## Examples

### Basic Usage

```bash
go build -ldflags="-s -w"
```

## Expected Output

No output on success; generates `revsocks` binary.

## Related

- [[procedures/Reverse-SOCKS-Proxy-Pivoting]]
