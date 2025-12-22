---
name: activate-python-virtual-environment
type: command
executor: bash
data: source $_VENV_PATH/bin/activate
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

# activate-python-virtual-environment

## Command

```bash
source $_VENV_PATH/bin/activate
```

## Description

Activates the Python virtual environment to use isolated Python and pip.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VENV_PATH | Path to the virtual environment (e.g., venv) | Yes |

## Examples

### Basic Usage

```bash
source venv/bin/activate
```

## Expected Output

```
(venv) $
```

Prompt changes to indicate activation.

## Related

- [[procedures/ZeroLogon-Exploitation-and-Post-Exploitation]]
- [[commands/create-python-virtual-environment]]
