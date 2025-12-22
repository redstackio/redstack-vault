---
id: 0c8a66fc-028d-4b65-9ac9-835402681a78
name: git-clone-adconnectdump-repository
type: command
executor: bash
data: 'git clone https://github.com/fox-it/adconnectdump'
output: null
created_at: '2023-04-06T03:56:16.148380+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - setup
  - tool-download
verified: true
validated: true
---

# git-clone-adconnectdump-repository

## Command

```bash
git clone https://github.com/fox-it/adconnectdump
```

## Description

This command clones the adconnectdump repository from GitHub, downloading the Python tool used for extracting Azure AD Connect credentials and performing DCSync attacks. Use this as the first step when preparing to dump AD Sync account hashes on a compromised sync server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/fox-it/adconnectdump | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/fox-it/adconnectdump
```

### With Specific Directory

```bash
git clone https://github.com/fox-it/adconnectdump ./tools/adconnectdump
```

## Expected Output

Cloning into 'adconnectdump'...
remote: Enumerating objects: 20, done.
remote: Counting objects: 100% (20/20), done.
remote: Compressing objects: 100% (15/15), done.
Receiving objects: 100% (20/20), 5.12 KiB | 5.12 KiB/s, done.

## Related

- [[procedures/azure-ad-connect-password-extraction-via-ad-sync-dcsync]]
- [[tools/adconnectdump]]
