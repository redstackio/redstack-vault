---
id: a50e5264-3dfb-4fcb-8ad2-96f8bb4ea3ef
name: cewl-generate-wordlist-from-website
type: command
executor: bash
data: cewl $_TARGET_IP -d $_DEPTH -m $_MAX_SIZE -w $_WORDLIST
output: 'CeWL 5.4.3 (Arkanoid) Robin Wood (robin@digi.ninja) (https://digi.ninja/)'
created_at: '2019-09-24T22:00:40.485122+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - wordlist
  - crawling
verified: true
validated: true
---

# cewl-generate-wordlist-from-website

## Command

```bash
cewl $_TARGET_IP -d $_DEPTH -m $_MAX_SIZE -w $_WORDLIST
```

## Description

Crawls a website to generate a custom wordlist from page content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | URL (e.g., http://10.10.10.10) | Yes |
| -d $_DEPTH | Crawl depth | No |
| -m $_MAX_SIZE | Min word length | No |
| -w $_WORDLIST | Output file | Yes |

## Examples

### Basic Usage

```bash
cewl http://10.10.10.10 -d 2 -m 5 -w words.txt
```

## Expected Output

Description: Wordlist file with extracted terms; console shows progress.

## Related

- [[procedures/Build-Custom-Password-List-for-Dictionary-Attack]]
- [[tools/CeWL]]
