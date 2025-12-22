---
id: a570fbf1-84ca-4cd6-993c-0f4b8f921a77
name: set-gopath-environment
type: command
executor: bash
data: export GOPATH=~/go
output: null
created_at: '2023-04-06T03:56:22.907428Z'
updated_at: '2023-04-10T20:25:18.397562Z'
platforms:
  - Linux
tags:
  - go
  - env
verified: true
validated: true
---

# set-gopath-environment

## Command

```bash
export GOPATH=~/go
```

## Description

Sets the GOPATH environment variable to specify the Go workspace directory for dependency installation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ~/go | Path to Go workspace | Yes |

## Examples

### Basic Usage

```bash
export GOPATH=~/go
```

## Expected Output

No output; verify with `echo $GOPATH`.

## Related

- [[procedures/Reverse-SOCKS-Proxy-Pivoting]]
