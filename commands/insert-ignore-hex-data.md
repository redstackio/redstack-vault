---
id: cmd-wordfence-hex-insert
data: >-
  if (!self::getDB()->queryWrite(sprintf("insert ignore into " . self::table() .
  " (name, val, autoload) values (%%s, X'%s', 'no')", $dataChunk),
  $chunkedValueKey . $chunks))
tags:
  - sqli
  - wordpress
type: command
output: null
executor: php
platforms:
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.592Z'
verified: false
validated: true
submitted: true
---
# insert-ignore-hex-data

## Command

```php
if (!self::getDB()->queryWrite(sprintf("insert ignore into " . self::table() . " (name, val, autoload) values (%%s, X'%s', 'no')", $dataChunk), $chunkedValueKey . $chunks))
```

## Description

From Wordfence plugin, uses sprintf with placeholders for hex binary data insertion, vulnerable to SQLi if $dataChunk is user-controlled and interacts with prepare() flaws via hex2bin/bin2hex.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| %%s | Escaped %s placeholder | Yes |
| X'%s' | Hex format for binary data | Yes |
| $dataChunk | User-controlled chunk | Yes |

## Examples

### Basic Usage

```php
$dataChunk = 'user_input';
self::getDB()->queryWrite(sprintf("insert ignore into table (name) values (%%s)", $dataChunk));
```

### Advanced Usage

```php
$chunks = bin2hex($dataChunk);
// Insert with hex
```

## Expected Output

Database insert query, but SQLi possible via format string manipulation, e.g., injected SQL in chunk.

## Related

- [[Related Procedure]]
