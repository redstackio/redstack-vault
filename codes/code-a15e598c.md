---
id: a15e598c-97d7-43ab-98c9-b7e4196cf4c4
type: code
language: xml
verified: false
created_at: '2023-04-06T03:56:41.519856+00:00'
updated_at: '2023-04-10T20:24:50.765436+00:00'
---

# Code Snippet a15e598c

**Language**: xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:msxsl="urn:schemas-microsoft-com:xslt"
xmlns:user="urn:my-scripts">

<msxsl:script language = "C#" implements-prefix = "user">
<![CDATA[
public string execute(){
System.Diagnostics.Process proc = new System.Diagnostics.Process();
proc.StartInfo.FileName= "C:\\windows\\system32\\cmd.exe";
proc.StartInfo.RedirectStandardOutput = true;
proc.StartInfo.UseShellExecute = false;
proc.StartInfo.Arguments = "/c dir";
proc.Start();
proc.WaitForExit();
return proc.StandardOutput.ReadToEnd();
}
]]>
</msxsl:script>

<xsl:template match="/fruits">
List Directory Contents:
<xsl:value-of select="user:execute()"/>
</xsl:template>
</xsl:stylesheet>
```


