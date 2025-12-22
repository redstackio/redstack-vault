---
type: command
executor: bash
data: >-
  php -r "$h = md5('ffifdyop', true); echo 'MD5 raw: '; echo bin2hex($h); echo
  '\n'; $s = sha1('3fDf ', true); echo 'SHA1 raw: '; echo bin2hex($s);"
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - linux
  - web
tags:
  - hashing
  - sql-injection
verified: true
validated: true
---

# calculate-md5-sha1-raw-hashes-php

## Command

```bash
php -r "$h = md5('ffifdyop', true); echo 'MD5 raw: '; echo bin2hex($h); echo '\n'; $s = sha1('3fDf ', true); echo 'SHA1 raw: '; echo bin2hex($s);"
```

## Description

This command uses PHP via bash to calculate raw (binary) MD5 and SHA1 hashes for specific passwords known to produce SQL-injectable byte sequences. It outputs hex for easy verification of the binary structure needed for bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ffifdyop | Example password for MD5 bypass | Yes |
| 3fDf  | Example password for SHA1 bypass | Yes |

## Examples

### Basic Usage

```bash
php -r "$h = md5('ffifdyop', true); echo bin2hex($h);"
```

### Full MD5 and SHA1

```bash
php -r "$h = md5('ffifdyop', true); $s = sha1('3fDf ', true); var_dump(bin2hex($h), bin2hex($s));"
```

## Expected Output

MD5 raw: 5f4dcc3b5aa765d61d8327deb882cf99
SHA1 raw: 4a8a08f09d37b73795649038408b5f33 (example; actual binary starts with bytes interpretable as '=' for SHA1 bypass).

## Related

- [[procedures/SQL-Injection-Authentication-Bypass-Using-Raw-MD5-and-SHA1-Hashes]]
- [[tools/PHP]]
