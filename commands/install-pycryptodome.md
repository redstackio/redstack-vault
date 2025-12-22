---
data: pip3 install pycryptodome
tags:
  - setup
  - python
type: command
output: Successfully installed pycryptodome
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.820Z'
id: 31d3fb1a-bea3-4615-a383-eb7abccd2629
verified: false
validated: true
submitted: true
---
# install-pycryptodome

## Command

```bash
pip3 install pycryptodome
```

## Description

Installs the PyCryptodome Python library, a self-contained cryptographic toolkit used for encryption and decryption operations in exploits targeting Telerik's custom handling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `pip3` | Python 3 package installer | Yes |
| `install` | Installs the specified package | Yes |
| `pycryptodome` | The cryptographic library package | Yes |

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

Successful installation: "Collecting pycryptodome\nDownloading...\nSuccessfully installed pycryptodome-3.20.0". Errors if pip3 or internet unavailable.

## Related

- [[commands/execute-telerik-exploit]]
- [[procedures/Prepare-Telerik-Deserialization-Exploit]]
