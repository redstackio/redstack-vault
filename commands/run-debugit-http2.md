---
id: cmd-run-debugit-001
data: './debugit_test https://http2.example.com'
tags:
  - reproduction
  - http2
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:18.479Z'
verified: false
validated: true
submitted: true
---
# run-debugit-http2

## Command

```bash
./debugit_test https://http2.example.com
```

## Description

Runs the debugit_test to reproduce HTTP/2-specific memory errors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | HTTP/2 target | Yes |

## Examples

### Basic Usage

```bash
./debugit_test https://http2.github.io
```

## Expected Output

ASAN errors in HTTP/2 functions.

## Related

- [[commands/run-curl-cpp-stress-test]]
