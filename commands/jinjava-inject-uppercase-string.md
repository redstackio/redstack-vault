---
id: 32a7ee3e-035e-4bda-8a6e-32ba7103376c
name: jinjava-inject-uppercase-string
type: command
executor: jinjava-template
data: '{{ ''a''.toUpperCase() }}'
output: null
created_at: '2023-04-06T03:56:39.935747+00:00'
updated_at: '2023-04-10T20:23:50.082714+00:00'
platforms:
  - Web
tags:
  - ssti
  - jinjava
verified: true
validated: true
---

# jinjava-inject-uppercase-string

## Command

```
{{ 'a'.toUpperCase() }}
```

## Description

This Jinjava template payload injects into a vulnerable input to execute the toUpperCase() method on a string, confirming SSTI by rendering 'A'. Use in web app inputs that are templated to test for injection without accessing sensitive data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'a'` | Test string to uppercase (can be any lowercase string) | Yes |
| `toUpperCase()` | Built-in Jinjava string method | Built-in |

## Examples

### Basic Usage

```
{{ 'hello'.toUpperCase() }}
```

Renders as 'HELLO'.

### Advanced Usage

```
{{ userInput.toUpperCase() }}
```

Where userInput is a variable; use to confirm variable access.

## Expected Output

The application renders the uppercased string, e.g., 'A', instead of the literal payload. Errors like template syntax issues indicate sanitization.

## Related

- [[procedures/Jinjava-SSTI-Uppercase-String-and-Request-Object-Injection]]
- [[commands/jinjava-access-request-object]]
