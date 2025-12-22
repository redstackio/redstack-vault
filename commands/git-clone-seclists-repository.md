---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: git-clone-seclists-repository
type: command
executor: bash
data: 'git clone https://github.com/danielmiessler/SecLists.git'
output: null
created_at: '2023-04-06T03:56:25Z'
updated_at: '2023-04-10T20:25:35Z'
platforms:
  - Linux
  - macOS
tags:
  - setup
  - wordlist
verified: true
validated: true
---

# git-clone-seclists-repository

## Command

```bash
git clone https://github.com/danielmiessler/SecLists.git
```

## Description

Clones the SecLists repository, a collection of wordlists for security testing, including DNS subdomains for brute-forcing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters; uses default Git clone | No |

## Examples

### Basic Usage

```bash
git clone https://github.com/danielmiessler/SecLists.git
```

## Expected Output

Cloning into 'SecLists'...
remote: Enumerating objects: 10000, done.
remote: Total 10000 (delta 0), reused 0 (delta 0), pack-reused 10000
Receiving objects: 100% (10000/10000), 50.00 MiB | 10.00 MiB/s, done.

## Related

- [[procedures/Subdomain-Enumeration-with-Knockpy-and-EyeWitness]]
