---
data: apt-get install sudo git build-essential
tags:
  - setup
  - packages
type: command
output: |-
  Reading package lists... Done
  Building dependency tree... Done
  ... (packages installed successfully)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:56.989Z'
id: 9df56383-ce91-4443-856e-d9bfc0fa0d3e
verified: false
validated: true
submitted: true
---
# apt-get-install-packages

## Command

```bash
apt-get install sudo git build-essential
```

## Description

Installs sudo for user switching, git for cloning repositories, and build-essential (including gcc) for compiling C code in a Debian-based Linux environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| install | Specifies packages to install | Yes |
| sudo | Enables privileged command execution | Yes |
| git | Version control tool | Yes |
| build-essential | Compilation tools like gcc, make | Yes |

## Examples

### Basic Usage

```bash
apt-get install sudo git build-essential
```

### Advanced Usage

```bash
apt-get update && apt-get install -y sudo git build-essential
```

## Expected Output

'0 upgraded, 3 newly installed... Setting up sudo... Setting up git... Setting up build-essential...'

## Related

- [[commands/sudo-switch-to-git]]
- [[procedures/Prepare-Environment-as-Git-User]]
