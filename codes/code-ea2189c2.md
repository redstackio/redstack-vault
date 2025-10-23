---
id: ea2189c2-cb77-4a6e-a074-202c747f8661
type: code
language: xml
verified: false
created_at: '2023-04-06T03:56:41.458387+00:00'
updated_at: '2023-04-10T20:24:48.989521+00:00'
---

# Code Snippet ea2189c2

**Language**: xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/fruits">
    <xsl:value-of select="system-property('xsl:vendor')"/>
  </xsl:template>
</xsl:stylesheet>
```


