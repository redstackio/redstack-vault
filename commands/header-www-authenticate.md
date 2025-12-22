---
data: 'header(''WWW-Authenticate: Basic realm="Log in to HackerOne"'');'
tags:
  - phishing
  - http
type: command
executor: php
platforms:
  - Web
id: db97dc32-a6bf-4ef8-8097-4e48595a395e
created_at: '2025-12-13T23:56:20.026Z'
updated_at: '2025-12-13T23:56:20.026Z'
verified: false
validated: true
submitted: true
---
# header-www-authenticate

## Command

```php
header('WWW-Authenticate: Basic realm="Log in to HackerOne"');
```

## Description

Sends an HTTP header to trigger a basic authentication prompt in the browser, used in phishing scenarios to mimic login dialogs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `WWW-Authenticate` | Specifies Basic auth with realm message | Yes |

## Examples

### Basic Usage

```php
header('WWW-Authenticate: Basic realm="Log in to HackerOne"');
```

## Expected Output

Browser displays authentication dialog

## Related

- [[procedures/Demonstrate-Phishing-via-Redirect]]
- [[commands/header-http-401-unauthorized]]
