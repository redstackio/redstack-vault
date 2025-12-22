---
type: command
executor: bash
data: |-
  apt install cmake build-essential -y
  apt install checkinstall git -y
platforms:
  - Linux
tags:
  - installation
  - dependencies
verified: true
validated: true
---

# apt-install-hashcat-build-dependencies

## Command

```bash
apt install cmake build-essential -y
apt install checkinstall git -y
```

## Description

This command installs the core dependencies needed to build Hashcat from source on Debian-based systems. It handles build tools and version control in sequence for a seamless setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-y` | Automatically confirm package installation without prompts | Yes |
| `cmake` | Build system configuration tool | Built-in (package name) |
| `build-essential` | Essential compilation tools (gcc, make, etc.) | Built-in (package name) |
| `checkinstall` | Tool to create .deb packages from source builds | Built-in (package name) |
| `git` | Version control system for cloning repositories | Built-in (package name) |

## Examples

### Basic Usage

```bash
apt install cmake build-essential -y
apt install checkinstall git -y
```

### Advanced Usage

If behind a proxy, prepend `http_proxy=...` to the commands for repository access.

## Expected Output

Reading package lists... Done
Building dependency tree... Done
The following NEW packages will be installed:
  cmake build-essential checkinstall git
0 upgraded, 4 newly installed, 0 to remove and 0 not upgraded.
Need to get 10.0 MB of archives.
After this operation, 50.0 MB of additional disk space will be used.
... (installation progress)
Setting up cmake (3.16.3-1ubuntu1) ...
```

## Related

- [[procedures/Install-Hashcat-from-Source]]
- [[tools/Hashcat]]
