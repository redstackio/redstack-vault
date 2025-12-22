---
id: 0a483c4b-04e8-4b0c-a3b1-f45aef32cb89
type: code
language: html
verified: true
created_at: '2023-04-06T03:56:39.415037+00:00'
updated_at: '2023-04-10T20:23:35.292542+00:00'
tags:
  - ssti
  - django
  - template-injection
platforms:
  - Web
validated: true
---

# Django-Template-Syntax-Examples

## Code

```html
# Variables
{{ variable }}
{{ variable.attr }}

# Filters
{{ value|length }}

# Tags
{% csrf_token %}
```

## Description

This code snippet provides basic examples of Django template syntax for variables, filters, and tags. It serves as a foundational reference for crafting server-side template injection (SSTI) payloads during post-exploitation. Variables allow access to context objects, attributes enable property traversal, filters process data (e.g., for length or formatting), and tags control flow or insert dynamic content. These elements are essential for building more complex payloads that lead to information disclosure or RCE.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| variable | A context variable from the template environment | request |
| value | Input value to apply filters to | '' (empty string for class access) |
| attr | Attribute name to access on an object | __class__ |

No runtime parameters are required beyond substitution in the injection payload.

## Usage

Embed these snippets into user-controlled inputs in a vulnerable Django template rendering endpoint (e.g., a search form or dynamic page). Start with simple variables to confirm SSTI, then chain attributes and filters to traverse objects toward RCE. For example, inject into a URL parameter: `/vulnerable?input={{ variable.attr|length }}`. Use in conjunction with tools like Burp Suite to intercept and modify requests. This is typically part of post-exploitation after initial access via the SSTI vuln.

## Detection

- Web application logs showing unevaluated template syntax in inputs (e.g., '{{' or '{%' patterns).
- Anomalous response content like Python class names or command outputs in rendered pages.
- Increased error rates from template evaluation failures.
- WAF rules matching SSTI payloads (e.g., object traversal like '__class__').
- Monitor for Python exceptions related to template rendering in server logs.

## Related

- [[procedures/Django-Template-Post-Exploitation]] (procedure that uses this syntax for RCE)
- [[tools/Burp-Suite]] (for payload delivery)
