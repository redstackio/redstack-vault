---
id: cmd-wordfence-insert
data: >-
  if (!self::getDB()->queryWrite(sprintf("insert ignore into " . self::table() .
  " (name, val, autoload) values (%%s, X'%s', 'no')", $dataChunk),
  $chunkedValueKey . $chunks))
tags:
  - sqli
  - wordfence
type: command
output: 'Database insert, but potential SQLi if user-controlled'
executor: php
platforms:
  - WordPress
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.734Z'
verified: false
validated: true
submitted: true
---
# insert-ignore-with-sprintf-in-wordfence

## Command

```php
if (!self::getDB()->queryWrite(sprintf("insert ignore into " . self::table() . " (name, val, autoload) values (%%s, X'%s', 'no')", $dataChunk), $chunkedValueKey . $chunks))
```

## Description

Example from Wordfence plugin using sprintf for insert with hex-encoded value; vulnerable if $dataChunk is user-controlled and interacts with prepare() flaws or hex2bin failures.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| %%s | Placeholder for name | Yes |
| X'%s' | Hex value placeholder | Yes |
| $dataChunk | Data chunk for insertion | Yes |

## Examples

### Basic Usage

```php
sprintf("insert ignore into table (name, val) values (%s, X'%s')", $name, $val);
```

### Advanced Usage

```php
self::getDB()->queryWrite($sprintf_query, $key);
```

## Expected Output

Successful insert query, but SQLi if payload in $dataChunk breaks hex encoding.

## Related

- [[Related Procedure]]
