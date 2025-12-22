---
id: cmd-uuid-3
data: python exp.py
tags:
  - automation
  - scanning
  - python
type: command
output: |-
  PORT: 25 OPEN
  PORT: 80 OPEN
  PORT: 443 OPEN
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.332Z'
verified: false
validated: true
submitted: true
---
# python-ssrf-port-scanner

## Command

```bash
python exp.py
```

## Description

Executes a Python script exp.py that automates SSRF port scanning by sending timed requests with gopher payloads to detect open ports based on timeouts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| exp.py | Path to the scanning script | Yes |

## Examples

### Basic Usage

```bash
python exp.py
```

### Advanced Usage

```bash
python exp.py --ports 1-1000 --timeout 3
```

## Expected Output

PORT: 25 OPEN
PORT: 80 OPEN
PORT: 443 OPEN

## Related

- [[Related Procedure: Automate-Port-Scanning-with-Python-Script]]
