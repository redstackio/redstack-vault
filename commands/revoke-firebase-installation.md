---
data: >-
  curl -X DELETE
  https://firebaseinstallations.googleapis.com/v1/projects/shopify-ping/installations/eGSi2WuU9CLH8ZZYJKGsKm
  -H "Content-Type: application/json" -H "Authorization: [Firebase auth]"
tags:
  - revoke
  - firebase
type: command
output: 'HTTP/1.1 200 OK {}'
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:45.071Z'
id: 2e51955e-3780-4861-9e8b-3a8deb29e97d
verified: false
validated: true
submitted: true
---
# revoke-firebase-installation

## Command

```bash
curl -X DELETE https://firebaseinstallations.googleapis.com/v1/projects/shopify-ping/installations/eGSi2WuU9CLH8ZZYJKGsKm -H "Content-Type: application/json" -H "Authorization: [Firebase auth]"
```

## Description

Revokes Firebase installation token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Authorization` | Firebase header | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

200 OK empty.

## Related

- [[Related Procedure: Initiate-Logout-in-Shopify-Ping-App]]
