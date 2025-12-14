---
data: >-
  wget
  https://repo.nordvpn.com/deb/nordvpn/debian/pool/main/nordvpn-release_1.0.0_all.deb
tags:
  - download
  - repository
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.203Z'
id: 48b59364-8ef9-4e25-9ac0-5650757d1e5e
verified: false
validated: true
submitted: true
---
# wget-download-nordvpn-release

## Command

```bash
wget https://repo.nordvpn.com/deb/nordvpn/debian/pool/main/nordvpn-release_1.0.0_all.deb
```

## Description

Downloads the NordVPN repository release package from the official URL to add the repo to the system's apt sources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://repo.nordvpn.com/.../nordvpn-release_1.0.0_all.deb | URL of the release deb file | Yes |

## Examples

### Basic Usage

```bash
wget https://repo.nordvpn.com/deb/nordvpn/debian/pool/main/nordvpn-release_1.0.0_all.deb
```

### Advanced Usage

```bash
wget -O release.deb https://repo.nordvpn.com/deb/nordvpn/debian/pool/main/nordvpn-release_1.0.0_all.deb
```

## Expected Output

File downloaded to current directory; progress bar or HTTP 200 status.

## Related

- [[commands/dpkg-install-release]]
- [[procedures/Install-NordVPN-Client-with-Vulnerable-Permissions]]
