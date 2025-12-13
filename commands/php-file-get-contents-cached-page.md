---
data: '$data = file_get_contents($discourse.''/u/''.$f.''.css'', false, $ctx);'
tags:
  - php
  - fetch
type: command
executor: php
platforms:
  - Web
id: 85b05f68-c37f-4bc3-bbb1-7b0331d53850
created_at: '2025-12-13T09:00:34.467Z'
updated_at: '2025-12-13T09:00:34.467Z'
verified: false
validated: true
submitted: true
---
# PHP File Get Contents Cached Page

## Command

```php
$data = file_get_contents($discourse.'/u/'.$f.'.css', false, $ctx);
```

## Description

Fetches the cached page content server-side from CloudFlare.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$f` | Random number for URL | Yes |
| `$ctx` | Stream context with ignore_errors=true | Yes |
| `$discourse` | Base URL of Discourse | Yes |

## Examples

### Basic Usage

```php
$data = file_get_contents('https://example.com/u/123.css', false, $ctx);
```

## Expected Output

HTML content including csrf-token and HTTP headers

## Related

- [[procedures/Fetch-Cached-Data-Server-Side]]
