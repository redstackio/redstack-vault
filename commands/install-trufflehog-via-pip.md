---
id: 83577ff0-c364-4fb7-8394-c30ced0e8d2d
name: install-trufflehog-via-pip
type: command
executor: bash
data: pip install truffleHog
output: null
created_at: '2023-04-06T03:56:00.111643+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - installation
  - trufflehog
verified: true
validated: true
---

# install-trufflehog-via-pip

## Command

```bash
pip install truffleHog
```

## Description

This command installs the TruffleHog tool via Python's pip package manager, enabling secret scanning in Git repositories. Use it in environments with Python 3.x to set up the tool for credential harvesting procedures.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `truffleHog` | The package name for installation | Yes |

## Examples

### Basic Usage

```bash
pip install truffleHog
```

### Advanced Usage

```bash
pip install --user truffleHog  # Install for current user only
```

## Expected Output

Successful installation outputs progress like:
```
Collecting truffleHog
  Downloading truffleHog-2.3.4-py3-none-any.whl (some size)
Installing collected packages: truffleHog
Successfully installed truffleHog-2.3.4
```
No errors indicate readiness; verify with `truffleHog --version`.

## Related

- [[commands/run-trufflehog-scan-on-repository]]
- [[procedures/Git-Repository-Secrets-Harvesting-with-TruffleHog]]
