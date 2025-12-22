---
id: cmd-637840-001
data: |
  |
    ./dlopen.sh
tags:
  - path-traversal
  - poc
  - rce
type: command
output: init and fini printed on successful load
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.588Z'
verified: false
validated: true
submitted: true
---
# execute-dlopen-sh

## Command

```bash
./dlopen.sh
```

## Description

Proof-of-concept script to demonstrate path traversal leading to dlopen of arbitrary file in MariaDB client on Debian Buster, triggering code execution via init/fini functions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Script runs with predefined malicious path | No |

## Examples

### Basic Usage

```bash
./dlopen.sh
```

### Advanced Usage

Adjust script for different paths:

```bash
# Edit dlopen.sh to change traversal depth, then ./dlopen.sh
```

## Expected Output

init and fini messages printed if library loads successfully, indicating code execution.

## Related

- [[procedures/Trigger-dlopen-via-Malicious-Server-Connection]]
- [[procedures/Reproduce-on-Debian-Buster-Setup]]
