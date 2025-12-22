---
id: 4234ae79-c0a7-41f2-a672-b9ee893fdbe0
name: php-execute-empty-array-hash
type: command
executor: php
data: 'php -r ''var_dump(sha1([])); var_dump(md5([]));'''
output: |-
  NULL#1  NULL
  #2  NULL
created_at: '2023-04-06T03:56:40.673509+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - php
  - hashing
  - type-juggling
verified: true
validated: true
---

# php-execute-empty-array-hash

## Command

```bash
php -r 'var_dump(sha1([])); var_dump(md5([]));'
```

## Description

This command executes a PHP one-liner to hash an empty array using sha1() and md5(), demonstrating that both return NULL due to invalid input type. Use this during vulnerability testing to verify PHP type juggling behaviors in authentication systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-r` | Execute the following PHP code directly | Yes |
| `'var_dump(sha1([])); var_dump(md5([]));'` | The PHP code snippet to run; [] represents empty array | Yes |

## Examples

### Basic Usage

```bash
php -r 'var_dump(sha1([])); var_dump(md5([]));'
```

### Advanced Usage

To output without var_dump for scripting:

```bash
php -r 'echo sha1([]) . "\n" . md5([]);'
```

## Expected Output

```
NULL#1  NULL
#2  NULL
```

This shows two NULL values, confirming the hashing behavior. In a vulnerable auth context, this NULL can loosely equal other values like 0 or '', enabling bypass.

## Related

- [[procedures/Demonstrate-PHP-Type-Juggling-with-Empty-Array-Hashing]]
- [[codes/PHP-Empty-Array-Hash-Demonstration]]
