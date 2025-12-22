---
id: 55063317-1a6c-47ba-87c7-c902dbd24d06-part1
name: apt-install-socat
type: command
executor: bash
data: sudo apt update && sudo apt install socat
output: null
created_at: '2023-04-06T03:56:16.271092+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - installation
  - socat
verified: true
validated: true
---

# apt-install-socat

## Command

```bash
sudo apt update && sudo apt install socat
```

## Description

This command updates the package index and installs the Socat utility on Debian-based Linux systems like Ubuntu, which is required for setting up network redirects and proxies in C2 infrastructure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sudo` | Elevates privileges for package management | Yes |
| `apt update` | Refreshes the list of available packages | Yes |
| `apt install socat` | Installs the Socat package | Yes |

## Examples

### Basic Usage

```bash
sudo apt update && sudo apt install socat
```

### If Already Installed

The command will output that Socat is already the newest version and skip installation.

## Expected Output

Reading package lists... Done
Building dependency tree... Done
... (progress)
socat is already the newest version (1.7.4.1-3ubuntu1).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.

Or for fresh install:
... (download progress)
Setting up socat (1.7.4.1-3ubuntu1) ...

## Related

- [[procedures/Install-Socat-Redirector-for-Cobalt-Strike]]
- [[commands/socat-forward-traffic-to-team-server]]
