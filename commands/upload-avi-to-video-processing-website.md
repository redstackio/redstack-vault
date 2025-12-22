---
type: command
executor: web
data: Upload $_AVI_FILE via the website's file upload form
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - exploits
  - upload
verified: true
validated: true
---

# Upload AVI to Video Processing Website

## Command

Manual web action: Navigate to the target website's upload endpoint and submit the AVI file using the form.

## Description

Uploads the malicious AVI file to a video processing service vulnerable to FFmpeg exploits. This delivers the payload for automatic processing. If the site has an API, use curl; otherwise, use a browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_AVI_FILE | Path to the generated malicious AVI file | Yes |
| Website URL | URL of the vulnerable upload page | Yes |

## Examples

### Basic Usage

Use browser: Go to https://example-videoservice.com/upload, select $_AVI_FILE, and submit.

### Advanced Usage (API)

```bash
curl -F "file=@$_AVI_FILE" https://example-videoservice.com/api/upload
```

## Expected Output

Success response from the site, such as a job ID, processing URL, or confirmation message. The file is queued for FFmpeg transcoding.

## Related

- [[procedures/Exploit-FFmpeg-HLS-Vulnerability-via-Malicious-AVI-for-Arbitrary-File-Read]]
