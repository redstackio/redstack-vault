---
id: 06d5cae4-831e-4854-a7f5-6d1dcae75ca3
name: pip-install-pivotnacci
type: command
executor: bash
data: pip3 install pivotnacci
output: null
created_at: '2023-04-06T03:56:22.599775+00:00'
updated_at: '2023-04-10T20:25:18.048816+00:00'
platforms:
  - Linux
tags:
  - installation
  - python
verified: true
validated: true
---

# pip-install-pivotnacci

## Command

```bash
pip3 install pivotnacci
```

## Description

This command installs the Pivotnacci Python package using pip3, enabling the creation of SOCKS proxies over HTTP agents for network pivoting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `pip3` | Python 3 package installer | Built-in |
| `install` | Installs the specified package | Built-in |
| `pivotnacci` | The package name for the pivoting tool | Yes |

## Examples

### Basic Usage

```bash
pip3 install pivotnacci
```

### Advanced Usage

```bash
pip3 install --user pivotnacci
```

## Expected Output

Successful installation will show progress like:

Collecting pivotnacci
  Downloading pivotnacci-0.1.0-py3-none-any.whl (10 kB)
Installing collected packages: pivotnacci
Successfully installed pivotnacci-0.1.0

## Related

- [[procedures/Web-SOCKS-Pivoting-with-Pivotnacci]]
