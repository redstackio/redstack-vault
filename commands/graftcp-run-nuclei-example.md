---
id: 75882d6a-953d-44af-abf4-6cc22329f0b6
name: graftcp-run-nuclei-example
type: command
executor: bash
data: graftcp ./nuclei -u $_TARGET_URL
output: null
created_at: '2023-04-06T03:56:22.550220+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - graftcp
  - nuclei
  - proxy
  - scan
verified: true
validated: true
---

# graftcp-run-nuclei-example

## Command

```bash
graftcp ./nuclei -u $_TARGET_URL
```

## Description

Runs the Nuclei scanner prefixed with Graftcp to proxify its HTTP requests through the established SOCKS5 chain for internal network scanning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| graftcp | Proxifier prefix (assumes graftcp-local running) | Yes |
| ./nuclei | Path to Nuclei binary | Yes |
| -u $_TARGET_URL | Target URL to scan | Yes |

## Examples

### Basic Usage

```bash
graftcp ./nuclei -u http://172.16.1.24
```

### Advanced Usage

```bash
graftcp ./nuclei -u http://internal.target -t templates/ -o results.txt
```

## Expected Output

Nuclei's scan results (e.g., "[INF] Sending GET /") with proxied traffic. Graftcp logs show routed connections. Errors if proxy fails.

## Related

- [[procedures/Proxify-Go-Application-with-Graftcp]]
- [[tools/Nuclei]]
