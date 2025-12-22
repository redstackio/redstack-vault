---
id: cmd-asan-log-001
data: >-
  ASAN_OPTIONS=abort_on_error=1:log_path=asan_log.%p ./curl_test
  https://http2.example.com 50
tags:
  - asan
  - logging
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:18.485Z'
verified: false
validated: true
submitted: true
---
# run-with-asan-log

## Command

```bash
ASAN_OPTIONS=abort_on_error=1:log_path=asan_log.%p ./curl_test https://http2.example.com 50
```

## Description

Executes the test with ASAN configured to log errors to files for detailed analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `abort_on_error=1` | Halts on first error | Yes |
| `log_path=asan_log.%p` | Logs to per-process files | Yes |

## Examples

### Basic Usage

```bash
ASAN_OPTIONS=verbosity=2 ./curl_test ...
```

## Expected Output

ASAN log files with error details, stack traces.

## Related

- [[commands/run-curl-cpp-stress-test]]
