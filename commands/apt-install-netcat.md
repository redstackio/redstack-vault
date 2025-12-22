---
id: cmd-uuid-003
name: apt-install-netcat
type: command
executor: bash
data: apt update && apt install -y netcat
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:47.857Z'
platforms:
  - Linux
tags:
  - apt
  - installation
verified: false
validated: true
submitted: true
---

# apt-install-netcat

## Command

```bash
apt update && apt install -y netcat
```

## Description

Updates package index and installs netcat non-interactively in a Debian-based system like GitLab container.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `update` | Refresh package lists | Yes |
| `install -y netcat` | Install netcat without prompts | Yes |

## Examples

### Basic Usage

```bash
apt update && apt install -y netcat
```

### Advanced Usage

Install with specific version:
```bash
apt update && apt install -y netcat-traditional
```

## Expected Output

Logs showing package updates and installation success, e.g., "Setting up netcat (1.10-41.1) ...".

## Related

- [[commands/nc-listen-12345]]
- [[procedures/Install-Netcat-in-GitLab-Container]]
