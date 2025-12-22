---
type: command
executor: bash
data: mysql --version
tags:
  - mysql
  - recon
  - version-check
platforms:
  - Linux
  - macOS
  - Windows
verified: true
validated: true
---

# mysql-check-version

## Command

```bash
mysql --version
```

## Description

This command queries the locally installed MySQL client to display its version information. It is used to verify if the MySQL version meets the minimum requirement (5.0+) for techniques relying on specific functions like NAME_CONST in error-based injections. Run this on the attacker's machine if simulating or on the target if shell access is available.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--version` | Displays the MySQL client version and exits | Yes |

No additional arguments are needed for basic version checking.

## Examples

### Basic Usage

```bash
mysql --version
```

### Usage with Connection (if testing remote)

```bash
mysql -h target-host -u user -p --version
```

> Note: The `--version` flag works independently of connection parameters but can be combined for remote checks.

## Expected Output

Successful execution produces output like:

```
mysql  Ver 8.0.30 for Linux on x86_64 (MySQL Community Server - GPL)
```

Look for the version number (e.g., 8.0.30) to confirm compatibility. If MySQL is not installed, it will error with a command not found message.

## Related

- [[procedures/MySQL-Error-Based-Injection-Using-NAME_CONST]]
