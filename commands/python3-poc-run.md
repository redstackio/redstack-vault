---
data: python3 poc.py
tags:
  - python
  - poc
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:19.014Z'
id: a8ba7c8c-26ad-4cf1-a339-7d28cadfb4b8
verified: false
validated: true
submitted: true
---
# python3-poc-run

## Command

```bash
python3 poc.py
```

## Description

Runs the full PoC script to orchestrate compilation, certificate generation, server start, and the TOCTOU attack execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
python3 poc.py
```

### Advanced Usage

```bash
python3 poc.py --debug
```

## Expected Output

Script output showing stages: compilation success, certs generated, server started, attack executed, vulnerability confirmed.

## Related

- [[procedures/Execute-TOCTOU-CA-Swap-and-Curl-Requests]]
