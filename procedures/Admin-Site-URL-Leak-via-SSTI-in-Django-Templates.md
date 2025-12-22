---
id: fd4cca67-4cb0-41cc-ac4d-c69153abd96a
name: Admin-Site-URL-Leak-via-SSTI-in-Django-Templates
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.524308+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - '[[tags/Admin-Site-URL-leak]]'
  - '[[tags/Django-Templates]]'
  - '[[tags/Server-Side-Template-Injection]]'
commands:
  - '[[commands/curl-send-ssti-payload]]'
platforms:
  - Web
tools: []
validated: true
---

# Admin-Site-URL-Leak-via-SSTI-in-Django-Templates

## Summary

This procedure exploits a Server-Side Template Injection (SSTI) vulnerability in Django templates to trigger a rendering error that leaks the admin site URL in the error message. When Django's debug mode is enabled, unsanitized user input passed to the template engine can cause exceptions, exposing internal paths like the admin interface URL, enabling unauthorized access for further attacks such as data manipulation.

## Description

Django templates dynamically render HTML by replacing variables with values, but if user input is directly interpolated without sanitization, attackers can inject template syntax to execute arbitrary code or trigger errors. In this case, the vulnerability allows injection of malformed template code (e.g., causing a division by zero) to force a TemplateSyntaxError or similar exception. With DEBUG=True in production (a common misconfiguration), the traceback in the error response reveals the admin site URL, typically /admin/ or a custom path. This leak provides a foothold for accessing the Django admin panel, where attackers can add, modify, or delete data if weak credentials or no authentication are in place. The procedure targets web applications using Django's template engine with vulnerable input points like search fields, comments, or form parameters rendered via {{ user_input }}.

## Requirements

1. Network access to the vulnerable Django web application (e.g., via HTTP/HTTPS).
2. Identification of an input field vulnerable to SSTI, such as a search parameter or user profile field.
3. Tools for sending HTTP requests, like curl or a proxy like Burp Suite.
4. Basic knowledge of Django template syntax and HTTP request manipulation.

## Defense

Defensive measures and detection strategies:

- Sanitize all user input before passing it to the template engine using Django's built-in escaping (e.g., {{ user_input|escape }} or mark_safe only when necessary).
- Disable DEBUG mode in production environments to prevent detailed error messages from leaking sensitive information.
- Implement Web Application Firewall (WAF) rules to detect and block common SSTI payloads like {{, {% , or arithmetic expressions.
- Regularly audit templates for unsafe rendering and update Django to the latest version to leverage security improvements.
- Enable logging for template rendering errors and monitor for anomalous requests containing template syntax.

## Objectives

1. Trigger a template rendering error via SSTI to expose the admin site URL.
2. Capture the leaked URL from the error response for subsequent unauthorized access.
3. Use the admin URL to attempt login or further exploitation, such as data modification.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Locate a user-controlled input that is rendered in a Django template without proper escaping, such as a search query or username field. Test for SSTI by injecting simple template syntax like {{ 7*7 }}; if the response shows 49, SSTI is confirmed.

**Command** ([[commands/curl-send-ssti-test]]):
```bash
curl -X GET "http://target.com/search?q={{ 7*7 }}" -v
```

> This command sends a basic SSTI test payload. If successful, the response will evaluate the expression and display 49 inline, confirming injection. If not, try POST requests or other parameters. Expected output: Response body containing "49" instead of the literal string "{{ 7*7 }}".

### Step 2: Craft and Send Error-Inducing Payload

**Context**: Once SSTI is confirmed, inject a payload that causes a rendering exception to trigger an error page. A division by zero ({{ 1/0 }}) forces a ZeroDivisionError, which in debug mode leaks tracebacks including the admin URL.

**Command** ([[commands/curl-send-ssti-payload]]):
```bash
curl -X POST "http://target.com/vulnerable-endpoint" -d "input={{ 1/0 }}" -H "Content-Type: application/x-www-form-urlencoded" -v
```

> Submit the payload via the vulnerable parameter (adjust endpoint and param name as needed). The server will attempt to render the template, fail, and return an error page. Expected output: HTTP 500 response with a detailed traceback mentioning the admin site URL, e.g., "Template error at /admin/base.html" or similar path disclosure.

### Step 3: Extract and Verify Leaked URL

**Context**: Parse the error response for the admin URL, typically found in the exception details or template path references. Verify by accessing the leaked URL directly.

No specific command needed; manually inspect the response or use grep on saved output:
```bash
grep -i "admin" error_response.html
```

> Look for paths like "/admin/" or custom admin URLs. Success is confirmed if the admin login page loads without prior knowledge of the path. If the URL is leaked, proceed to credential testing or brute-forcing.
