---
id: 6ca3f14f-f146-4e8d-b02d-b6c7cf0b130f
name: git-clone-mso-lspray-from-github
type: command
executor: bash
data: 'git clone https://github.com/dafthack/MSOLSpray'
output: null
created_at: '2023-05-23T16:38:53.036204+00:00'
updated_at: '2023-05-23T16:38:53.084754+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - setup
  - download
verified: true
validated: true
---

# git-clone-mso-lspray-from-github

## Command

```bash
git clone https://github.com/dafthack/MSOLSpray
```

## Description

This command clones the MSOLSpray repository from GitHub, downloading the PowerShell tool for Azure AD password spraying.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/dafthack/MSOLSpray | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/dafthack/MSOLSpray
```

### With Specific Directory

```bash
git clone https://github.com/dafthack/MSOLSpray ./tools/mso-lspray
```

## Expected Output

Cloning into 'MSOLSpray'...
remote: Enumerating objects: 50, done.
remote: Counting objects: 100% (50/50), done.
remote: Compressing objects: 100% (30/30), done.
Receiving objects: 100% (50/50), 20.00 KiB | 1.00 MiB/s, done.

## Related

- [[procedures/Azure-AD-Password-Spray]]
