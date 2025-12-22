---
id: ea2189c2-cb77-4a6e-a074-202c747f8661
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:41.458387+00:00'
updated_at: '2023-04-10T20:24:48.989521+00:00'
tags:
  - xslt-injection
  - vendor-enumeration
  - payload
platforms:
  - Web
validated: true
---

# XSLT-Vendor-Extraction-Payload

## Code

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/fruits">
    <xsl:value-of select="system-property('xsl:vendor')"/>
  </xsl:template>
</xsl:stylesheet>
```

## Description

This XSLT payload is designed to extract the vendor name of the target XSLT processor during an injection attack. It uses the `system-property('xsl:vendor')` function within a simple stylesheet template, matching a root XML element (e.g., '/fruits') to output the vendor string directly in the transformation result. This is a minimal, focused snippet for initial reconnaissance in XSLT injection scenarios.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `/fruits` | Root element to match in the input XML; adjust if the target's XML structure differs | `/data` or `/input` |

## Usage

Embed this payload into a user-controlled input field that the application processes as an XSLT stylesheet, such as a parameter in an HTTP request (e.g., via Burp Suite or curl). Pair it with a simple input XML like `<fruits></fruits>` to trigger the transformation. The output will be the vendor name, e.g., 'libxml'. Used in procedures like [[procedures/Extract-XSLT-Processor-Vendor-and-Version-via-Injection]] for fingerprinting the processor before deeper exploitation.

## Detection

- Monitor application logs for XSLT transformation errors or unusual `system-property` calls.
- WAF rules detecting `<xsl:stylesheet>` or `system-property('xsl:vendor')` in inputs.
- Output anomalies like unexpected vendor strings in response bodies.

## Related

- [[procedures/Extract-XSLT-Processor-Vendor-and-Version-via-Injection]]
