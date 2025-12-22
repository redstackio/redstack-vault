---
type: command
executor: bash
data: |-
  virtualenv3 venvADFSSpoof
  source venvADFSSpoof/bin/activate
platforms:
  - Linux
  - macOS
tags:
  - python
  - setup
verified: true
validated: true
---

# create-and-activate-python-virtual-environment

## Command

```bash
virtualenv3 venvADFSSpoof
source venvADFSSpoof/bin/activate
```

## Description

Creates a Python 3 virtual environment named venvADFSSpoof and activates it for isolated dependency management in ADFSpoof setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `venvADFSSpoof` | Name of the virtual environment | Yes |

## Examples

### Basic Usage

```bash
virtualenv3 venvADFSSpoof
source venvADFSSpoof/bin/activate
```

### Advanced Usage

Use `deactivate` to exit the environment later.

## Expected Output

Using base prefix '/usr'
New python executable in /path/venvADFSSpoof/bin/python3
Also creating executable in /path/venvADFSSpoof/bin/python
...
(venvADFSSpoof) $

Prompt changes to indicate activation.

## Related

- [[procedures/Golden-SAML-Attack-via-ADFS]]
