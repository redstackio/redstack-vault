---
data: >-
  xhr.setRequestHeader('Accept', 'text/html');
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
tags:
  - exploitation
  - http
type: command
output: Headers applied to request
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.427Z'
id: a5e1f52e-6815-4c0c-b780-3c8aa922f977
verified: false
validated: true
submitted: true
---
# js-set-request-headers

## Command

```javascript
xhr.setRequestHeader('Accept', 'text/html'); xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
```

## Description

Sets HTTP headers on the XMLHttpRequest to mimic a browser form submission for the email change.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Accept | 'text/html' to request HTML response | Yes |
| Content-Type | 'application/x-www-form-urlencoded' for form data | Yes |

## Examples

### Basic Usage

```javascript
xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
```

### Advanced Usage

```javascript
xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
```

## Expected Output

Headers successfully set on xhr object.

## Related

- [[commands/js-set-withcredentials]]
