---
id: cmd-002
data: >-
  sudo apt-get install -y build-essential autoconf automake libtool pkg-config
  clang valgrind
tags:
  - setup
  - dependencies
type: command
output: Installed packages
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.083Z'
verified: false
validated: true
submitted: true
---
# apt-get-install-build-tools

## Command

```bash
sudo apt-get install -y build-essential autoconf automake libtool pkg-config clang valgrind
```

## Description

Installs essential build tools, compiler, and Valgrind for cURL compilation and testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-y` | Auto-confirm | Yes |
| `build-essential` | Core build packages | Yes |
| `clang` | C compiler | Yes |
| `valgrind` | Memory debugger | Yes |

## Examples

### Basic Usage

```bash
sudo apt-get install -y build-essential clang valgrind
```

### Advanced Usage

```bash
sudo apt-get install -y build-essential autoconf automake libtool pkg-config clang valgrind libssl-dev
```

## Expected Output

Reading package lists... Done; packages installed.

## Related

- [[commands/apt-get-update]]
- [[procedures/Building-cURL-with-Security-Debugging-Flags]]
