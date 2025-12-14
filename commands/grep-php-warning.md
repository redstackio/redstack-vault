---
id: cmd-grep-warning-001
data: grep -i "warning" response.txt
tags:
  - text-processing
  - error-parsing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.992Z'
verified: false
validated: true
submitted: true
---
# grep-php-warning

## Command

```bash
grep -i "warning" response.txt
```

## Description

Searches for PHP warning messages in a captured response file to extract path disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Case-insensitive search | No |
| Pattern | 'warning' for PHP errors | Yes |
| File | Response file | Yes |

## Examples

### Basic Usage

```bash
grep -i "warning" response.txt
```

### Advanced Usage

```bash
grep -i "trim()" response.txt | sed 's/.*in \(.*\).*/\1/'
```

## Expected Output

Lines containing 'Warning: trim() expects parameter 1 to be string, array given in /path/to/file.php on line X'.

## Related

- [[Related Procedure]]
