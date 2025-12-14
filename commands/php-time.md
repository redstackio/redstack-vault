---
id: cmd-php-time-001
data: echo time();
tags:
  - timestamp
  - prediction
type: command
output: 'Current Unix timestamp (e.g., 1600080000)'
executor: php
platforms:
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.085Z'
verified: false
validated: true
submitted: true
---
# php-time

## Command

```php
echo time();
```

## Description

This PHP command returns the current Unix timestamp as an integer, used internally by Concrete CMS for naming update directories and generating ccm_tokens. In attacks, it's exploited to predict directory names by approximating the unzip time from the ccm_token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Built-in function, no parameters | No |

## Examples

### Basic Usage

```php
echo time();
```

### Advanced Usage

Run in a script to get timestamp at specific moment:

```php
<?php
// Approximate for prediction
$approx_time = time() - 60; // Subtract seconds if needed
echo $approx_time;
?>
```

## Expected Output

A single integer representing seconds since Unix epoch, e.g., 1696152000.

## Related

- [[procedures/Predict-Update-Directory-Using-CCM-Token]]
