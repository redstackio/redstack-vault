---
id: 11cb5350-2978-44c9-a8c3-477cf88ab9a5
type: code
language: Python
verified: true
created_at: '2020-03-16T06:46:13.217669+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
tags:
  - rce
  - file-read
  - werkzeug
validated: true
---

# Python-Read-Arbitrary-File-Werkzeug

## Code

```python
target = "/etc/passwd"; f = open(target, "r"); print(f.read()); f.close()
```

## Description

This Python code snippet reads the contents of an arbitrary file (e.g., /etc/passwd) and prints it to the output. It is designed for execution in the Werkzeug debugger console to exfiltrate sensitive system files during RCE exploitation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| target | Full path to the file to read | "/etc/passwd" |

## Usage

Execute this directly in the Werkzeug interactive console after triggering an error page. Substitute the 'target' variable with any readable file path on the server. Useful for initial reconnaissance to gather user accounts, configurations, or credentials.

## Detection

- Monitor web application logs for Python file I/O operations (e.g., open() calls on sensitive paths like /etc/passwd).
- Enable Python tracing or sandboxing in production environments to log console executions.
- File access auditing on the server (e.g., via auditd) for unexpected reads by the web process.
- WAF rules to block debug console access or anomalous error triggers.

## Related

- [[procedures/Werkzeug-Debugger-Panel-Read-Write-RCE]]
