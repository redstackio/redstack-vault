---
id: 658df61c-8d59-4acf-9f61-1cf550be26d5
name: strings-search-raw-data-for-human-readable-strings
type: command
executor: bash
data: strings $_DUMP | grep $_STRING
output: |-
  root@kali:~# strings dump | grep password
  ... admin:wh3r3sth3b33f
created_at: '2020-03-31T05:01:26.325180+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - memory-analysis
  - strings
verified: true
validated: true
---

# strings-search-raw-data-for-human-readable-strings

## Command

```bash
strings $_DUMP | grep $_STRING
```

## Description

Extracts and searches for printable strings in binary files like dumps.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DUMP | Input dump file | Yes |
| $_STRING | Search term | Yes |

## Examples

### Basic Usage

```bash
strings lsass.dmp | grep password
```

### With Context

```bash
strings lsass.dmp | grep -A 2 -i key
```

## Expected Output

Matching strings.

## Related

- [[procedures/find-interesting-strings-in-raw-memory-dump]]
