---
data: pkgutil --expand package.pkg output_dir
tags:
  - package
  - analysis
type: command
output: null
executor: bash
platforms:
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:26.805Z'
id: 794556d3-3805-456e-9eec-8bae5a507abf
verified: false
validated: true
submitted: true
---
# pkgutil-expand

## Command

```bash
pkgutil --expand package.pkg output_dir
```

## Description

Expands a macOS .pkg installer package into a directory for inspection, useful for analyzing components like scripts for vulnerabilities such as symlink flaws.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--expand` | Command to unpack the package | Yes |
| `package.pkg` | Path to the .pkg file | Yes |
| `output_dir` | Directory to extract contents | Yes |

## Examples

### Basic Usage

```bash
pkgutil --expand MozillaVPN.pkg /tmp/expanded
```

### Advanced Usage

```bash
pkgutil --expand /Downloads/app.pkg ~/analysis/
```

## Expected Output

Creates output_dir with subdirectories like Payload, Resources, and scripts; no stdout unless error.

## Related

- [[Related Procedure: Analyze Mozilla VPN Installer for Symlink Flaws]]
