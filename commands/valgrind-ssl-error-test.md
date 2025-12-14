---
id: cmd-021
data: >-
  valgrind --tool=memcheck --leak-check=full ./src/curl -v --cert
  /nonexistent/cert.pem https://httpbin.org/get 2>&1 | tee ssl_error_test.log
tags:
  - test
  - valgrind
  - error-handling
type: command
output: Valgrind report with no errors
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:27.974Z'
verified: false
validated: true
submitted: true
---
# valgrind-ssl-error-test

## Command

```bash
valgrind --tool=memcheck --leak-check=full ./src/curl -v --cert /nonexistent/cert.pem https://httpbin.org/get 2>&1 | tee ssl_error_test.log
```

## Description

Tests WolfSSL error path with invalid cert.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--cert /nonexistent/cert.pem` | Bad cert | Yes |

## Examples

### Basic Usage

```bash
valgrind ./src/curl --cert bad.pem https://site
```

## Expected Output

Error handling without leaks.

## Related

- [[procedures/Dynamic-Memory-Testing-of-cURL-with-Valgrind]]
