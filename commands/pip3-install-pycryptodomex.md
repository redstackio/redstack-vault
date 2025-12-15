---
data: pip3 install pycryptodomex
tags:
  - setup
  - python
type: command
executor: bash
platforms:
  - Linux
id: db721e05-5233-4289-b4ac-587d7108a7c1
created_at: '2025-12-14T17:23:27.529Z'
updated_at: '2025-12-14T17:23:27.529Z'
verified: false
validated: true
submitted: true
---
# pip3-install-pycryptodomex

## Command

```bash
pip3 install pycryptodomex
```

## Description

Alternative installation for a pycryptodome variant to provide Crypto.Hash functionality, useful if the standard pycryptodome conflicts with existing installations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `pycryptodomex` | The package name for the alternative library | Yes |

## Examples

### Basic Usage

```bash
pip3 install pycryptodomex
```

### Advanced Usage

```bash
pip3 install pycryptodomex --upgrade
```

## Expected Output

Successful installation, e.g., 'Successfully installed pycryptodomex-3.18.0'.

## Related

- [[commands/pip3-install-pycryptodome]]
