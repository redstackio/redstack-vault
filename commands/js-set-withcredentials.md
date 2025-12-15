---
data: xhr.withCredentials = true;
tags:
  - exploitation
  - auth
type: command
output: Cookies sent with request
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.426Z'
id: 9b3bb5e4-c16d-42a3-8f5e-c8daa88f6442
verified: false
validated: true
submitted: true
---
# js-set-withcredentials

## Command

```javascript
xhr.withCredentials = true;
```

## Description

Enables credentials mode on XMLHttpRequest to include cookies in cross-origin requests, simulating authenticated session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| withCredentials | true to send cookies | Yes |

## Examples

### Basic Usage

```javascript
xhr.withCredentials = true;
```

### Advanced Usage

```javascript
// For fetch alternative: fetch(url, {credentials: 'include'})
```

## Expected Output

Cookies included in subsequent send.

## Related

- [[commands/js-build-email-body]]
