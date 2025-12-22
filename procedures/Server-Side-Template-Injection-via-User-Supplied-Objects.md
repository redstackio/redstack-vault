---
id: be2d5a3a-2ecf-47e7-9ae3-6b5905c29ecb
name: Server-Side-Template-Injection-via-User-Supplied-Objects
type: procedure
verified: true
submitted: false
created_at: '2020-08-24T06:12:14.484247+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
  - Web
tags:
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Server Side Template Injection]]'
  - '[[tags/SSTI]]'
  - '[[tags/Web Applications]]'
  - ssti
  - django
  - injection
  - information-disclosure
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[System Information Discovery]]'
sub_techniques: []
commands: []
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Server-Side-Template-Injection-via-User-Supplied-Objects

## Summary

This procedure demonstrates how to exploit Server-Side Template Injection (SSTI) in a Django-based web application by injecting malicious template expressions into user-supplied objects, such as product description templates. The attack allows disclosure of sensitive information, including the application's SECRET_KEY, by leveraging Django's template engine to access internal objects and settings.

## Description

Server-Side Template Injection occurs when user input is unsafely embedded into server-side templates, allowing attackers to inject and execute arbitrary template code. In this scenario, the target application permits authenticated users to edit product description templates, which are rendered using Django's template engine. By injecting payloads, an attacker can trigger errors to identify the framework, invoke debugging features to enumerate accessible objects, and extract configuration details like the SECRET_KEY. This technique is particularly dangerous in web applications as it can lead to remote code execution (RCE) in more advanced cases, but here it focuses on information disclosure. The attack assumes the attacker has valid user credentials and access to the template editing interface. It maps to MITRE ATT&CK techniques for exploiting public-facing applications and system information discovery.

## Requirements

1. Valid user account with permissions to edit product description templates in the web application.
2. Access to a web browser or proxy tool like [[tools/Burp-Suite]] to intercept and manipulate requests.
3. Knowledge of the target's URL and login endpoint.
4. No special privileges beyond standard user access; the vulnerability stems from insufficient input sanitization in the template rendering process.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization for all user-supplied template content, using whitelisting for allowed expressions.
- Disable debug mode in production environments and restrict access to sensitive objects like settings.
- Use sandboxed template engines or third-party libraries that limit expression evaluation (e.g., Django's safe filters).
- Monitor application logs for template rendering errors, unusual payloads in request bodies, or access to internal objects.
- Employ Web Application Firewalls (WAFs) to detect common SSTI patterns like `{%`, `{{`, or debug invocations.

## Objectives

1. Identify the template engine (Django) via error messages triggered by invalid payloads.
2. Enumerate accessible objects and properties within the template context.
3. Extract sensitive configuration data, such as the SECRET_KEY, for potential further exploitation.
4. Demonstrate information disclosure without requiring code execution privileges.

## Instructions

### Step 1: Authenticate to the Application

**Context**: Gain authenticated access to the web application to reach the template editing functionality. This step ensures the attacker can interact with user-supplied objects.

Navigate to the login page using a browser or proxy tool like [[tools/Burp-Suite]]. Enter valid credentials and submit the login form.

**Expected Output**: Successful redirection to the dashboard or main application page, with session cookies or tokens indicating authenticated state.

### Step 2: Navigate to Product Description Template Editor

**Context**: Locate the feature allowing editing of product description templates, where user input is directly inserted into server-side templates.

From the authenticated session, browse to the product management or template editing section. Select a product and access its description template editor.

**Expected Output**: The editor interface loads, displaying the current template content (e.g., existing Django template expressions).

### Step 3: Inject Fuzz Payload to Identify Template Engine

**Context**: Test for SSTI vulnerability by injecting an invalid or fuzzing string to provoke an error that reveals the underlying framework. This helps confirm Django usage without alerting the application.

In the template editor, replace or append the fuzz payload from [[codes/SSTI-Fuzz-Payload]] to the existing template content. Save the changes.

**Expected Output**: An error page or message indicating a template syntax error, specifically mentioning Django (e.g., "Invalid block tag" or Django traceback).

### Step 4: Inject Debug Payload to Enumerate Context

**Context**: Once Django is confirmed, use the built-in debug functionality to list all accessible objects and properties in the template context, identifying paths to sensitive data.

Remove the fuzz payload and insert the debug payload from [[codes/Django-SSTI-Debug-Payload]] into the template. Save the changes.

**Expected Output**: The rendered template displays a debug output dump, including a list of variables, objects (e.g., request, user, settings), and their properties.

### Step 5: Extract SECRET_KEY Using Settings Access

**Context**: Leverage the identified settings object to disclose the SECRET_KEY, a critical configuration value used for signing sessions and other security features.

Remove the debug payload and insert the extraction payload from [[codes/Django-SSTI-Settings-Secret-Key-Extraction]] into the template. Save the changes.

**Expected Output**: The rendered template outputs the plaintext SECRET_KEY value (e.g., a long random string like 'django-insecure-abc123...').

## Expected Output

Successful execution results in the disclosure of the SECRET_KEY and potentially other settings. Verify by comparing the output against known Django configuration patterns. If the key is exposed, it can be used for session forgery or further attacks.
