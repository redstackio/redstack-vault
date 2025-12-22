---
data: dpkg -i nordvpn-release_1.0.0_all.deb
tags:
  - install
  - repository
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.201Z'
id: a93bb8f7-5971-4384-9b09-c4acefa4711e
verified: false
validated: true
submitted: true
---
# dpkg-install-release

## Command

```bash
dpkg -i nordvpn-release_1.0.0_all.deb
```

## Description

Installs the NordVPN repository release package, adding the NordVPN apt source to /etc/apt/sources.list.d/.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i | Install mode | Yes |
| nordvpn-release_1.0.0_all.deb | Path to the deb file | Yes |

## Examples

### Basic Usage

```bash
dpkg -i nordvpn-release_1.0.0_all.deb
```

### Advanced Usage

```bash
sudo dpkg -i --force-depends package.deb
```

## Expected Output

"Repository added successfully" or similar; no fatal errors.

## Related

- [[commands/wget-download-nordvpn-release]]
- [[procedures/Install-NordVPN-Client-with-Vulnerable-Permissions]]
