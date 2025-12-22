---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: pip install fabric-sdk-py==1.5.3
tags:
  - installation
  - vulnerability-setup
type: command
output: null
executor: bash
platforms:
  - Python
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:16:31.342Z'
verified: false
validated: true
submitted: true
---
# pip-install-vulnerable-package

## Command

```bash
pip install fabric-sdk-py==1.5.3
```

## Description

Installs a specific vulnerable version of the fabric-sdk-py package to replicate the XSS environment, ensuring the outdated jQuery dependency is included for doc generation exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `fabric-sdk-py==1.5.3` | Specifies the exact vulnerable version; adjust based on report details | Yes |

## Examples

### Basic Usage

```bash
pip install fabric-sdk-py==1.5.3
```

### Advanced Usage

```bash
pip install --user fabric-sdk-py==1.5.3  # Install for current user only
```

## Expected Output

Installation progress with dependency resolution, ending in 'Successfully installed fabric-sdk-py-1.5.3' and related packages, including vulnerable jQuery.

## Related

- [[Related Procedure: Demonstrate-XSS-in-fabric-sdk-py-Doc-Generation]]
