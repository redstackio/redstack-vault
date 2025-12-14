---
id: cmd-uuid-1
data: >-
  if(count($params) != count($params,COUNT_RECURSIVE)){ throw new
  \InvalidArgumentException("Invalid params"); }
tags:
  - validation
  - php
type: command
output: Throws InvalidArgumentException if $params is not one-dimensional
executor: php
platforms:
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.541Z'
verified: false
validated: true
submitted: true
---
# validate-params-1d-array

## Command

```php
if(count($params) != count($params,COUNT_RECURSIVE)){ throw new \InvalidArgumentException("Invalid params"); }
```

## Description

This PHP code snippet validates that the $params array is one-dimensional by comparing its non-recursive count to the recursive count. If they differ, it indicates nested elements, triggering an exception to prevent processing and potential error-based path disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$params` | The input array to validate | Yes |
| `COUNT_RECURSIVE` | PHP constant (2) for recursive array counting | Yes (built-in) |

## Examples

### Basic Usage

```php
$params = ['key' => 'value']; // 1D
if(count($params) != count($params,COUNT_RECURSIVE)){ throw new \InvalidArgumentException("Invalid params"); } // No throw
```

### Advanced Usage (Invalid Case)

```php
$params = ['key' => ['nested']]; // Multi-D
if(count($params) != count($params,COUNT_RECURSIVE)){ throw new \InvalidArgumentException("Invalid params"); } // Throws exception
```

## Expected Output

For valid 1D arrays: No output, continues execution. For invalid multi-D arrays: PHP Fatal error or exception with message "Invalid params", without revealing server paths.

## Related

- [[procedures/Propose-Array-Validation-Fix]]
