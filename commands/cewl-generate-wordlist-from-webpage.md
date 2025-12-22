---
id: new-uuid-for-cewl
name: cewl-generate-wordlist-from-webpage
type: command
executor: bash
data: cewl -d 1 -w users.txt $_TARGET_URL
output: |-
  root@kali:~# cewl -d 1 -w users.txt https://example.com
  'CeWL 5.5.2 (https://github.com/digininja/CeWL)'
  ... (generates wordlist with scraped words)
created_at: '2023-01-01T00:00:00.000000+00:00'
updated_at: '2023-01-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - osint
  - scraping
verified: true
validated: true
---

# cewl-generate-wordlist-from-webpage

## Command

```bash
cewl -d 1 -w users.txt $_TARGET_URL
```

## Description

Crawls a website to generate a wordlist from page text, useful for names and terms.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d 1 | Crawl depth | Yes |
| -w users.txt | Output wordlist file | Yes |
| $_TARGET_URL | Website URL | Yes |

## Examples

### Basic Usage

```bash
cewl -d 2 -w names.txt https://target.com/about
```

## Expected Output

Wordlist file with extracted terms.

## Related

- [[procedures/build-user-list-from-public-webpage]]
