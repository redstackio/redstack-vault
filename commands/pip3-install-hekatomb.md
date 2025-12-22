---
type: command
executor: bash
data: pip3 install hekatomb
output: null
created_at: '2023-04-06T03:56:26.320991+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - installation
  - python
verified: true
validated: true
---

# pip3-install-hekatomb

## Command

```bash
pip3 install hekatomb
```

## Description

This command installs the Hekatomb Python package, a tool for DPAPI-based credential theft in Windows environments. Use it as the first step before executing extraction commands.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `pip3` | Python 3 package installer | Yes |
| `install` | Installs the specified package | Yes |
| `hekatomb` | The Hekatomb package from PyPI | Yes |

## Examples

### Basic Usage

```bash
pip3 install hekatomb
```

### With Upgrade

```bash
pip3 install --upgrade hekatomb
```

## Expected Output

Collecting hekatomb
  Downloading hekatomb-0.1.0-py3-none-any.whl (xx kB)
...
Successfully installed hekatomb-0.1.0 dpapick-...

## Related

- [[procedures/DPAPI-Credential-Theft-with-Hekatomb]]
- [[tools/Hekatomb]]
