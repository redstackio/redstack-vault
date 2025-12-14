---
data: dpkg -c /var/cache/apt/archives/nordvpn_3.10.0-1_amd64.deb
tags:
  - inspection
  - package
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.208Z'
id: 4924aac9-228c-4584-a7c1-a4f78ebe1c7c
verified: false
validated: true
submitted: true
---
# dpkg-list-package-contents

## Command

```bash
dpkg -c /var/cache/apt/archives/nordvpn_3.10.0-1_amd64.deb
```

## Description

Lists the contents of a Debian package, including file paths, permissions, sizes, and ownership, to inspect structure and identify unsafe permissions like world-writable files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -c | Show package contents listing | Yes |
| /var/cache/apt/archives/nordvpn_3.10.0-1_amd64.deb | Path to the deb file | Yes |

## Examples

### Basic Usage

```bash
dpkg -c package.deb
```

### Advanced Usage

```bash
dpkg -c package.deb | grep permissions
```

## Expected Output

Detailed listing, e.g., drwxrwxrwx root/root 0 ... /etc/init.d/nordvpn, revealing 777 permissions on service files.

## Related

- [[commands/sha256sum-verify-package]]
- [[procedures/Install-NordVPN-Client-with-Vulnerable-Permissions]]
