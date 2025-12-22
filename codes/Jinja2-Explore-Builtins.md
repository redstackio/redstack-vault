---
type: code
language: python
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - ssti
  - jinja2
  - exploration
platforms:
  - Web
validated: true
---

# Jinja2-Explore-Builtins

## Code

```python
{{ __builtins__ }}
```

## Description

This simple Jinja2 payload outputs the __builtins__ namespace, revealing available Python built-in functions and modules. It aids in reconnaissance during SSTI exploitation to identify accessible paths for further payload development.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No parameters; dumps entire builtins dict |

## Usage

Use early in SSTI testing to map the environment. Inject into vulnerable fields and parse the response for functions like 'import' or 'open'. Helps craft evasive payloads if direct os access is restricted.

## Detection

- Logs of template rendering with __builtins__ access.
- Response payloads containing Python namespace dumps.
- Behavioral monitoring for reconnaissance patterns in web inputs.

## Related

- [[procedures/Jinja2-Server-Side-Template-Injection-with-os-popen-read]]
