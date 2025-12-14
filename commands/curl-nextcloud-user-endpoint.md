---
id: cmd-001
data: >-
  curl -H "OCS-APIRequest: true" -u username:password
  https://nextcloud.example.com/ocs/v1.php/cloud/user?format=json
tags:
  - api
  - curl
  - nextcloud
type: command
output: >-
  {\"ocs\":{\"meta\":{\"status\":\"ok\",\"statuscode\":100,\"message\":null},\"data\":{\"users\":[{\"displayname\":\"Admin\",\"storageLocation\":\"/home/bohwaz/www/tmp/nextcloud/data/bohwaz\",\"...\"}]}}
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.088Z'
verified: false
validated: true
submitted: true
---
# curl-nextcloud-user-endpoint

## Command

```bash
curl -H "OCS-APIRequest: true" -u username:password https://nextcloud.example.com/ocs/v1.php/cloud/user?format=json
```

## Description

This command queries the Nextcloud OCS API to retrieve user information in JSON format, potentially disclosing the server storage path. Use it after authentication to perform reconnaissance on the instance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "OCS-APIRequest: true"` | Header required for OCS API compatibility | Yes |
| `-u username:password` | Basic authentication credentials | Yes |
| `https://nextcloud.example.com/ocs/v1.php/cloud/user?format=json` | Target endpoint URL with JSON format | Yes |

## Examples

### Basic Usage

```bash
curl -H "OCS-APIRequest: true" -u admin:pass https://target.com/ocs/v1.php/cloud/user?format=json
```

### Advanced Usage

```bash
curl -H "OCS-APIRequest: true" -b cookies.txt -X GET https://target.com/ocs/v1.php/cloud/user?format=json -o response.json
```

> Uses session cookies and saves output to file.

## Expected Output

JSON response with user data, including `storageLocation` field like `{\"ocs\":{\"data\":{\"users\":[{\"storageLocation\":\"/path/to/data\"}]}}}`. Success indicated by statuscode 100.

## Related

- [[Related Procedure: Query-Nextcloud-Cloud-User-API]]
