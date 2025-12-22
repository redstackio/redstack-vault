---
id: 03660999-8a3d-4202-8356-25ca44b55eb0
type: code
language: python
verified: true
created_at: '2023-04-06T03:56:39.901333+00:00'
updated_at: '2023-04-10T20:23:43.898447+00:00'
platforms:
  - Web
tags:
  - jinja2
  - ssti
validated: true
---

# access-request-class-directly

## Code

```python
request.__class__
request["__class__"]
```

## Description

Basic Jinja2 expressions to access the __class__ attribute of the request object directly. Used to verify SSTI before attempting filter bypasses; may be blocked by filters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| request | The Werkzeug/Flask request object in the template context | N/A |

## Usage

Inject into a template-rendered input field (e.g., search param) in a vulnerable Flask app. If unfiltered, reveals the class for further chaining.

## Detection

- Template logs showing direct attribute access attempts.
- WAF rules for __class__ in user input.

## Related

- [[procedures/Bypass-Jinja2-Filters-for-SSTI-Code-Execution]]
