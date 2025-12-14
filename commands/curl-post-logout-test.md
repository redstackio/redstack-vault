---
data: 'curl -X POST https://target.com/logout -d '''' -b cookies.txt -c cookies.txt'
tags:
  - web
  - testing
  - csrf
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 7be5339b-5d62-43b5-8baf-a53b7736914e
created_at: '2025-12-14T17:27:42.494Z'
updated_at: '2025-12-14T17:27:42.494Z'
verified: false
validated: true
submitted: true
---
# curl-post-logout-test

## Command

```bash
curl -X POST https://target.com/logout -d '' -b cookies.txt -c cookies.txt
```

## Description

This command tests a POST request to the /logout endpoint using curl, simulating a CSRF attack by sending an empty body without CSRF tokens, while managing session cookies to verify if the logout succeeds.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `https://target.com/logout` | Target logout URL | Yes |
| `-d ''` | Empty data body for the POST | Yes |
| `-b cookies.txt` | Read cookies from file for authenticated session | Yes |
| `-c cookies.txt` | Save cookies to file post-request | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/logout -d '' -b cookies.txt -c cookies.txt
```

### Advanced Usage

```bash
curl -X POST https://target.com/logout -d '' --referer https://attacker.com -b cookies.txt -c cookies.txt -v
```

## Expected Output

HTTP response code 200 or 302 (redirect), with session cookie absent or cleared in the output file, indicating successful logout without CSRF validation.

## Related

- [[Related Procedure: Test-for-CSRF-on-Logout-Endpoint]]
