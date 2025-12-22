---
id: 037a9f1c-e367-4716-b931-af4278db0d17
name: Jinja2-SSTI-to-RCE-via-Flask-Hook
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.758140+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[sub-techniques/Python|T1059.006 - Python]]'
tags:
  - '[[tags/Jinja2]]'
  - '[[tags/Server-Side-Template-Injection]]'
  - '[[tags/Remote-Code-Execution]]'
commands: []
platforms:
  - Web
  - Python
tools: []
validated: true
---

# Jinja2-SSTI-to-RCE-via-Flask-Hook

## Summary

This procedure exploits a Server-Side Template Injection (SSTI) vulnerability in Jinja2-based Flask applications to achieve remote code execution (RCE). By injecting a malicious template payload, an attacker can execute arbitrary Python code on the server, such as hooking into Flask's request lifecycle to force output from otherwise blind RCE scenarios, enabling confirmation of exploitation and further command execution.

## Description

Jinja2 is a widely used templating engine in Python web frameworks like Flask, allowing dynamic content generation. If user input is directly interpolated into templates without proper escaping or sandboxing, it leads to SSTI vulnerabilities. Attackers can abuse Jinja2's expression syntax to access the template context, escalate to builtins, and execute code. This procedure focuses on a blind SSTI scenario where normal payloads don't produce visible output; instead, it uses Flask-specific hooks (like after_this_request) to modify responses post-execution, proving RCE by altering the server's output (e.g., injecting 'Powned' into the response). The technique is applicable to Flask apps with unsanitized user-controlled template rendering, such as search fields, usernames, or dynamic content sections. Success grants arbitrary code execution, potentially leading to shell access, data exfiltration, or persistence.

## Requirements

1. Access to a web application using Flask with Jinja2 templating where user input is rendered in templates without autoescaping or sandboxing.
2. Identification of an injectable parameter (e.g., via Burp Suite or manual testing with payloads like '{{7*7}}' to confirm SSTI).
3. Knowledge of the application's request flow to target response-modifying hooks.
4. A proxy tool like Burp Suite for intercepting and modifying requests.

## Defense

- Enable Jinja2 autoescaping for all user-controlled inputs and use the sandboxed environment for untrusted templates.
- Validate and sanitize all user inputs before template rendering, avoiding direct interpolation.
- Implement a Web Application Firewall (WAF) with rules to detect common SSTI payloads (e.g., '{{', '%7B%7B').
- Monitor server logs for anomalous Python executions or unexpected response modifications in Flask apps.

## Objectives

1. Confirm SSTI vulnerability in a Jinja2/Flask endpoint.
2. Inject a payload to execute arbitrary code via Flask hooks for output forcing in blind scenarios.
3. Achieve verifiable RCE by observing modified server responses.
4. Establish a foundation for further post-exploitation, such as reverse shell deployment.

## Instructions

### Step 1: Identify and Confirm SSTI Vulnerability

**Context**: Locate a user-controlled input point (e.g., a search box or profile field) that renders via Jinja2 templates. Test for injection by submitting a simple expression to evaluate if the server processes it.

Inject a basic payload like '{{7*7}}' into the vulnerable parameter and submit the request. Observe the response for the computed result (e.g., '49'), confirming SSTI. If no output appears (blind SSTI), proceed to output-forcing techniques.

**Expected Output**: For confirmatory payload, response contains '49' or equivalent computation result. For blind cases, no visible change, but proceed assuming vulnerability.

### Step 2: Prepare and Inject Flask Hook Payload for RCE

**Context**: Escalate from basic SSTI to code execution by accessing Python builtins and importing Flask modules. Use the template to exec a hook function that modifies the response after request processing, forcing output to prove RCE.

Use a proxy to intercept the request to the vulnerable endpoint. Replace the injectable parameter with the following payload, referencing the code snippet [[codes/Jinja2-Flask-Hook-for-Output-Forcing]]:

```py
{{
  (_=lambda:().__class__.__bases__[0].__subclasses__()).().__init__.__globals__['sys'].modules['os'].popen('id').read()
}}
```

For output forcing in blind RCE, inject the specialized Flask hook payload:

Embed the code from [[codes/Jinja2-Flask-Hook-for-Output-Forcing]] directly into the parameter (URL-encoded if necessary, e.g., via %7B%7B for '{{'). Submit the request.

This payload accesses builtins via attribute chaining, imports Flask, defines an after_this_request hook to create a custom response ('Powned'), and returns it, bypassing normal template rendering.

**Expected Output**: Server response body modified to include 'Powned' instead of the expected content, confirming RCE execution.

### Step 3: Verify and Escalate RCE

**Context**: Confirm the hook executed by checking response alterations. Escalate by modifying the payload to run system commands or deploy a reverse shell.

If 'Powned' appears, the vulnerability is exploitable. Extend the exec statement in the payload to run commands, e.g., replace 'Powned' with output from os.popen('whoami').read() to exfiltrate data via response.

For full RCE, adapt the hook to execute a reverse shell script (e.g., import subprocess and call a Python one-liner shell).

**Expected Output**: Response includes output from executed commands (e.g., username or system info), or a new connection to your listener if escalating to shell.

### Step 4: Clean Up and Document

**Context**: Avoid detection by removing hooks if persistence isn't needed, and log findings for reporting.

Submit a normal request to clear any lingering hooks. Document the vulnerable endpoint, payload, and impact for remediation.
