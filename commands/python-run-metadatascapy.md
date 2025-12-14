---
data: python3 /metadatascapy.py
tags:
  - exploit
  - mitm
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.880Z'
id: d88ac424-67f2-4704-a3a4-46bb8a4dff7f
verified: false
validated: true
submitted: true
---
# python-run-metadatascapy

## Command

```bash
python3 /metadatascapy.py
```

## Description

Executes the Scapy-based script to perform MITM on metadata service and inject SSH key.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| script | Path to metadatascapy.py | Yes |

## Examples

### Basic Usage

```bash
python3 exploit.py
```

## Expected Output

Sniffing for metadata traffic... Key injected successfully. Kubeconfig: ...

## Related

- [[procedures/Execute-MITM-Exploit-Script-for-Privilege-Escalation]]
