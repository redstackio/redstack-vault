---
data: gcc -o curl_race_test curl_race_demo.c -lcurl -lpthread
tags:
  - compilation
  - c
type: command
executor: bash
platforms:
  - Linux
  - Unix-like
id: 76ca4f4e-2b18-42e4-8426-b5fbe658a48f
created_at: '2025-12-14T17:24:18.805Z'
updated_at: '2025-12-14T17:24:18.805Z'
verified: false
validated: true
submitted: true
---
# gcc-compile-test

## Command

```bash
gcc -o curl_race_test curl_race_demo.c -lcurl -lpthread
```

## Description

Compiles a C source file demonstrating the libcurl race condition, linking against libcurl for HTTP operations and pthread for multi-threading. Use this to build the test binary before execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-o curl_race_test` | Specifies output binary name | Yes |
| `curl_race_demo.c` | Input source file | Yes |
| `-lcurl` | Links libcurl library | Yes |
| `-lpthread` | Links pthread for threading | Yes |

## Examples

### Basic Usage

```bash
gcc -o curl_race_test curl_race_demo.c -lcurl -lpthread
```

### Advanced Usage

```bash
gcc -Wall -g -o curl_race_test curl_race_demo.c -lcurl -lpthread
```

## Expected Output

No output on success; generates executable `curl_race_test`. Errors if libraries missing, e.g., "ld: cannot find -lcurl".

## Related

- [[Related Procedure|procedures/Trigger-libcurl-Resolver-Race-Condition]]
