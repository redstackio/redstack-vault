---
data: pip3 install pycryptodome
tags:
  - setup
  - python
type: command
executor: bash
platforms:
  - Linux
id: 58a4bbcb-d1c6-4203-b9f3-b6326ab9dc03
created_at: '2025-12-14T17:23:27.546Z'
updated_at: '2025-12-14T17:23:27.546Z'
verified: false
validated: true
submitted: true
---
# pip3-install-pycryptodome

## Command

```bash
pip3 install pycryptodome
```

## Description

Installs the pycryptodome Python library, which provides cryptographic primitives including the Crypto.Hash module needed for MD5 operations in exploitation scripts like primefaces.py.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `pycryptodome` | The package name for the library | Yes |

## Examples

### Basic Usage

```bash
pip3 install pycryptodome
```

### Advanced Usage

```bash
pip3 install pycryptodome --user
```

## Expected Output

Successful installation message, e.g., 'Successfully installed pycryptodome-3.18.0' with no errors.

## Related

- [[commands/pip3-install-pycryptodomex]]
