---
id: a86547e0-950e-403e-bdbc-2ae0add934ea
name: install-python-in-wsl
type: command
executor: bash
data: sudo apt-get update && sudo apt-get install -y python3
output: null
created_at: '2023-04-06T03:56:29.607962+00:00'
updated_at: '2023-04-10T20:37:54.958414+00:00'
platforms:
  - Linux
tags:
  - wsl
  - setup
verified: true
validated: true
---

# install-python-in-wsl

## Command

```bash
sudo apt-get update && sudo apt-get install -y python3
```

## Description

Updates package lists and installs Python3 within the WSL Ubuntu environment, required for executing Python-based payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sudo | Runs with elevated privileges | Yes |
| apt-get update | Refreshes package index | Yes |
| apt-get install -y | Installs without prompts | Yes |
| python3 | Python3 package | Yes |

## Examples

### Basic Usage

```bash
sudo apt-get update && sudo apt-get install -y python3
```

## Expected Output

Reading package lists... Done
Building dependency tree... Done
... (installation progress)
Setting up python3 (3.x.x-1) ...

## Related

- [[procedures/WSL-Privilege-Escalation-via-Default-User-Modification]]
