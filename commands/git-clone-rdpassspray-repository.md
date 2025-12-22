---
type: command
executor: bash
data: 'git clone https://github.com/xFreed0m/RDPassSpray'
platforms:
  - Linux
tags:
  - setup
  - tool-install
verified: true
validated: true
---

# git-clone-rdpassspray-repository

## Command

```bash
git clone https://github.com/xFreed0m/RDPassSpray
```

## Description

This command clones the RDPassSpray repository from GitHub, downloading the tool used for RDP password spraying. Use this as the first step to acquire the script before running spraying operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/xFreed0m/RDPassSpray | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/xFreed0m/RDPassSpray
```

### With Destination Directory

```bash
git clone https://github.com/xFreed0m/RDPassSpray ./tools/
```

## Expected Output

Cloning into 'RDPassSpray'...
remote: Enumerating objects: 20, done.
remote: Counting objects: 100% (20/20), done.
remote: Compressing objects: 100% (15/15), done.
Receiving objects: 100% (20/20), done.

## Related

- [[procedures/RDP-Service-Password-Spraying]]
- [[tools/rdpas-sspray]]
