---
data: >-
  curl -c cookies.txt -d "username=validuser&password=validpass" -X POST
  https://app.starbucks.com/login
tags:
  - auth
  - login
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: a07da0f4-a6e3-4fa6-82bb-b8f3d277f592
created_at: '2025-12-14T17:31:52.941Z'
updated_at: '2025-12-14T17:31:52.941Z'
verified: false
validated: true
submitted: true
---
# curl-login-starbucks

## Command

```bash
curl -c cookies.txt -d "username=validuser&password=validpass" -X POST https://app.starbucks.com/login
```

## Description

This command performs a login to the Starbucks web app using curl, saving the authentication cookie to a file for later use in authenticated requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c cookies.txt` | Save cookies to the specified file | Yes |
| `-d "username=validuser&password=validpass"` | POST data with credentials | Yes |
| `-X POST` | Specify POST method | Yes |
| `https://app.starbucks.com/login` | Target login endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -c cookies.txt -d "username=validuser&password=validpass" -X POST https://app.starbucks.com/login
```

### Advanced Usage

```bash
curl -c cookies.txt -d "username=validuser&password=validpass&remember=true" -X POST -H "User-Agent: Mozilla/5.0" https://app.starbucks.com/login
```

## Expected Output

HTTP response code 200 or 302 (redirect), with headers including Set-Cookie: session_id=abc123; Path=/; HttpOnly. The cookies.txt file will contain the session details.

## Related

- [[Related Procedure: Obtain-Starbucks-Auth-Cookie]]
