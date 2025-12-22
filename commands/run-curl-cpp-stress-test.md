---
id: cmd-run-curl-stress-001
data: './curl_test https://http2.example.com 100'
tags:
  - stress-test
  - multi-threaded
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:18.487Z'
verified: false
validated: true
submitted: true
---
# run-curl-cpp-stress-test

## Command

```bash
./curl_test https://http2.example.com 100
```

## Description

Runs the curl_test binary to perform multi-threaded HTTP requests, stressing connection reuse in libcurl.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target HTTP/2 endpoint | Yes |
| Threads | Number of threads (default 100) | No |

## Examples

### Basic Usage

```bash
./curl_test https://http2.example.com 50
```

### Advanced Usage

Adjust requests per thread via code modification.

## Expected Output

Thread logs and potential ASAN errors during execution.

## Related

- [[commands/run-debugit-http2]]
