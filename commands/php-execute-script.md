---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: php script.php
tags:
  - php
  - execution
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.274Z'
verified: false
validated: true
submitted: true
---
# php-execute-script

## Command

```bash
php script.php
```

## Description

Executes a PHP script from the command line, useful for testing vulnerabilities like memory corruption in functions such as implode(). This command runs the script in the PHP interpreter, simulating server-side execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `script.php` | Path to the PHP file to execute | Yes |
| `-r "code"` | Inline PHP code to run without a file | No |
| `-l` | Syntax check only | No |

## Examples

### Basic Usage

```bash
php vulnerable_script.php
```

### Advanced Usage

```bash
php -r "\$arr = str_repeat('a', 1000000); echo implode('', [\$arr]);"
```

## Expected Output

If successful and non-vulnerable: Script output or empty. If vulnerable: Segmentation fault (core dumped) or abrupt termination indicating crash.

## Related

- [[Related Procedure|procedures/Trigger-PHP-implode-Crash]]
