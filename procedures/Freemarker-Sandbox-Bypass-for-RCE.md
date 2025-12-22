---
id: 6ab3fc32-12c4-4a1c-8e16-58c32248d66c
name: Freemarker-Sandbox-Bypass-for-RCE
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.075018+00:00'
updated_at: '2023-04-10T20:23:38.534109+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
  - >-
    [[techniques/Virtualization/Sandbox Evasion|T1497 - Virtualization/Sandbox
    Evasion]]
sub_techniques: []
tags:
  - '[[tags/Freemarker]]'
  - '[[tags/Freemarker - Sandbox bypass]]'
  - '[[tags/Server Side Template Injection]]'
commands: []
platforms:
  - Web
  - Java
tools: []
validated: true
---

# Freemarker-Sandbox-Bypass-for-RCE

## Summary

This procedure demonstrates how to bypass the built-in sandbox in Apache FreeMarker Template Engine to achieve remote code execution (RCE) via server-side template injection (SSTI). It targets vulnerable web applications using FreeMarker for dynamic content generation, allowing attackers to load restricted classes and execute arbitrary system commands on the server.

## Description

FreeMarker is a Java-based template engine commonly used in web applications to merge templates with data for generating dynamic HTML or other outputs. If user input is not properly sanitized and is passed directly into FreeMarker templates, it can lead to SSTI vulnerabilities. FreeMarker includes a sandbox to restrict access to dangerous Java classes and methods, but this can be bypassed by accessing the class loader through seemingly benign objects like 'article' (often available in default configurations). The bypass involves loading the ObjectWrapper and Execute utility classes to instantiate and invoke command execution. This technique is particularly effective against outdated or misconfigured FreeMarker versions (e.g., pre-2.3.32) in environments like Spring Boot or custom Java web apps. Successful exploitation grants shell access, enabling data exfiltration, persistence, or further lateral movement. The target environment typically involves a web application with direct template injection points, such as search fields, user profiles, or error messages that render FreeMarker syntax.

## Requirements

1. Valid user input point in the target web application that allows injection of FreeMarker template syntax (e.g., via a form field or URL parameter).
2. Knowledge of FreeMarker syntax and the application's template context (e.g., availability of objects like 'article' or similar).
3. Network access to the target application over HTTP/HTTPS.
4. Basic understanding of Java class loading and reflection to customize payloads.
5. Tools for intercepting and modifying requests, such as a proxy (though not strictly required for injection).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to prevent injection of template syntax (e.g., escape user input with FreeMarker's built-in escaping).
- Enable and configure FreeMarker's sandbox properly, restricting access to class loaders and sensitive packages like 'java.lang' or 'freemarker.template.utility'.
- Use allowlists for permitted directives and variables in templates, disabling dynamic class loading.
- Regularly update FreeMarker and dependent libraries to patch known SSTI vulnerabilities (e.g., upgrade to 2.3.32+).
- Monitor application logs for anomalous template processing errors or unexpected class loads; implement WAF rules to block payloads containing '<#assign' or class references.
- Enable Java security managers or use containers with restricted permissions to limit RCE impact.

## Objectives

1. Identify and confirm SSTI vulnerability in a FreeMarker-based application.
2. Bypass the sandbox restrictions to access restricted Java classes.
3. Execute arbitrary system commands on the server to achieve RCE.
4. Verify execution and potentially escalate to full system compromise.

## Instructions

### Step 1: Confirm SSTI Vulnerability

**Context**: Test if the application processes FreeMarker syntax by injecting a benign payload that reveals template context or executes a simple output. This step verifies the injection point without triggering the sandbox bypass.

Inject a basic FreeMarker expression into the vulnerable input field, such as a search box or profile description:

```freemarker
${7*7}
```

> This should render as '49' if SSTI is possible. If it outputs literally or errors out, the point may not be vulnerable. Expected output: The result of the arithmetic operation displayed in the response. If successful, proceed to sandbox bypass.

### Step 2: Inject Sandbox Bypass Payload

**Context**: Use the provided payload to load the class loader and Execute class, bypassing sandbox restrictions. This step accesses the protection domain of an available object (e.g., 'article') to chain into command execution.

Reference the payload code: [[codes/Freemarker-Sandbox-Bypass-Payload]]

Inject the payload into the same vulnerable input point. Customize the final command (e.g., replace 'id' with 'whoami' or a reverse shell invocation if needed).

> The payload loads the ObjectWrapper to create an instance of the Execute utility, then invokes it with the desired system command. Expected output: The output of the executed command (e.g., 'uid=33(www-data) gid=33(www-data)' for 'id') embedded in the application's response. If the sandbox blocks it, try alternative entry points like '${.globals}' or adjust based on the template's available variables.

### Step 3: Verify and Escalate Execution

**Context**: Confirm RCE by executing a command that provides diagnostic information, then escalate if possible (e.g., to a full shell).

Modify the payload's command parameter to run a verification command like 'uname -a' or attempt file read (e.g., '/etc/passwd'). If successful, chain to more destructive actions like downloading tools.

> Expected output: System details or file contents in the response. Success is indicated by non-error execution and relevant output. If blocked, iterate on the payload by exploring other class paths or using reflection alternatives.

### Step 4: Clean Up and Mitigate Detection

**Context**: Avoid alerting defenders by limiting payload executions and monitoring for logs.

After verification, avoid repeated injections. Use one-time payloads for persistence if needed (e.g., add cron jobs via RCE).

> Expected output: No additional visible changes, but check application logs indirectly if access allows. Success: RCE achieved without immediate detection.
