---
id: 59cf3d31-5379-4cd9-9a13-a3ba68c29dec
type: code
language: python
verified: true
created_at: '2023-04-06T03:56:40.091487+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - web-applications
  - python
tags:
  - ssti
  - mako
  - payload
validated: true
---

# Mako-SSTI-OS-Module-Reference

## Code

```python
os
```

## Description

This code snippet references the Python 'os' module directly, serving as a basic payload for Mako SSTI to confirm access to operating system functionalities through the template namespace.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; direct module reference. | N/A |

## Usage

Inject as `${os}` into a vulnerable Mako template parameter (e.g., via HTTP request) to disclose the module in the rendered output. Used in reconnaissance to test SSTI without executing commands.

## Detection

- Application logs showing template rendering with 'os' module references.
- Response bodies containing `<module 'os'` strings.
- Anomalous Python import traces in server error logs.

## Related

- [[procedures/Mako-SSTI-OS-Information-Gathering]]
