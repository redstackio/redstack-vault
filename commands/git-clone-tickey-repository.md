---
id: 77a837bc-251d-4532-986d-1175ec344aa4
name: git-clone-tickey-repository
type: command
executor: bash
data: 'git clone https://github.com/TarlogicSecurity/tickey'
output: null
created_at: '2023-04-06T03:56:08.565454+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - setup
  - tool-installation
verified: true
validated: true
---

# Git Clone Tickey Repository

## Command

```bash
git clone https://github.com/TarlogicSecurity/tickey
```

## Description

Clones the Tickey tool repository from GitHub to the local filesystem, downloading the source code necessary for building the Kerberos ticket extraction utility.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/TarlogicSecurity/tickey | The URL of the Tickey GitHub repository | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/TarlogicSecurity/tickey
```

### With Specific Directory

```bash
git clone https://github.com/TarlogicSecurity/tickey tickey-tool
```

## Expected Output

Cloning into 'tickey'...
remote: Enumerating objects: X, done.
remote: Counting objects: 100% (X/X), done.
remote: Compressing objects: 100% (X/X), done.
Receiving objects: 100% (X/X), X MiB | X MiB/s, done.
Resolving deltas: 100% (X/X), done.

## Related

- [[procedures/extract-ccache-tickets-from-linux-keyring-with-tickey]]
- [[tools/tickey]]
