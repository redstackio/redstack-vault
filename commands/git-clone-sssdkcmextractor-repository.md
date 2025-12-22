---
id: cd41140e-ef00-4d1f-a614-858e35aae787
name: git-clone-sssdkcmextractor-repository
type: command
executor: bash
data: 'git clone https://github.com/fireeye/SSSDKCMExtractor'
output: null
created_at: '2023-04-06T03:56:08.604262+00:00'
updated_at: '2023-10-10T20:26:03.243838+00:00'
platforms:
  - Linux
tags:
  - extraction
  - kerberos
verified: true
validated: true
---

# git-clone-sssdkcmextractor-repository

## Command

```bash
git clone https://github.com/fireeye/SSSDKCMExtractor
```

## Description

This command clones the FireEye SSSDKCMExtractor repository from GitHub, which contains a Python tool for extracting Kerberos credentials from SSSD databases on Linux and Samsung Android devices. Use this as the first step in credential dumping procedures targeting AD-integrated systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://github.com/fireeye/SSSDKCMExtractor` | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/fireeye/SSSDKCMExtractor
```

### With Specific Directory

```bash
git clone https://github.com/fireeye/SSSDKCMExtractor ./tools/sssd
```

## Expected Output

Cloning into 'SSSDKCMExtractor'...
remote: Enumerating objects: 50, done.
remote: Total 50 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (50/50), done.

## Related

- [[procedures/CCACHE-Ticket-Reuse-from-SSSD-KCM-and-Android-Devices]]
- [[commands/python-extract-secrets-sssdkcmextractor]]
