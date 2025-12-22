---
id: e19bd1d0-54fa-4e8d-b656-5f4b099007c5
name: Server-Side-Template-Injection-with-Debug-Information-Leak
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.470835+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - '[[tags/Debug information leak]]'
  - '[[tags/Django Templates]]'
  - '[[tags/Server Side Template Injection]]'
commands:
  - '[[commands/curl-inject-django-debug]]'
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# Server-Side-Template-Injection-with-Debug-Information-Leak

## Summary

This procedure exploits Server-Side Template Injection (SSTI) in Django applications by injecting the {% debug %} template tag into user-controlled input fields, leveraging enabled debug mode to leak sensitive server configuration details such as installed packages, file system paths, and environment variables. This information can be used to craft further payloads for remote code execution or deeper reconnaissance.

## Description

Server-Side Template Injection (SSTI) occurs when user input is unsafely interpolated into server-side templates, allowing attackers to inject and execute arbitrary template code. In Django, templates use a syntax that, if not properly escaped, enables injection of tags like {% debug %}, which dumps debugging information when debug mode is active (DEBUG=True in settings.py). This leak reveals critical details like the template context, request data, server settings, and installed Python packages, aiding in payload refinement for full compromise. The procedure targets web applications with Django's template engine, typically in forms, URL parameters, or search fields. Successful exploitation can lead to information disclosure, paving the way for code execution via more advanced SSTI payloads.

## Requirements

1. Access to a web application using Django templates with user-controlled input points (e.g., search fields, form parameters).
2. Knowledge of the SSTI vulnerability and Django template syntax.
3. The target Django application must have DEBUG=True enabled in production (common misconfiguration).
4. Network access to the application and tools like curl or a proxy (e.g., Burp Suite) for payload injection.

## Defense

- Disable DEBUG mode in production environments by setting DEBUG=False in Django's settings.py.
- Sanitize and escape all user input before rendering in templates using Django's built-in auto-escaping or libraries like bleach.
- Implement Web Application Firewalls (WAFs) to detect and block template injection patterns (e.g., {%, {{, }}).
- Regularly audit and update Django and dependencies to patch known template vulnerabilities.
- Enable logging for template rendering errors and monitor for anomalous debug outputs.

## Objectives

1. Inject the {% debug %} tag to trigger information disclosure from the Django template engine.
2. Extract sensitive server details like package lists and file paths to inform further exploitation.
3. Validate the vulnerability for potential escalation to remote code execution.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Locate a user input field rendered via Django templates, such as a search box or profile field, where input is directly interpolated without escaping. Test for SSTI by injecting simple template expressions like {{ 7*7 }} to confirm execution (expected output: 49).

**Command** ([[commands/curl-inject-django-debug]]):

Use curl to send a basic SSTI test payload to the vulnerable endpoint.

```bash
curl -X POST "http://target.com/search" -d "q={{ 7*7 }}"
```

> This step verifies template execution. If the response shows "49", SSTI is confirmed. Otherwise, try other parameters or endpoints.

### Step 2: Inject Debug Tag for Information Leak

**Context**: Once SSTI is confirmed, inject the {% debug %} tag using [[codes/Django-Debug-Template-Tag]] to dump server debugging information. This leverages Django's debug mode to output context variables, settings, and environment details.

**Command** ([[commands/curl-inject-django-debug]]):

```bash
curl -X POST "http://target.com/search" -d "q={% debug %}" -v
```

> The verbose flag (-v) helps inspect headers and responses. Expected output includes a detailed debug dump with sections like "Context Variables", "Template Path", and "Installed Apps". Review for sensitive data like database credentials or file paths. If the response is truncated, use a proxy to capture full output.

### Step 3: Analyze Leaked Information

**Context**: Parse the debug output to identify exploitable details, such as Python package versions for gadget chains or absolute paths for file read payloads. This step refines subsequent attacks, like importing os for RCE.

No specific command needed; manually review the response from Step 2.

> Look for indicators like "os" module availability or server root paths. Success is confirmed by extracting at least one actionable piece of information, such as a package list confirming vulnerable libraries.
