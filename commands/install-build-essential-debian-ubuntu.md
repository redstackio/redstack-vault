---
type: command
executor: bash
data: apt update && apt install build-essential -y
tags:
  - installation
  - dependencies
platforms:
  - Linux
verified: true
validated: true
---

# install-build-essential-debian-ubuntu

## Command

```bash
apt update && apt install build-essential -y
```

## Description

Updates package index and installs essential build tools including gcc, g++, and make on Debian/Ubuntu-based systems. Use before compiling C programs like exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Runs with default options; uses sudo if needed for installation | No |

## Examples

### Basic Usage

```bash
apt update && apt install build-essential -y
```

### Advanced Usage

```bash
apt update && apt install build-essential gcc-multilib -y
```

(Adds 32-bit support for cross-compilation.)

## Expected Output

Description of what output to expect when the command runs successfully.

Hit:1 http://archive.ubuntu.com/ubuntu focal InRelease
...
Reading package lists... Done
Building dependency tree       
Reading state information... Done
...
build-essential is already the newest version.
(or installation progress if not installed)

## Related

- [[procedures/Exploit-Dirty-Cow-Vulnerability]]
- [[commands/gcc-compile-dirty-cow-exploit]]
