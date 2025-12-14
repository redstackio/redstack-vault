---
data: >-
  curl -c cookies.txt -d "email=your@email.com&password=yourpass"
  https://www.semrush.com/login
tags:
  - authentication
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.771Z'
id: af28487c-903b-4a37-85a5-1d46b4784b22
verified: false
validated: true
submitted: true
---
# curl-login-semrush

## Command

```bash
curl -c cookies.txt -d "email=your@email.com&password=yourpass" https://www.semrush.com/login
```

## Description

This command authenticates to the Semrush login endpoint using POST data for credentials and saves the resulting session cookie to a file for use in subsequent requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c cookies.txt` | Saves cookies to the specified file | Yes |
| `-d "email=...&password=..."` | Form data for login credentials | Yes |
| `https://www.semrush.com/login` | Login endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -c cookies.txt -d "email=user@example.com&password=pass123" https://www.semrush.com/login
```

### Advanced Usage

```bash
curl -c cookies.txt -d "email=user@example.com&password=pass123" -L https://www.semrush.com/login
```

## Expected Output

Redirect (302) to the dashboard or success message, with cookies.txt containing session tokens like 'session=abc123'.

## Related

- [[Related Procedure|procedures/Exploit-Unrestricted-File-Upload-in-Semrush-My-Reports]]
