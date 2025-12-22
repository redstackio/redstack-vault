---
type: code
language: jinja2
verified: true
tags:
  - ssti
  - jinja2
  - debug
  - template-injection
platforms:
  - Web
validated: true
---

# Jinja2-Basic-Debug-Dump

## Code

```jinja2
{% debug %}
```

## Description

This Jinja2 template snippet injects the debug statement to output all variables in the current template context, including locals, globals, and request data. It is used in SSTI attacks to reconnaissance application internals without executing arbitrary code.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static payload with no variables; customize surrounding input as needed. | N/A |

## Usage

Inject this payload into a user-controlled template input, such as a search parameter (?search={% debug %}) or username field. Requires the Jinja2 debug extension to be enabled on the server. Use in conjunction with tools like Burp Suite to craft requests and view responses.

## Detection

- Monitor HTTP responses for debug dumps containing variable lists (e.g., patterns like 'config: <Config>', 'request: <Request>').
- Log template rendering errors or unusual {% %} tags in inputs.
- WAF rules to block '{% debug %}' in request bodies/parameters.
- Application logs showing debug extension usage in production.

## Related

- [[procedures/Exploit-Jinja2-Debug-Statement-for-SSTI]]
