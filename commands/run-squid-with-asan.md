---
id: cmd-uuid-3
data: ASAN_OPTIONS="abort_on_error=true" ./sbin/squid --foreground -d 100
tags:
  - run
  - debug
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.212Z'
verified: false
validated: true
submitted: true
---
# run-squid-with-asan

## Command

```bash
ASAN_OPTIONS="abort_on_error=true" ./sbin/squid --foreground -d 100
```

## Description

Launches Squid in foreground with ASAN options to abort on memory errors and high debug level for logging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| abort_on_error=true | ASAN aborts on detected issues | Yes |
| --foreground | Run in terminal | Yes |
| -d 100 | Debug verbosity level | Yes |

## Examples

### Basic Usage

```bash
ASAN_OPTIONS="abort_on_error=true" ./sbin/squid --foreground -d 100
```

### Advanced Usage

```bash
export ASAN_OPTIONS="abort_on_error=true"; ./sbin/squid --foreground -d 100 -f squid.conf
```

## Expected Output

Squid startup logs; ready for requests, ASAN active.

## Related

- [[Related Procedure: Build-and-Run-Squid-with-AddressSanitizer]]
