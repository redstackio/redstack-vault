---
id: 8ba05cda-dd25-4c82-bd0e-880524aaa492
name: curl-facebook-access-token-debug
type: command
executor: bash
data: >-
  curl
  "https://developers.facebook.com/tools/debug/accesstoken/?access_token=$_ACCESS_TOKEN&version=v3.2"
output: null
created_at: '2023-04-06T03:55:53.110139+00:00'
updated_at: '2023-04-06T03:55:53.116074+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - api
  - debug
  - token
verified: true
validated: true
---

# curl-facebook-access-token-debug

## Command

```bash
curl "https://developers.facebook.com/tools/debug/accesstoken/?access_token=$_ACCESS_TOKEN&version=v3.2"
```

## Description

This command uses curl to query Facebook's Access Token Debug tool, providing detailed information about a specified Access Token. It is used in scenarios where an attacker has obtained a token and needs to evaluate its validity, associated user, permissions, and expiration without making broader API calls. The output is JSON, making it suitable for parsing in automated scripts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ACCESS_TOKEN | The Facebook Access Token to debug (alphanumeric string) | Yes |
| version=v3.2 | Specifies the Graph API version; v3.2 is used for compatibility with older tokens | No (default if omitted) |

## Examples

### Basic Usage

```bash
curl "https://developers.facebook.com/tools/debug/accesstoken/?access_token=EAA...abc123&version=v3.2"
```

### Advanced Usage (with JSON Parsing)

```bash
curl "https://developers.facebook.com/tools/debug/accesstoken/?access_token=EAA...abc123&version=v3.2" | jq '.data'
```

## Expected Output

Successful execution returns a JSON object like:

```json
{
  "data": {
    "app_id": 1234567890,
    "type": "USER",
    "application": "My App",
    "expires_at": 1699999999,
    "is_valid": true,
    "issued_at": 1690000000,
    "scopes": ["public_profile", "email", "user_posts"],
    "user_id": 123456789
  }
}
```

If invalid: {"data": {"is_valid": false, "error": {"message": "..."}}}

## Related

- [[procedures/Debug-Facebook-Access-Token]] (procedure that uses this command)
- [[tools/cURL]] (base tool documentation)
