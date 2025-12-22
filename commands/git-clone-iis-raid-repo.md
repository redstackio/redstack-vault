---
id: 91b3aa47-8a44-4f22-b1a4-bf7655f1acf8
name: git-clone-iis-raid-repo
type: command
executor: bash
data: 'git clone https://github.com/0x09AL/IIS-Raid'
output: null
created_at: '2023-04-06T03:56:27.931360+00:00'
updated_at: '2023-04-10T20:37:21.199886+00:00'
platforms:
  - Linux
  - macOS
tags:
  - persistence
  - iis
verified: true
validated: true
---

# git-clone-iis-raid-repo

## Command

```bash
git clone https://github.com/0x09AL/IIS-Raid
```

## Description

Clones the IIS-Raid GitHub repository to the local machine, downloading the tool used for backdooring IIS servers. Run this on the attacker's control machine to obtain the necessary scripts and DLLs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/0x09AL/IIS-Raid | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/0x09AL/IIS-Raid
```

This creates a local directory named 'IIS-Raid' with all tool files.

## Expected Output

Cloning into 'IIS-Raid'...
remote: Enumerating objects: X, done.
remote: Counting objects: 100% (X/X), done.
...
Resolving deltas: 100% (X/X), done.

Directory 'IIS-Raid' created with files like iis_controller.py.

## Related

- [[procedures/IIS-Raid-Backdoor-Persistence]]
- [[commands/python-execute-iis-controller]]
