---
data: >-
  preg_match('/X-Discourse-Username: (.*)/', implode("\n",
  $http_response_header), $name_matches);
tags:
  - php
  - regex
type: command
executor: php
platforms:
  - Web
id: b093391c-27c3-4fcf-b672-410ec530f172
created_at: '2025-12-13T09:00:34.460Z'
updated_at: '2025-12-13T09:00:34.460Z'
verified: false
validated: true
submitted: true
---
# PHP Preg Match Username

## Command

```php
preg_match('/X-Discourse-Username: (.*)/', implode("\n", $http_response_header), $name_matches);
```

## Description

Extracts the username from the HTTP response headers using regex.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `string` | Imploded HTTP headers | Yes |
| `pattern` | Regex for username header | Yes |
| `$name_matches` | Array to store matches | Yes |

## Examples

### Basic Usage

```php
preg_match('/X-Discourse-Username: (.*)/', implode("\n", $http_response_header), $name_matches);
```

## Expected Output

Username in $name_matches[1]

## Related

- [[procedures/Fetch-Cached-Data-Server-Side]]
