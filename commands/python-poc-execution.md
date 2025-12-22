---
id: cmd-python-poc
data: python3 poc.py
tags:
  - rce
  - poc
  - exploitation
type: command
output: HTTP 200 OK or error; RCE triggered (check listener for shell)
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.416Z'
verified: false
validated: true
submitted: true
---
# python-poc-execution

## Command

```bash
python3 poc.py
```

## Description

Executes a Python script (poc.py) that sends a malicious HTTP GET request to the Flink API /jars/{jar_id}/plan endpoint, exploiting it for RCE via JavaScript gadget to establish a reverse shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Script must be pre-configured with host, jar_id, etc. | Yes |

## Examples

### Basic Usage

```bash
python3 poc.py
```

### Advanced Usage

```bash
python3 poc.py --debug
```
(If script supports --debug for verbose HTTP output.)

## Expected Output

Script outputs HTTP request details and response status. Success: No errors, reverse shell appears in netcat listener. Flink instance crashes post-execution.

## Related

- [[Related Procedure: Prepare-and-Execute-Flink-RCE-PoC]]
- [[Related Command: nc-reverse-shell-listener]]
