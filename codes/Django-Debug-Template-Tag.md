---
id: ea3cb053-ed34-4931-9fdd-b026b1eb1218
name: Django-Debug-Template-Tag
type: code
language: django
verified: true
created_at: '2023-04-06T03:56:39.469187+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - ssti
  - debug-leak
  - django
validated: true
---

# Django-Debug-Template-Tag

## Code

```django
{% debug %}
```

## Description

This Django template tag injects a debug dump into the rendered output when DEBUG=True is set in the Django settings. It exposes sensitive information including context variables, request details, template paths, installed applications, and environment variables, which can be leveraged for reconnaissance in SSTI attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This tag requires no parameters; it dumps the current template context directly. | N/A |

## Usage

Inject this tag via user-controlled input in Django templates, such as form fields or URL parameters (e.g., ?q={% debug %}). Use tools like curl or Burp Suite to submit the payload. Ideal for initial SSTI validation and information gathering before escalating to RCE payloads.

## Detection

- Monitor web application logs for template rendering errors or debug tag executions.
- WAF rules to block {% debug %} patterns in incoming requests.
- Enable Django's logging for template contexts and alert on unexpected debug outputs in production.
- Network traffic analysis for responses containing package lists or SECRET_KEY leaks.

## Related

- [[procedures/Server-Side-Template-Injection-with-Debug-Information-Leak]]
- [[curl-inject-django-debug]]
