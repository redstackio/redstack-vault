---
type: command
executor: bash
data: cd ItWasAllADream && poetry install && poetry shell
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - setup
  - dependencies
verified: true
validated: true
---

# install-itwasalladream-dependencies

## Command

```bash
cd ItWasAllADream && poetry install && poetry shell
```

## Description

Navigates to the ItWasAllADream directory, installs required Python dependencies using Poetry, and activates the virtual environment. This prepares the tool for local execution in PrintNightmare exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Directory | Assumes 'ItWasAllADream' exists from prior clone | Yes |

## Examples

### Basic Usage

```bash
cd ItWasAllADream && poetry install && poetry shell
```

### If Poetry Missing

First install Poetry: `pip install poetry`, then run the command.

## Expected Output

Installing dependencies from lock file (or pyproject.toml)...
Package operations: 10 installs, 0 updates, 0 removals
... (installation logs)
Spawning environment with /path/to/python
(ItWasAllADream-py3.10) $

## Related

- [[procedures/PrintNightmare-Remote-Code-Execution]]
