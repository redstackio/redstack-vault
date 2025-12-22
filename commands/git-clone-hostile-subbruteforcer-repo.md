---
id: 4c436c54-ef73-4712-8c10-953f996037f9
name: git-clone-hostile-subbruteforcer-repo
type: command
executor: bash
data: 'git clone https://github.com/nahamsec/HostileSubBruteforcer'
output: null
created_at: '2023-04-06T03:56:25.800728+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - setup
  - recon
verified: true
validated: true
---

# git-clone-hostile-subbruteforcer-repo

## Command

```bash
git clone https://github.com/nahamsec/HostileSubBruteforcer
```

## Description

This command clones the Hostile Subdomain Bruteforcer repository from GitHub, downloading the Ruby script and default wordlist needed for subdomain enumeration and takeover detection. Use this as the first step in setting up the tool on a Linux system with Git installed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/nahamsec/HostileSubBruteforcer | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/nahamsec/HostileSubBruteforcer
```

### With Specific Directory

```bash
git clone https://github.com/nahamsec/HostileSubBruteforcer ./my-tools
```

## Expected Output

Cloning into 'HostileSubBruteforcer'...
remote: Enumerating objects: 10, done.
remote: Counting objects: 100% (10/10), done.
remote: Compressing objects: 100% (8/8), done.
Receiving objects: 100% (20/20), 5.00 KiB | 5.00 KiB/s, done.

## Related

- [[procedures/Subdomain-Enumeration-and-Takeover-using-Hostile-Subdomain-Bruteforcer]]
- [[tools/Hostile-Subdomain-Bruteforcer]]
