---
type: command
executor: bash
data: go get -v github.com/jpillora/chisel
tags:
  - installation
  - chisel
platforms:
  - Linux
  - macOS
verified: true
validated: true
---

# chisel-install-via-go

## Command

```bash
go get -v github.com/jpillora/chisel
```

## Description

This command installs the Chisel tunneling tool by fetching and building it from the official GitHub repository using Go's get functionality. It places the binary in your GOPATH/bin directory, ready for use in network pivoting scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output during build | No |
| `github.com/jpillora/chisel` | Repository URL to fetch | Yes |

## Examples

### Basic Usage

```bash
go get -v github.com/jpillora/chisel
```

### Advanced Usage

For a specific version, use `go get github.com/jpillora/chisel@version` after checking tags.

## Expected Output

Building output showing download progress, compilation, and success message like "github.com/jpillora/chisel". The binary is now executable as `chisel`.

## Related

- [[procedures/chisel-port-forwarding-and-socks-proxy-network-pivoting]]
- [[tools/Chisel]]
