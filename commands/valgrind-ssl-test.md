---
id: cmd-020
data: >-
  valgrind --tool=memcheck --leak-check=full ./src/curl -v
  https://httpbin.org/get 2>&1 | tee ssl_test.log
tags:
  - test
  - valgrind
  - ssl
type: command
output: Valgrind report with no errors
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:27.977Z'
verified: false
validated: true
submitted: true
---
# valgrind-ssl-test

## Command

```bash
valgrind --tool=memcheck --leak-check=full ./src/curl -v https://httpbin.org/get 2>&1 | tee ssl_test.log
```

## Description

Tests SSL backend with Valgrind.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--leak-check=full` | Full checks | Yes |

## Examples

### Basic Usage

```bash
valgrind ./src/curl https://example.com
```

## Expected Output

No invalid reads.

## Related

- [[commands/valgrind-ssl-error-test]]
