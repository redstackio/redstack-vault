---
data: ls -la $(brew --prefix)
tags:
  - recon
  - file-system
type: command
output: null
executor: bash
platforms:
  - macOS
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:10.100Z'
id: f4469028-8594-4011-9f09-96c2e4730059
verified: false
validated: true
submitted: true
---
# ls-homebrew-ls

## Command

```bash
ls -la $(brew --prefix)
```

## Description

Lists the contents of the Homebrew prefix directory in long format, revealing symlinks, permissions, and ownership to identify exploitable paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-la` | Long listing with all files, including hidden | Yes |
| `$(brew --prefix)` | Substitutes the Homebrew path | Yes |

## Examples

### Basic Usage

```bash
ls -la $(brew --prefix)
```

### Advanced Usage

```bash
ls -la $(brew --prefix) | grep '^l'  # Filter symlinks only
```

## Expected Output

Detailed directory listing, e.g., drwxr-xr-x  root  staff  /opt/homebrew with symlink details.

## Related

- [[Related Procedure|procedures/Exploit-Homebrew-Symlink-for-Root-Access]]
