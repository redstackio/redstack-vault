---
id: 2c1e8c15-a0d0-4c45-9184-0d135adc2343
type: command
executor: bash
data: pipenv shell
output: null
created_at: '2023-04-06T03:56:14.584630+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - setup
  - python
verified: true
validated: true
---

# pipenv-shell-activate

## Command

```bash
pipenv shell
```

## Description

Activates the virtual environment managed by Pipenv for a Python project, isolating dependencies for tools like ROADRecon or StormSpotter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; assumes Pipenv is installed and Pipfile exists in current directory | No |

## Examples

### Basic Usage

```bash
pipenv shell
```

Activates the environment and changes prompt to indicate shell activation.

## Expected Output

(ENV) user@host:~/project$ 

Indicates successful activation; exit with 'exit'.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/ROADRecon]]
