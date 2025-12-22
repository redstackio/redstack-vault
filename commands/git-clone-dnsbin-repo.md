---
id: 0c67c577-0362-4e19-bd35-b44336c243e5
name: git-clone-dnsbin-repo
type: command
executor: bash
data: 'git clone https://github.com/HoLyVieR/dnsbin.git'
output: null
created_at: '2023-04-06T03:55:57.488495+00:00'
updated_at: '2023-04-06T03:55:57.502968+00:00'
platforms:
  - Linux
tags:
  - setup
  - dnsbin
verified: true
validated: true
---

# git-clone-dnsbin-repo

## Command

```bash
git clone https://github.com/HoLyVieR/dnsbin.git
```

## Description

Clones the dnsbin repository from GitHub to the local machine. dnsbin is a tool for setting up a temporary DNS server to capture exfiltration data via subdomain queries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/HoLyVieR/dnsbin.git | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/HoLyVieR/dnsbin.git
```

### With Specific Directory

```bash
git clone https://github.com/HoLyVieR/dnsbin.git /path/to/dnsbin
```

## Expected Output

Cloning into 'dnsbin'...
remote: Enumerating objects: X, done.
remote: Counting objects: 100% (X/X), done.
remote: Compressing objects: 100% (X/X), done.
Receiving objects: 100% (X/X), X.XX KiB | XX.XX KiB/s, done.

## Related

- [[procedures/DNS-Data-Exfiltration-via-Command-Injection]]
- [[tools/dnsbin]]
