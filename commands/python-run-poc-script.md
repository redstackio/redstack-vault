---
id: python-poc-001
data: python3 poc.py
tags:
  - python
  - exploit
  - rce
type: command
output: 'Exploitation success, triggering reverse shell to netcat listener'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.285Z'
verified: false
validated: true
submitted: true
---
# Python Run PoC Script

## Command

```bash
python3 poc.py
```

## Description

Executes the Python script that exploits Kafka Connect by configuring connectors for file upload and SSRF, leading to RCE via Jolokia agent load.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| poc.py | Script file handling API calls and exploit logic | Yes |

## Examples

### Basic Usage

```bash
python3 poc.py
```

### Advanced Usage

```bash
python3 poc.py --target https://connect.example.com
```

## Expected Output

Console logs of API responses, connector status, and agent load success; external shell connection.

## Related

- [[Related Procedure: Execute-PoC-Script-for-Kafka-Connect-RCE]]
