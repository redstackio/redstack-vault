---
id: cmd-uuid-2
data: pip install pysha3
tags:
  - installation
  - python
type: command
output: Successfully installed pysha3-1.0.2
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.323Z'
verified: false
validated: true
submitted: true
---
# install-pysha3

## Command

```bash
pip install pysha3
```

## Description

This command installs the pysha3 Python library via pip, providing SHA3 hashing functions necessary for crafting the malformed RLP data in the DoS PoC script targeting the RSKJ server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Installs latest version from PyPI | N/A |

## Examples

### Basic Usage

```bash
pip install pysha3
```

### Advanced Usage

```bash
pip install pysha3==1.0.2 --user
```

## Expected Output

"Collecting pysha3 ... Successfully installed pysha3-1.0.2"

## Related

- [[procedures/Craft-and-Send-Malicious-UDP-Packet]]
- [[tools/Python-3]]
