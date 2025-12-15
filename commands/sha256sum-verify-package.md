---
data: sha256sum nordvpn_3.10.0-1_amd64.deb
tags:
  - verification
  - hash
type: command
output: >-
  204d0089e326542c629c5f50a235de82bf3fa9fa829065be0490a0902e6770b63
  nordvpn_3.10.0-1_amd64.deb
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.214Z'
id: 319f9bd7-1499-441b-a15f-648e2209ae3f
verified: false
validated: true
submitted: true
---
# sha256sum-verify-package

## Command

```bash
sha256sum nordvpn_3.10.0-1_amd64.deb
```

## Description

Computes the SHA256 checksum of the NordVPN deb package file to verify its integrity and ensure it hasn't been tampered with before analysis or installation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| nordvpn_3.10.0-1_amd64.deb | Path to the deb package file | Yes |

## Examples

### Basic Usage

```bash
sha256sum nordvpn_3.10.0-1_amd64.deb
```

### Advanced Usage

```bash
sha256sum -c checksums.txt  # If using a file with expected hashes
```

## Expected Output

Hash followed by filename, e.g., 204d0089e326542c629c5f50a235de82bf3fa9fa829065be0490a0902e6770b63 nordvpn_3.10.0-1_amd64.deb. Compare against known good value.

## Related

- [[commands/dpkg-list-package-contents]]
- [[procedures/Install-NordVPN-Client-with-Vulnerable-Permissions]]
