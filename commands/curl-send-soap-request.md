---
data: 'curl -X POST [endpoint] -H "Content-Type: text/xml" -d ''[xml_payload]'''
tags:
  - http
  - post
  - soap
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 8c03df6a-3e77-409e-bb55-55de8b84b0de
created_at: '2025-12-13T09:00:27.916Z'
updated_at: '2025-12-13T09:00:27.916Z'
verified: false
validated: true
submitted: true
---
# Curl Send SOAP Request

## Command

```bash
curl -X POST [endpoint] -H "Content-Type: text/xml" -d '[xml_payload]'
```

## Description

This command uses curl to send a POST request with XML data to a SOAP endpoint, useful for testing and exploiting XML-based vulnerabilities like XXE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Content-Type: text/xml"` | Sets XML content type | Yes |
| `-d '[xml_payload]'` | XML data to send | Yes |
| `--data @file.xml` | Alternative to send from file | No |

## Examples

### Basic Usage

```bash
curl -X POST https://www.starbucks.com.sg/RestApi/soap11 -H "Content-Type: text/xml" -d '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Body><test/></soapenv:Body></soapenv:Envelope>'
```

### Advanced Usage

```bash
curl -X POST https://www.starbucks.com.sg/RestApi/soap11 -H "Content-Type: text/xml" --data @xxe_payload.xml
```

## Expected Output

A SOAP response XML, potentially containing exploited data like file contents.

## Related
- [[procedures/Identify-SOAP-Endpoint]]
- [[procedures/Exploit-XXE-for-File-Reading]]
