---
id: f81f0e2e-0579-4a88-9c22-e34332b58395
name: ligolo-clone-and-install-dependencies
type: command
executor: bash
data: |
  cd `go env GOPATH`/src
  git clone https://github.com/sysdream/ligolo
  cd ligolo
  make dep
output: null
created_at: '2023-04-06T03:56:22.792060+00:00'
updated_at: '2023-04-10T20:25:12.831311+00:00'
platforms:
  - Linux
tags:
  - setup
  - dependencies
verified: true
validated: true
---

# Ligolo Clone and Install Dependencies

## Command

```bash
cd `go env GOPATH`/src
git clone https://github.com/sysdream/ligolo
cd ligolo
make dep
```

## Description

This multi-line command sets up the Ligolo development environment by navigating to the Go source path, cloning the official repository, and installing module dependencies. Use this as the initial step in preparing Ligolo for building tunneling agents and proxies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `go env GOPATH` | Environment variable pointing to Go workspace (backticks execute it) | Yes |
| https://github.com/sysdream/ligolo | Repository URL for cloning | Yes |

## Examples

### Basic Usage

```bash
cd `go env GOPATH`/src
git clone https://github.com/sysdream/ligolo
cd ligolo
make dep
```

### Advanced Usage

If GOPATH is not set, export it first: `export GOPATH=$HOME/go`, then run the command.

## Expected Output

Cloning into 'ligolo'...
remote: Enumerating objects: ..., done.
remote: Total ... (delta ...), reused ... (delta ...), pack-reused 0
Receiving objects: 100% (...), ... KiB | ... KiB/s, done.
Resolving deltas: 100% (...), completed with ... local objects.
make dep
 go mod download
 go: downloading github.com/... v1.0.0
 ... (dependency list)

Success is confirmed by the presence of the 'ligolo' directory with 'go.mod' file.

## Related

- [[procedures/setup-ligolo-for-reverse-tunneling]]
- [[tools/ligolo]]
