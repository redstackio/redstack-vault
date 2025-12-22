---
id: 6d616937-fb82-4c3f-97e8-753cfbe0e6d8
type: code
language: jinja2
verified: true
created_at: '2023-04-06T03:56:39.664928+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - ssti
  - jinja2
  - config-dump
platforms:
  - Web
validated: true
---

# Jinja2-Config-Variables-Dump

## Code

```jinja2
{% for key, value in config.iteritems() %}
    <dt>{{ key|e }}</dt>
    <dd>{{ value|e }}</dd>
{% endfor %}
```

## Description

This Jinja2 template payload exploits SSTI vulnerabilities to iterate over the application's config dictionary and output all key-value pairs in an HTML definition list format. It uses the 'e' filter to escape outputs, preventing HTML breakage while revealing sensitive configuration details like secret keys and database credentials.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| config | The application's config object (assumed globally available in Jinja2 environment) | Flask's app.config |

## Usage

Inject this payload into a vulnerable input field in a Jinja2-powered web application, such as a search parameter or user bio. Submit via HTTP request (e.g., GET/POST) and inspect the response HTML for the dumped config. Commonly used in reconnaissance phases of web pentests to map backend infrastructure.

## Detection

- WAF rules matching Jinja2 SSTI patterns like '{% for' or 'config.iteritems()'. 
- Application logs showing template evaluation errors or unusual variable access.
- Response analysis for escaped HTML tags (<dt>, <dd>) containing config-like strings (e.g., 'SECRET_KEY', 'DATABASE_URL').
- Runtime monitoring for unauthorized access to config objects in Python processes.

## Related

- [[procedures/Jinja2-Config-Information-Extraction]]
