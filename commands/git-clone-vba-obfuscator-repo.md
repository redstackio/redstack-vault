---
id: 8c313328-de2f-47d6-9c67-7149eab1050e
name: git-clone-vba-obfuscator-repo
type: command
executor: bash
data: 'git clone https://github.com/bonnetn/vba-obfuscator'
output: null
created_at: '2023-04-06T03:56:23.756677+00:00'
updated_at: '2023-04-10T20:36:59.136282+00:00'
platforms:
  - Linux
  - macOS
tags:
  - git
  - clone
  - obfuscation
verified: true
validated: true
---

# git-clone-vba-obfuscator-repo

## Command

```bash
git clone https://github.com/bonnetn/vba-obfuscator
```

## Description

This command clones the vba-obfuscator GitHub repository, which contains a Docker-based tool for obfuscating VBA macros. Use this as the first step in setting up VBA obfuscation for defense evasion in Office-based attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://github.com/bonnetn/vba-obfuscator` | The repository URL to clone | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/bonnetn/vba-obfuscator
```

### Advanced Usage

Clone to a specific directory:
```bash
git clone https://github.com/bonnetn/vba-obfuscator ./my-tools/
```

## Expected Output

Cloning into 'vba-obfuscator'...
remote: Enumerating objects: 50, done.
remote: Counting objects: 100% (50/50), done.
remote: Compressing objects: 100% (30/30), done.
Receiving objects: 100% (50/50), 20.00 KiB | 1.00 MiB/s, done.
Resolving deltas: 100% (20/20), done.

A new 'vba-obfuscator' directory is created with the tool files.

## Related

- [[procedures/Obfuscate-VBA-Macros-Using-vba-obfuscator]]
