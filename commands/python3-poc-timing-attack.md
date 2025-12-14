---
data: 'python3 poc_timing_attack.py http://localhost:8080/protected'
tags:
  - timing-attack
  - poc
type: command
output: >-
  Timing results like 'Testing algorithm: MD5 - 963236.5 ns' and confirmation
  'VULNERABILITY CONFIRMED: Timing attack possible The server likely uses
  algorithm: MD5'
executor: bash
platforms:
  - Linux
created_at: '2024-12-14T00:00:00Z'
updated_at: '2025-12-14T17:31:30.961Z'
id: 9ee7586f-4505-4cb1-b8bf-84745b7d3d77
verified: false
validated: true
submitted: true
---
# python3-poc-timing-attack

## Command

```bash
python3 poc_timing_attack.py http://localhost:8080/protected
```

## Description

Executes a Python PoC script to perform timing measurements on Digest Authentication responses using curl, testing different algorithms and detecting vulnerabilities via response time analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://localhost:8080/protected` | Target URL for the protected resource | Yes |

## Examples

### Basic Usage

```bash
python3 poc_timing_attack.py http://localhost:8080/protected
```

### Advanced Usage

```bash
python3 poc_timing_attack.py https://example.com/secure --iterations 10
```

## Expected Output

Detailed timing logs for each algorithm and a summary confirming the vulnerability and likely supported algorithm.

## Related

- [[Related Procedure: Execute-Timing-Attack-PoC]]
