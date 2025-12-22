---
id: dfbb572f-9db2-4575-be12-9d03cc6fcddd
name: Groovy-Server-Side-Template-Injection-for-Command-Execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.205085+00:00'
updated_at: '2023-04-10T20:23:42.719023+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - '[[tags/Groovy]]'
  - '[[tags/Groovy - Command Execution]]'
  - '[[tags/Server Side Template Injection]]'
commands: []
platforms:
  - Web
  - Java
  - Windows
tools: []
validated: true
---

# Groovy-Server-Side-Template-Injection-for-Command-Execution

## Summary

This procedure exploits Server-Side Template Injection (SSTI) vulnerabilities in web applications using Groovy templating engines to achieve remote command execution (RCE). By injecting malicious Groovy expressions into user-controlled template inputs, an attacker can execute arbitrary system commands on the server, such as launching applications or running scripts, leading to full server compromise.

## Description

Groovy Server-Side Template Injection targets web applications that dynamically render user input through Groovy-based templating systems, such as those integrated with frameworks like Grails or custom Java servers. These templates allow server-side evaluation of expressions, which, if unsanitized, permit injection of Groovy code. The injected code leverages Groovy's dynamic features—like the `exec()` and `execute()` methods on strings—to spawn processes and run OS commands. This technique is particularly dangerous in enterprise environments where Groovy is used for configuration or reporting, as it bypasses typical input validation and enables persistence, data exfiltration, or lateral movement. Success depends on the application's rendering context and the server's permissions; for example, on Windows servers, commands like launching calc.exe can confirm execution. Detection is challenging due to the lack of explicit logging in template engines, but anomalies in process creation or error logs may indicate exploitation.

## Requirements

1. Access to a web application with a vulnerable Groovy template endpoint (e.g., user-controlled fields in forms, URLs, or API parameters that feed into template rendering).
2. Knowledge of the application's input points and basic Groovy syntax for crafting payloads.
3. Network access to the target server; no authentication required if the injection point is public-facing.
4. A proxy tool like Burp Suite for intercepting and modifying requests (optional but recommended for testing).
5. Target environment running on a system where command execution is possible (e.g., Windows for calc.exe testing).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to escape or whitelist template expressions, using libraries like OWASP ESAPI.
- Deploy a Web Application Firewall (WAF) tuned to detect SSTI patterns, such as Groovy-specific syntax like `${}` or `exec()`.
- Regularly update and patch Groovy-based frameworks (e.g., to versions with improved sandboxing) and conduct code reviews for template usage.
- Enable comprehensive logging for template rendering errors and monitor for unexpected process spawns via EDR tools.
- Use runtime application self-protection (RASP) to block dynamic code evaluation in production.

## Objectives

1. Confirm SSTI vulnerability by evaluating simple Groovy expressions.
2. Inject payloads to execute arbitrary system commands on the server.
3. Verify command execution through observable effects, such as application launches or output in responses.
4. Escalate to full server control for data access or persistence.

## Instructions

### Step 1: Identify and Test for SSTI Vulnerability

**Context**: Locate a user-controlled input that is processed through a Groovy template engine, such as a search field, profile bio, or dynamic report parameter. Test for injection by submitting simple expressions that should evaluate server-side if vulnerable.

**Test Payload**: Submit input like `${7*7}` or `${new Date()}` via the application's form or API.

> This step verifies if the application renders the evaluated result (e.g., "49" or current timestamp) instead of treating it as literal text. If successful, the input point is vulnerable to SSTI.

### Step 2: Craft and Inject Command Execution Payload

**Context**: Once SSTI is confirmed, escalate to RCE by injecting Groovy code that executes system commands. Use the provided code snippet for reliable execution methods.

**Code** ([[codes/Groovy-Command-Execution-Payloads]]):

```groovy
${T(java.lang.Runtime).getRuntime().exec("calc.exe")}
${'calc.exe'.execute()}
${this.getClass().forName("java.lang.Runtime").getRuntime().exec("calc.exe")}
${new GroovyShell().evaluate("'calc.exe'.execute()")}
```

> Replace "calc.exe" with the desired command (e.g., "whoami" on Linux). Submit the payload in the vulnerable input field. The `execute()` method spawns a new process, while `Runtime.exec()` provides direct OS access. Expected behavior: The command runs silently on the server; for calc.exe, a calculator window appears if in an interactive session, or check server logs/process lists for confirmation.

### Step 3: Verify Execution and Escalate

**Context**: Confirm RCE by observing side effects or chaining to more complex commands. If output isn't returned in the response, use out-of-band techniques like DNS exfiltration.

**Verification**: After injection, monitor the server for process creation (e.g., via task manager on Windows) or response anomalies. For proof, inject a command that writes to a web-readable file, like `${'echo PWNED > /tmp/pwned.txt'.execute()}` and access /tmp/pwned.txt.

> Success is indicated by the command's effects, such as file creation, network callbacks, or visible application launches. If blocked, try alternative payloads or check for sandbox restrictions.
