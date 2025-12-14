---
data: header('HTTP/1.0 401 Unauthorized');
tags:
  - phishing
  - http
type: command
executor: php
platforms:
  - Web
id: 34368c2d-172a-4575-8d55-96ec351811db
created_at: '2025-12-13T23:56:20.022Z'
updated_at: '2025-12-13T23:56:20.022Z'
verified: false
validated: true
submitted: true
---
# header-http-401-unauthorized

## Command

```php
header('HTTP/1.0 401 Unauthorized');
```

## Description

Sends an HTTP 401 status code to indicate unauthorized access, often combined with WWW-Authenticate for auth prompts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```php
header('HTTP/1.0 401 Unauthorized');
```

## Expected Output

401 Unauthorized response

## Related

- [[procedures/Demonstrate-Phishing-via-Redirect]]
- [[commands/header-www-authenticate]]
