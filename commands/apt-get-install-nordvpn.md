---
data: apt-get install nordvpn
tags:
  - install
  - nordvpn
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.195Z'
id: e799c57d-5e55-4a14-b3b6-cee3677ebd50
verified: false
validated: true
submitted: true
---
# apt-get-install-nordvpn

## Command

```bash
apt-get install nordvpn
```

## Description

Installs the NordVPN client package from the repository, deploying the vulnerable service files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| install | Install mode | Yes |
| nordvpn | Package name | Yes |

## Examples

### Basic Usage

```bash
sudo apt-get install nordvpn
```

### Advanced Usage

```bash
sudo apt-get install -y nordvpn
```

## Expected Output

"NordVPN installed with vulnerable files"; package unpacked.

## Related

- [[commands/apt-get-update]]
- [[procedures/Install-NordVPN-Client-with-Vulnerable-Permissions]]
