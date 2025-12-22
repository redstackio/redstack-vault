---
id: c0c787aa-4083-4610-9ceb-666e1e4d0d3b
name: go-get-yamux-package
type: command
executor: bash
data: go get github.com/hashicorp/yamux
output: null
created_at: '2023-04-06T03:56:22.907747Z'
updated_at: '2023-04-10T20:25:18.397562Z'
platforms:
  - Linux
tags:
  - go
  - dependency
verified: true
validated: true
---

# go-get-yamux-package

## Command

```bash
go get github.com/hashicorp/yamux
```

## Description

Downloads and installs the yamux multiplexing library dependency for revsocks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| github.com/hashicorp/yamux | Package URL | Yes |

## Examples

### Basic Usage

```bash
go get github.com/hashicorp/yamux
```

## Expected Output

go: downloading github.com/hashicorp/yamux v0.0.0-...
...
go: added github.com/hashicorp/yamux

## Related

- [[procedures/Reverse-SOCKS-Proxy-Pivoting]]
