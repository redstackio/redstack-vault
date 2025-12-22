---
id: 69304f46-8376-437a-85ca-05b4d58bab62
name: git-clone-dnsdumpster-repository
type: command
executor: bash
data: 'git clone https://github.com/nmmapper/dnsdumpster'
output: null
created_at: '2023-04-06T03:56:25.739590+00:00'
updated_at: '2023-04-10T20:25:40.190549+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - setup
verified: true
validated: true
---

# git-clone-dnsdumpster-repository

## Command

```bash
git clone https://github.com/nmmapper/dnsdumpster
```

## Description

This command clones the DNS Dumpster repository from GitHub, downloading the Python-based tool for subdomain enumeration. Use this as the first step in setting up the tool for reconnaissance against target domains.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/nmmapper/dnsdumpster | The GitHub repository URL for DNS Dumpster | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/nmmapper/dnsdumpster
```

### Advanced Usage

If behind a proxy, add Git config:

```bash
git config --global http.proxy http://proxy:port && git clone https://github.com/nmmapper/dnsdumpster
```

## Expected Output

Cloning into 'dnsdumpster'...
remote: Enumerating objects: X, done.
remote: Counting objects: 100% (X/X), done.
remote: Compressing objects: 100% (X/X), done.
Receiving objects: 100% (X/X), X KiB | X KiB/s, done.

The directory 'dnsdumpster' is created with the tool files.

## Related

- [[procedures/Subdomain-Enumeration-Using-DNS-Dumpster]]
- [[tools/DNS-Dumpster]]
