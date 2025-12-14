---
id: cmd-curl-conversion-001
data: >-
  curl -X POST https://github.enterprise/api/user/convert-to-org -H
  "Authorization: token USER_TOKEN" -H "Content-Type: application/json" -d
  '{"organization_name": "target_org", "billing_email": "admin@example.com"}'
tags:
  - api
  - github
  - conversion
type: command
output: null
executor: bash
platforms:
  - GitHub Enterprise Server
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:17.979Z'
verified: false
validated: true
submitted: true
---
# curl-initiate-conversion

## Command

```bash
curl -X POST https://github.enterprise/api/user/convert-to-org -H "Authorization: token USER_TOKEN" -H "Content-Type: application/json" -d '{"organization_name": "target_org", "billing_email": "admin@example.com"}'
```

## Description

Initiates the user account to organization conversion in GitHub Enterprise Server via API, creating the race condition window for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method for creation | Yes |
| `-H "Authorization: token USER_TOKEN"` | Auth header with personal access token | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload type | Yes |
| `-d '{...}'` | JSON data for org name and email | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://github.enterprise/api/user/convert-to-org -H "Authorization: token ghp_abc123" -d '{"organization_name": "test_org"}'
```

### Advanced Usage

```bash
curl -X POST https://github.enterprise/api/user/convert-to-org -H "Authorization: token ghp_abc123" -d '{"organization_name": "test_org", "billing_email": "user@domain.com", "description": "Test org"}'
```

## Expected Output

JSON response like {"id": 123, "login": "target_org", "status": "converting"}, indicating initiation without errors.

## Related

- [[Related Procedure: Exploit-GitHub-User-to-Org-Race-Condition]]
