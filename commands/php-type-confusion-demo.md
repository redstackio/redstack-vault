---
id: cmd-uuid-001
data: 'echo (''0e123'' != ''0e456'') ? ''Not equal'' : ''Equal'';'
tags:
  - demo
  - type-confusion
type: command
output: Equal
executor: php
platforms:
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:35.030Z'
verified: false
validated: true
submitted: true
---
# php-type-confusion-demo

## Command

```php
echo ('0e123' != '0e456') ? 'Not equal' : 'Equal';
```

## Description

This PHP one-liner demonstrates type confusion with the != operator, where strings '0e123' and '0e456' are treated as equal (both 0 in scientific notation), potentially leading to auth bypasses in vulnerable code.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Direct execution; no flags | No |

## Examples

### Basic Usage

```bash
php -r "echo ('0e123' != '0e456') ? 'Not equal' : 'Equal';"
```

### Advanced Usage

Embed in a script for broader testing:

```php
<?php
$token1 = '0e123';
$token2 = '0e456';
if ($token1 != $token2) {
    echo 'Bypass failed';
} else {
    echo 'Bypass succeeded - equal!'; // This runs
}
?>
```

## Expected Output

'Equal' - illustrating the unexpected equality due to type juggling.

## Related

- [[Related Procedure]]
