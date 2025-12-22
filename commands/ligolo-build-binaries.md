---
id: 6dea59bc-5e17-48a3-bcce-0579bf2bc9d6
name: ligolo-build-binaries
type: command
executor: bash
data: make build-all
output: null
created_at: '2023-04-06T03:56:22.792191+00:00'
updated_at: '2023-04-10T20:25:12.831311+00:00'
platforms:
  - Linux
tags:
  - build
  - compile
verified: true
validated: true
---

# Ligolo Build Binaries

## Command

```bash
make build-all
```

## Description

This command compiles all Ligolo components, including the proxy server and agent binaries for multiple platforms (Linux, Windows, etc.). It cross-compiles where possible, producing standalone executables for deployment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (None) | Builds all targets by default | N/A |

## Examples

### Basic Usage

```bash
make build-all
```

### Advanced Usage

For specific target: Edit Makefile or use `go build -o bin/agent-linux-amd64 agent/main.go` manually.

## Expected Output

go build -o bin/proxy proxy/main.go
 go build -o bin/agent-linux-amd64 agent/main.go
 go build -o bin/agent-windows-amd64.exe agent/main.go
 ... (build logs for each binary)

Binaries appear in the 'bin' directory; no errors indicate success.

## Related

- [[procedures/setup-ligolo-for-reverse-tunneling]]
- [[tools/ligolo]]
