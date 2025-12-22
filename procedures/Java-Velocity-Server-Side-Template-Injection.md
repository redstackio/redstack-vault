---
id: 2faa5e25-1d13-46bd-aa8a-097d9531239d
name: Java-Velocity-Server-Side-Template-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:40.381440+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - Java
  - Velocity
  - Server-Side-Template-Injection
  - SSTI
  - RCE
commands:
  - '[[commands/curl-velocity-ssti-inject]]'
platforms:
  - Web
  - Java
tools: []
validated: true
---

# Java-Velocity-Server-Side-Template-Injection

## Summary

This procedure demonstrates how to exploit Server-Side Template Injection (SSTI) vulnerabilities in Java web applications using the Velocity template engine to achieve remote code execution (RCE). By injecting malicious Velocity Template Language (VTL) payloads into user-controlled inputs, attackers can execute arbitrary system commands on the server, such as retrieving the current user identity with 'whoami'.

## Description

Server-Side Template Injection occurs when user input is unsafely interpolated into server-side templates processed by engines like Apache Velocity in Java applications. Velocity allows dynamic content generation but, if not properly sanitized, enables attackers to inject VTL directives that invoke Java classes and methods, leading to RCE. This technique targets web applications where templates are rendered from parameters like URLs, forms, or headers. In a typical scenario, an attacker identifies a vulnerable endpoint (e.g., a search or profile page), crafts a payload to access Java's Runtime class for command execution, and observes the output in the response. Success grants server-side access, potentially escalating to data exfiltration or persistence. This procedure assumes basic web access and focuses on detection, payload crafting, and injection for educational or red team purposes.

## Requirements

1. Network access to a Java web application using Velocity for server-side templating.
2. Identification of a user-controlled input point that is interpolated into Velocity templates (e.g., via error messages, rendered pages, or logs).
3. Tools for HTTP request manipulation, such as curl or a proxy like Burp Suite.
4. Basic knowledge of VTL syntax and Java reflection to chain class inspections.

## Defense

- Implement strict input validation and sanitization to block VTL directives (e.g., whitelist allowed characters, escape special sequences like $ and #).
- Configure Velocity to run in secure mode with restricted access to Java classes (e.g., disable introspection via velocity.properties).
- Use web application firewalls (WAFs) to detect and block common SSTI patterns, such as Runtime.exec invocations.
- Enable comprehensive logging of template rendering and monitor for anomalous Java method calls or command executions.
- Regularly audit and update dependencies, including Velocity engine versions, to patch known vulnerabilities.

## Objectives

1. Identify and confirm a Velocity SSTI vulnerability in the target application.
2. Craft and inject a VTL payload to execute arbitrary server-side commands.
3. Retrieve command output to verify RCE and gather initial reconnaissance (e.g., current user).
4. Establish a foundation for further exploitation, such as privilege escalation or data access.

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Probe the application to find inputs that are processed by Velocity templates. Look for pages that dynamically render user input, such as search results or error pages, where injected content appears unescaped.

Use manual testing or fuzzing with common SSTI probes like '${7*7}' to detect if Velocity evaluates expressions (expected output: 49).

### Step 2: Craft VTL Payload for RCE

**Context**: Construct a payload using VTL to inspect and invoke Java classes for command execution. This step leverages the provided code snippet to run 'whoami' and capture output.

Embed the payload [[codes/Velocity-SSTI-Whoami-Payload]] into the vulnerable parameter.

### Step 3: Inject Payload and Execute

**Context**: Send the crafted payload via an HTTP request to the vulnerable endpoint. This triggers the template engine to evaluate the VTL, executing the command and returning output in the response.

**Command** ([[commands/curl-velocity-ssti-inject]]):
```bash
curl -X GET "http://target.com/vulnerable?param=$_PAYLOAD" -v
```

> This command injects the VTL payload into the 'param' query parameter. Replace $_PAYLOAD with the URL-encoded Velocity code. The -v flag provides verbose output to inspect headers and body for command results. Expected behavior: The server processes the template, runs 'whoami', and echoes the username in the response body or error message.

### Step 4: Verify and Analyze Output

**Context**: Check the response for successful command execution. If 'whoami' output appears (e.g., 'www-data' or 'tomcat'), the SSTI is confirmed with RCE. If not, adjust encoding or try alternative injection points.

Manually inspect the response body for the username string. For further actions, modify the payload to execute other commands like 'id' or 'ls'.
