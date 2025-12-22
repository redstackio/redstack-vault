---
data: brew --prefix
tags:
  - recon
  - homebrew
type: command
output: null
executor: bash
platforms:
  - macOS
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:10.103Z'
id: d89f1faf-73b0-499d-ba2a-41b96e6ebc8c
verified: false
validated: true
submitted: true
---
# brew-prefix-check

## Command

```bash
brew --prefix
```

## Description

Displays the installation prefix for Homebrew, typically /opt/homebrew on macOS or /home/linuxbrew/.linuxbrew on Linux, used to locate the base directory for symlink attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--prefix` | Shows the Homebrew prefix path | Yes |

## Examples

### Basic Usage

```bash
brew --prefix
```

### Advanced Usage

```bash
brew --prefix | xargs ls -la
```

## Expected Output

A single line with the prefix path, e.g., /opt/homebrew.

## Related

- [[Related Procedure|procedures/Exploit-Homebrew-Symlink-for-Root-Access]]
