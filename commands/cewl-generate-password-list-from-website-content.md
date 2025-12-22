---
id: a50e5264-3dfb-4fcb-8ad2-96f8bb4ea3ef
name: cewl-generate-password-list-from-website-content
type: command
executor: bash
data: cewl $_TARGET_IP -d $_DEPTH -m $_MIN_WORD_SIZE -w $_WORDLIST
output: |-
  root@kali:~# cewl -d 2 -m 5 http://10.10.10.10 -w words.txt
  CeWL 5.4.3 ... Generated 150 words
created_at: '2019-09-24T22:00:40.485122+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Web
tags:
  - wordlist
  - custom
verified: true
validated: true
---

# cewl-generate-password-list-from-website-content

## Command

```bash
cewl $_TARGET_IP -d $_DEPTH -m $_MIN_WORD_SIZE -w $_WORDLIST
```

## Description

Crawls site and generates wordlist from unique words.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target URL | Yes |
| -d $_DEPTH | Crawl depth | Yes |
| -m $_MIN_WORD_SIZE | Min word length | Yes |
| -w $_WORDLIST | Output file | Yes |

## Examples

### Basic Generation

```bash
cewl http://10.10.10.10 -d 2 -w list.txt
```

## Expected Output

Wordlist file with site-specific terms.

## Related

- [[procedures/enumerate-web-cms-for-usernames-and-passwords]]
