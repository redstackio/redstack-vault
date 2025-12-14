---
data: apt-get update
tags:
  - update
  - packages
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.198Z'
id: 2a319722-39ac-4470-89ae-ee71a339bd32
verified: false
validated: true
submitted: true
---
# apt-get-update

## Command

```bash
apt-get update
```

## Description

Refreshes the local package index from all configured repositories, including newly added ones like NordVPN.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| update | Refresh package index | Yes |

## Examples

### Basic Usage

```bash
sudo apt-get update
```

### Advanced Usage

```bash
sudo apt-get update -qq
```

## Expected Output

Updated package lists; mentions of new repos like "Hit: https://repo.nordvpn.com".

## Related

- [[commands/apt-get-install-nordvpn]]
- [[procedures/Install-NordVPN-Client-with-Vulnerable-Permissions]]
