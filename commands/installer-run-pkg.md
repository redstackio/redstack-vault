---
data: sudo installer -pkg package.pkg -target / -dumplog log_file
tags:
  - installation
  - privilege
type: command
output: null
executor: bash
platforms:
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:26.803Z'
id: 02b4847c-2954-406b-a48a-92b5d1059432
verified: false
validated: true
submitted: true
---
# installer-run-pkg

## Command

```bash
sudo installer -pkg package.pkg -target / -dumplog log_file
```

## Description

Installs a .pkg package on macOS using the installer tool, often requiring sudo for root installation. In exploits, used to trigger vulnerabilities like symlink following during the process.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-pkg` | Specifies the package file | Yes |
| `package.pkg` | Path to .pkg | Yes |
| `-target` | Installation target (e.g., / for system-wide) | Yes |
| `-dumplog` | Path to log file for output | No |

## Examples

### Basic Usage

```bash
sudo installer -pkg MozillaVPN.pkg -target /
```

### Advanced Usage

```bash
sudo installer -pkg app.pkg -target / -verbose -dumplog /tmp/install.log
```

## Expected Output

Installation progress messages; log file contains detailed actions, including file operations that may reveal exploits.

## Related

- [[Related Procedure: Achieve Privilege Escalation via Installer]]
