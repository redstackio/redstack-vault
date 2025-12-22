---
id: 6128009a-ea72-464c-996e-bed06164c089
name: Jinja2-Config-Information-Extraction
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.666575+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - >-
    [[techniques/System-Information-Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Jinja2]]'
  - '[[tags/Server-Side-Template-Injection]]'
  - '[[tags/Config-Dump]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Jinja2-Config-Information-Extraction

## Summary

This procedure exploits Server-Side Template Injection (SSTI) vulnerabilities in web applications using the Jinja2 templating engine to extract sensitive configuration variables, such as database credentials, secret keys, and environment details. By injecting a malicious template payload, attackers can dump the application's config dictionary, providing reconnaissance insights into the infrastructure and potential escalation paths.

## Description

Jinja2 is a Python-based templating engine commonly used in frameworks like Flask and Django to generate dynamic HTML content. SSTI vulnerabilities occur when user input is unsafely rendered into templates, allowing arbitrary code execution on the server. This procedure targets the 'config' object available in Jinja2 environments, which holds application settings. The injected payload iterates over the config dictionary and outputs key-value pairs, revealing sensitive data without direct file access. This technique is useful in red team engagements for mapping the target environment, identifying misconfigurations, or chaining to further exploits like database access. It assumes the application exposes an injection point, such as a search field or user profile renderer, and runs on a Python backend with Jinja2.

## Requirements

1. Valid user session or unauthenticated access to a web application vulnerable to SSTI in Jinja2.
2. Knowledge of an input field that renders user-supplied data as a Jinja2 template (e.g., via error messages, previews, or dynamic content).
3. Tools for intercepting and modifying HTTP requests, such as a browser developer console or proxy like Burp Suite.
4. Basic understanding of HTTP requests to craft and submit the injection payload.

## Defense

Defensive measures and detection strategies:

- Upgrade to the latest Jinja2 version and enable autoescaping for all user inputs.
- Implement strict input validation and sandboxing for template rendering, avoiding direct user input in templates.
- Deploy a Web Application Firewall (WAF) to detect common SSTI payloads, including Jinja2-specific patterns like '{{', '%{', or config references.
- Monitor application logs for anomalous template rendering errors or unexpected output in responses.
- Use runtime application self-protection (RASP) tools to block code execution in templating engines.

## Objectives

1. Identify and confirm an SSTI vulnerability in a Jinja2-based application.
2. Extract the full config dictionary to reveal sensitive variables like API keys, database URIs, and debug flags.
3. Gather reconnaissance data to support further attacks, such as credential reuse or service enumeration.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Locate a user-controllable input that is processed by Jinja2 templating. Common points include search bars, comment fields, or profile descriptions where input is echoed back in rendered HTML.

Test for SSTI by injecting a simple payload like '{{7*7}}' and checking if the response evaluates to '49' instead of literal text. This confirms template execution without escaping.

### Step 2: Inject the Config Dump Payload

**Context**: Once confirmed, use the specialized payload to access and dump the config object. This payload loops through the config dictionary, escaping outputs to avoid breaking the HTML response.

**Code** ([[codes/Jinja2-Config-Variables-Dump]]):

```jinja2
{% for key, value in config.iteritems() %}
    <dt>{{ key|e }}</dt>
    <dd>{{ value|e }}</dd>
{% endfor %}
```

Submit this payload via the identified injection point, such as in a POST request body or URL parameter. Use a proxy to capture the response and inspect the rendered HTML for the dumped config entries.

> The payload assumes the 'config' object is globally accessible in the Jinja2 environment (common in Flask apps). If not, adapt by first confirming object access with '{{config}}'. Expected output is an HTML definition list (<dl>) with config keys (e.g., SECRET_KEY, DATABASE_URL) and their values, potentially revealing credentials or paths.

### Step 3: Analyze and Verify Output

**Context**: Review the response for sensitive data and validate the dump's completeness.

Parse the HTML output to extract key-value pairs. Look for indicators like database connection strings, encryption keys, or environment variables. If the dump is partial, chain with additional payloads to access other objects like 'request' or 'app'.

> Success is indicated by visible config entries in the response without template errors. If values are redacted or empty, the environment may have restricted access.
