---
data: >-
  preg_match('/name="csrf-token" content="([a-zA-Z0-9\/=+\/]+)"/', $data,
  $matches);
tags:
  - parsing
  - regex
type: command
output: 'Matches array with token in $matches[1]'
executor: php
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.431Z'
id: db112cb9-b2c3-4149-9b4f-9f64a20e3f97
verified: false
validated: true
submitted: true
---
# php-preg-match-csrf-token

## Command

```php
preg_match('/name="csrf-token" content="([a-zA-Z0-9\/=+\/]+)"/', $data, $matches);
```

## Description

Extracts the CSRF token from the fetched HTML using regex pattern matching the meta tag.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $data | HTML content from fetch | Yes |
| pattern | Regex for csrf-token content | Yes |

## Examples

### Basic Usage

```php
preg_match('/name="csrf-token" content="([a-zA-Z0-9\/=+\/]+)"/', $data, $matches);
echo $matches[1];
```

### Advanced Usage

```php
if (preg_match(...)) { /* use $matches[1] */ }
```

## Expected Output

Array $matches with captured token in index 1.

## Related

- [[commands/php-preg-match-username-header]]
