---
id: cmd-make-build
data: make build
tags:
  - build
  - go
type: command
output: Compiled binaries in the build directory
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:46.762Z'
verified: false
validated: true
submitted: true
---
---

# make-build

## Command

```bash
make build
```

## Description

Compiles the Cosmos SDK from source using Make and Go, targeting the vulnerable lockup module for POC reproduction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Standard Make target for build | No |

## Examples

### Basic Usage

```bash
make build
```

### Advanced Usage

```bash
make build RACE_DETECTOR_ENABLED=false
```

## Expected Output

Build logs ending with 'Successfully built cosmos-sdk'; binaries in build/.

## Related

- [[Related Procedure: Build-Cosmos-SDK-Binaries]]
