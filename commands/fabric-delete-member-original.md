---
id: cmd-fabric-delete-original
data: >-
  curl -X DELETE
  'https://fabric.io/api/v3/accounts/54c1e78b9ea696b3cb00026a/organizations/54aa36e3937ae35559011d17/leave'
  -H 'Host: fabric.io' -H 'Authorization: Bearer [TOKEN]'
tags:
  - api-delete
  - fabric-io
type: command
output: |-
  HTTP/1.1 200 OK
  {"status":"success"}
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:58.764Z'
verified: false
validated: true
submitted: true
---
# fabric-delete-member-original

## Command

```bash
curl -X DELETE 'https://fabric.io/api/v3/accounts/54c1e78b9ea696b3cb00026a/organizations/54aa36e3937ae35559011d17/leave' -H 'Host: fabric.io' -H 'Authorization: Bearer [TOKEN]'
```

## Description

Sends a legitimate DELETE request to remove a member from the sender's own organization in Fabric.io, used to capture the request format for interception.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X DELETE` | Specifies HTTP DELETE method | Yes |
| `accounts/{account_id}` | ID of the member to remove (e.g., 54c1e78b9ea696b3cb00026a) | Yes |
| `organizations/{org_id}` | ID of the organization (e.g., 54aa36e3937ae35559011d17) | Yes |
| `-H 'Authorization: Bearer [TOKEN]'` | Auth token from session | Yes |

## Examples

### Basic Usage

```bash
curl -X DELETE 'https://fabric.io/api/v3/accounts/54c1e78b9ea696b3cb00026a/organizations/54aa36e3937ae35559011d17/leave' -H 'Host: fabric.io' -H 'Authorization: Bearer [TOKEN]'
```

### Advanced Usage

Add verbose output:

```bash
curl -v -X DELETE 'https://fabric.io/api/v3/accounts/54c1e78b9ea696b3cb00026a/organizations/54aa36e3937ae35559011d17/leave' -H 'Host: fabric.io' -H 'Authorization: Bearer [TOKEN]'
```

## Expected Output

HTTP 200 OK with JSON success response, confirming member removal from own org.

## Related

- [[commands/fabric-delete-member-modified]]
- [[procedures/Intercept-DELETE-Request-with-Burp-Proxy]]
