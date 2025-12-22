---
data: >-
  preg_match('/X-Discourse-Username: (.*)/', implode("\n",
  $http_response_header), $name_matches);
tags:
  - parsing
  - regex
type: command
output: 'Matches array with username in $name_matches[1]'
executor: php
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.430Z'
id: b0ab147f-6fa3-4ec3-9293-92878a6a148c
verified: false
validated: true
submitted: true
---
# php-preg-match-username-header

## Command

```php
preg_match('/X-Discourse-Username: (.*)/', implode("\n", $http_response_header), $name_matches);
```

## Description

Extracts the username from HTTP response headers using regex after imploding the header array.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $http_response_header | Array of response headers | Yes |
| pattern | Regex for X-Discourse-Username | Yes |

## Examples

### Basic Usage

```php
$headers = implode("\n", $http_response_header);
preg_match('/X-Discourse-Username: (.*)/', $headers, $name_matches);
echo $name_matches[1];
```

### Advanced Usage

```php
if (!empty($name_matches)) { /* process */ }
```

## Expected Output

Array $name_matches with username in index 1.

## Related

- [[commands/php-preg-match-csrf-token]]
