---
type: command
executor: bash
data: python3 smuggler.py -h
output: null
platforms:
  - linux
  - macos
tags:
  - setup
  - help
verified: true
validated: true
---

# Smuggler Py Display Help

## Command

```bash
python3 smuggler.py -h
```

## Description

This command shows the help menu for the Smuggler Python script, listing options for detection modes, custom requests, and configuration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -h | Help flag | Yes |

## Examples

### Basic Usage

```bash
python3 smuggler.py -h
```

## Expected Output

usage: smuggler.py [-h] -u URL [--mode {clte,tecl,te.te,cl.cl}] [-s SPEED] ...

positional arguments:
  ...

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Target URL
  --mode {clte,tecl,...} Smuggling mode
  ...

## Related

- [[procedures/http-request-smuggling-detection-and-exploitation]]
- [[tools/smuggler]]
