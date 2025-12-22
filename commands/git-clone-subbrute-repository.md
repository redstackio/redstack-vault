---
type: command
executor: bash
data: 'git clone https://github.com/TheRook/subbrute'
tags:
  - installation
  - recon
platforms:
  - Linux
verified: true
validated: true
---

# git-clone-subbrute-repository

## Command

```bash
git clone https://github.com/TheRook/subbrute
```

## Description

This command downloads the Subbrute tool from its official GitHub repository, creating a local copy for installation and use in subdomain enumeration tasks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/TheRook/subbrute | The repository URL to clone from | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/TheRook/subbrute
```

### Advanced Usage

If git is not installed, first install it with `sudo apt install git` on Debian-based systems.

## Expected Output

Cloning into 'subbrute'...
remote: Enumerating objects: 50, done.
remote: Total 50 (delta 0), reused 0 (delta 0), pack-reused 50
Receiving objects: 100% (50/50), done.

## Related

- [[procedures/Subdomain-Enumeration-Using-Subbrute]]
- [[tools/Subbrute]]
