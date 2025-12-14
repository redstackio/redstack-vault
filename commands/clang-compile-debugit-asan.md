---
id: cmd-clang-debugit-001
data: clang++ -g -fsanitize=address debugit.cpp -o debugit_test -lcurl -lpthread
tags:
  - compilation
  - debug
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:18.483Z'
verified: false
validated: true
submitted: true
---
# clang-compile-debugit-asan

## Command

```bash
clang++ -g -fsanitize=address debugit.cpp -o debugit_test -lcurl -lpthread
```

## Description

Compiles debugit.cpp for HTTP/2-specific reproduction with ASAN and threading support.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-lpthread` | Enables multi-threading | Yes |

## Examples

### Basic Usage

```bash
clang++ -g -fsanitize=address debugit.cpp -o debugit_test -lcurl
```

## Expected Output

debugit_test binary ready.

## Related

- [[commands/clang-compile-curl-cpp-asan]]
