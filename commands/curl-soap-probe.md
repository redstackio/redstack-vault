---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: >-
  curl -X POST $1 -H "Content-Type: text/xml" -d '<?xml
  version="1.0"?><soap:Envelope
  xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body></soap:Body></soap:Envelope>'
  -i
tags:
  - recon
  - soap
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:19.528Z'
verified: false
validated: true
submitted: true
---
# curl-soap-probe

## Command

```bash
curl -X POST http://target.com/soap -H "Content-Type: text/xml" -d '<?xml version="1.0"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body></soap:Body></soap:Envelope>' -i
```

## Description

This command probes a potential SOAP endpoint by sending an empty SOAP envelope to check for service availability and PHP handling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL (positional) | Target SOAP endpoint URL | Yes |
| -H | Custom header for Content-Type | Yes |
| -d | SOAP XML payload | Yes |
| -i | Include response headers | No |

## Examples

### Basic Usage

```bash
curl -X POST http://example.com/soap -H "Content-Type: text/xml" -d '<?xml version="1.0"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body></soap:Body></soap:Envelope>' -i
```

### Advanced Usage

```bash
curl -X POST https://target.com/wsdl.php -H "SOAPAction: "" -H "Content-Type: text/xml" -d '<empty-soap-payload>' --insecure
```

## Expected Output

HTTP response with 200 status and XML body, such as <soap:Fault> or WSDL schema, indicating active SOAP service.

## Related

- [[Related Procedure: Identify PHP SOAP Service]]
