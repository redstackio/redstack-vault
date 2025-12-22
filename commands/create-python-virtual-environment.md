---
id: d624020e-9f0e-48cb-aee1-b82146d3fa2b
name: create-python-virtual-environment
type: command
executor: bash
data: python3 -m venv $_VENV_NAME
output: null
created_at: '2023-04-06T03:56:02.672932+00:00'
updated_at: '2023-04-10T20:36:01.289773+00:00'
platforms:
  - Linux
tags:
  - python
  - venv
verified: true
validated: true
---

# create-python-virtual-environment

## Command

```bash
python3 -m venv $_VENV_NAME
```

## Description

Creates a Python virtual environment to isolate dependencies for tools like Impacket.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VENV_NAME | Name of the virtual environment directory (e.g., venv) | Yes |

## Examples

### Basic Usage

```bash
python3 -m venv venv
```

## Expected Output

```
created virtual environment in venv
```

## Related

- [[procedures/ZeroLogon-Exploitation-and-Post-Exploitation]]
- [[commands/activate-python-virtual-environment]]
