---
id: b26f462e-4a11-4578-906b-12ef247a2f5e
name: git-clone-revsocks-repo
type: command
executor: bash
data: 'git clone https://github.com/kost/revsocks'
output: null
created_at: '2023-04-06T03:56:23.693451Z'
updated_at: '2023-04-10T20:36:49.692107Z'
platforms:
  - Linux
tags:
  - build
  - go
verified: true
validated: true
---

# git-clone-revsocks-repo

## Command

```bash
git clone https://github.com/kost/revsocks
```

## Description

Clones the revsocks source code repository from GitHub to the local directory for building the tool.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/kost/revsocks
```

## Expected Output

Cloning into 'revsocks'...
remote: Enumerating objects: X, done.
remote: Counting objects: 100% (X/X), done.
...
Resolving deltas: 100% (X/X), done.

## Related

- [[procedures/Reverse-SOCKS-Proxy-Pivoting]]
