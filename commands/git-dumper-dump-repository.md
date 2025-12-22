---
id: 6263497b-69cd-4664-9201-c7f2669c236d
name: git-dumper-dump-repository
type: command
executor: bash
data: ./git-dumper.py $_TARGET_GIT_URL $_OUTPUT_DIR
output: null
created_at: '2023-04-06T03:55:59.891893+00:00'
updated_at: '2023-04-10T20:33:54.555211+00:00'
platforms:
  - Linux
tags:
  - git-dumper
  - dump
  - recovery
verified: true
validated: true
---

# git-dumper-dump-repository

## Command

```bash
./git-dumper.py $_TARGET_GIT_URL $_OUTPUT_DIR
```

## Description

This command runs the git-dumper.py script to download and reconstruct a Git repository from an exposed .git directory over HTTP, saving the recovered repo to a local output directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_GIT_URL | URL of the exposed .git directory (e.g., http://target.com/.git) | Yes |
| $_OUTPUT_DIR | Local directory to save the reconstructed repository | Yes |

## Examples

### Basic Usage

```bash
./git-dumper.py http://example.com/.git ~/recovered-repo
```

### With Silent Output

```bash
./git-dumper.py http://example.com/.git ~/recovered-repo > dump.log 2>&1
```

## Expected Output

[*] Getting info/refs
[+] HEAD: refs/heads/master
[*] Getting pack
[+] objects/pack/pack-abc123.git
[+] refs/heads/master: abc123def456
[*] Downloading 50 objects...
[100%] Done.
Repository successfully dumped to ~/recovered-repo

## Related

- [[procedures/Recover-Source-Code-from-Insecure-Git-Repository-Using-Git-Dumper]]
- [[tools/git-dumper]]
