---
id: cmd-get-team-members
data: >-
  curl -X GET
  "https://fabric.io/api/v2/organizations/[orgid]/apps/[appid]/team_members" -H
  "Cookie: _fabric_session=..." -H "User-Agent: Mozilla/5.0 (Macintosh; Intel
  Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0"
tags:
  - api
  - recon
type: command
output: >-
  {"name":"alice","email":"alice@mailinator.com","id":"54aa4ab19ea6961359001260","is_activated":true,"is_admin":false}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:51.524Z'
verified: false
validated: true
submitted: true
---
# get-team-members

## Command

```bash
curl -X GET "https://fabric.io/api/v2/organizations/[orgid]/apps/[appid]/team_members" \
  -H "Cookie: _fabric_session=..." \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0"
```

## Description

This command retrieves the list of team members for a specific app in Fabric.io via the API, exposing user IDs, names, emails, and roles. Use it during reconnaissance to obtain identifiers for privilege escalation attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `[orgid]` | Organization ID from app settings URL | Yes |
| `[appid]` | App ID from app settings URL | Yes |
| `Cookie: _fabric_session=...` | Authenticated session cookie | Yes |
| `User-Agent` | Browser user agent string | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://fabric.io/api/v2/organizations/123/apps/456/team_members" -H "Cookie: _fabric_session=abc123"
```

### Advanced Usage

```bash
curl -X GET "https://fabric.io/api/v2/organizations/[orgid]/apps/[appid]/team_members" -H "Cookie: _fabric_session=..." | jq '.[].id'
```

## Expected Output

JSON array of user objects, e.g., [{"name":"alice","email":"alice@mailinator.com","id":"54aa4ab19ea6961359001260","is_activated":true,"is_admin":false}]. Look for the target user's ID and confirm non-admin status.

## Related

- [[commands/put-update-admin-status]]
- [[procedures/Retrieve-Team-Members-to-Obtain-User-ID]]
