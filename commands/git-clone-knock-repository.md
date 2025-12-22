---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: git-clone-knock-repository
type: command
executor: bash
data: 'git clone https://github.com/guelfoweb/knock.git'
output: null
created_at: '2023-04-06T03:56:25Z'
updated_at: '2023-04-10T20:25:35Z'
platforms:
  - Linux
  - macOS
tags:
  - setup
  - tool-install
verified: true
validated: true
---

# git-clone-knock-repository

## Command

```bash
git clone https://github.com/guelfoweb/knock.git
```

## Description

Clones the Knockpy repository, a Python tool for subdomain brute-forcing via DNS queries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters; uses default Git clone | No |

## Examples

### Basic Usage

```bash
git clone https://github.com/guelfoweb/knock.git
```

## Expected Output

Cloning into 'knock'...
remote: Enumerating objects: 500, done.
remote: Total 500 (delta 0), reused 0 (delta 0), pack-reused 500
Receiving objects: 100% (500/500), 1.00 MiB | 500.00 KiB/s, done.

## Related

- [[procedures/Subdomain-Enumeration-with-Knockpy-and-EyeWitness]]
