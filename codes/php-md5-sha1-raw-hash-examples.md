---
type: code
language: php
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - web
tags:
  - hashing
  - bypass
validated: true
---

# php-md5-sha1-raw-hash-examples

## Code

```php
md5("ffifdyop", true) = 'or'6]!r,b
sha1("3fDf ", true) = Qu'='@[t- o_-!
```

## Description

This PHP code calculates raw binary MD5 and SHA1 hashes for specific passwords designed to produce byte sequences that inject SQL bypass code when inserted into queries. The output shows the binary representation, where the starting bytes ('or' for MD5, '=' for SHA1) enable string closure and tautology addition.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| ffifdyop | Password for MD5 bypass injection | ffifdyop |
| 3fDf  | Password for SHA1 bypass injection | 3fDf  |

## Usage

Execute in PHP to verify hash output before using the password in login submissions. Integrate into scripts for automated testing of hash-based SQLi. Useful in red team engagements targeting PHP apps with raw hashing.

## Detection

- PHP execution logs showing md5/sha1 with raw=true.
- Network requests with suspicious passwords like ffifdyop.
- Binary data in SQL parameters via app server logs.

## Related

- [[procedures/SQL-Injection-Authentication-Bypass-Using-Raw-MD5-and-SHA1-Hashes]]
- [[commands/calculate-md5-sha1-raw-hashes-php]]
