---
data: 'preg_match(''/name="csrf-token" content="([a-zA-Z0-9\/=+]+)"/'',$data,$matches);'
tags:
  - php
  - regex
type: command
executor: php
platforms:
  - Web
id: 3f4f0291-f968-46c3-a6b8-5bf949391042
created_at: '2025-12-13T09:00:34.463Z'
updated_at: '2025-12-13T09:00:34.463Z'
verified: false
validated: true
submitted: true
---
# PHP Preg Match CSRF Token

## Command

```php
preg_match('/name="csrf-token" content="([a-zA-Z0-9\/=+]+)"/',$data,$matches);
```

## Description

Extracts the CSRF token from the fetched HTML content using regex.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$data` | Fetched HTML | Yes |
| `pattern` | Regex for csrf-token | Yes |
| `$matches` | Array to store matches | Yes |

## Examples

### Basic Usage

```php
preg_match('/name="csrf-token" content="([a-zA-Z0-9\/=+]+)"/',$data,$matches);
```

## Expected Output

CSRF token value in $matches[1]

## Related

- [[procedures/Fetch-Cached-Data-Server-Side]]
