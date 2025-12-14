---
data: 'ab -n 30 -c 30 http://localhost:8090/download'
tags:
  - load-testing
  - dos
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.231Z'
id: 5c90417d-0443-4c70-ba0a-f5e3dd52b4a3
verified: false
validated: true
submitted: true
---
# ab-load-test-concurrent-requests

## Command

```bash
ab -n 30 -c 30 http://localhost:8090/download
```

## Description

This command uses Apache Benchmark (ab) to perform load testing by sending 30 concurrent requests (30 total) to a local HTTP endpoint, simulating DoS exploitation to trigger out-of-memory conditions on a server that loads large files into memory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n 30` | Total number of requests to perform | Yes |
| `-c 30` | Number of concurrent requests | Yes |
| `http://localhost:8090/download` | Target URL for the benchmark | Yes |

## Examples

### Basic Usage

```bash
ab -n 30 -c 30 http://localhost:8090/download
```

### Advanced Usage

```bash
ab -n 100 -c 50 -k http://target.com/endpoint
```

> Adds keep-alive (-k) for more realistic concurrency.

## Expected Output

Benchmark results including server response times, transfer rates, and failed requests; in vulnerable setups, expect high failure rates and server OOM (e.g., process crash observed via logs or oom.png screenshot).

## Related

- [[Related Procedure: Simulate-DoS-with-Local-Go-Server-and-Load-Testing]]
