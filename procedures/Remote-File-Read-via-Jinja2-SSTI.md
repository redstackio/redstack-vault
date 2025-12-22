---
id: 027e0a13-cac2-44c2-bcae-f350b46df486
name: Remote-File-Read-via-Jinja2-SSTI
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.689236+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/File-and-Directory-Discovery|T1083 - File and Directory
    Discovery]]
  - >-
    [[techniques/Exploit-Public-Facing-Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - jinja2
  - ssti
  - server-side-template-injection
  - file-read
  - template-injection
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Remote-File-Read-via-Jinja2-SSTI

## Summary

This procedure exploits Server-Side Template Injection (SSTI) vulnerabilities in applications using the Jinja2 templating engine to read arbitrary files on the server. By injecting malicious templates, attackers can access sensitive files like configuration files or user data, enabling information disclosure and potential further compromise.

## Description

Jinja2 SSTI occurs when user input is unsafely rendered as a template in a web application, allowing attackers to execute arbitrary Python code within the template context. This procedure focuses on file read operations by leveraging built-in Python classes and functions accessible in the Jinja2 environment, such as subclasses of the object class to instantiate a File object or accessing builtins via global scopes. It targets Flask applications or similar, where the template engine processes user-supplied strings. Successful exploitation reveals file contents in the HTTP response, aiding in credential theft or system reconnaissance. This technique requires an injectable parameter, like a search field or username input, and assumes the application runs with sufficient file permissions.

## Requirements

1. Network access to a vulnerable web application using Jinja2 (e.g., Flask-based).
2. An input point vulnerable to SSTI, such as a form field, URL parameter, or API endpoint that renders user input as a template.
3. Tools for intercepting and modifying requests, like a proxy (though not strictly required for basic injection).
4. Knowledge of target file paths (e.g., /etc/passwd on Linux servers).

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and validation to prevent template syntax in user inputs; use auto-escaping in Jinja2 (e.g., enable Jinja2's autoescape).
- Sandbox the template environment to restrict access to dangerous classes like File or builtins.open.
- Monitor application logs for anomalous template rendering errors or unexpected file access patterns.
- Use Web Application Firewalls (WAFs) to detect SSTI payloads, such as {{ }} expressions or __class__ traversals.
- Regularly audit and update dependencies like Flask/Jinja2 to patched versions.

## Objectives

1. Identify and confirm SSTI vulnerability in Jinja2-based applications.
2. Read contents of sensitive server files to disclose information.
3. Use disclosed data for lateral movement or privilege escalation.

## Instructions

### Step 1: Confirm SSTI Vulnerability

**Context**: Test if the input is rendered as a Jinja2 template by injecting a benign payload that alters the output predictably. This verifies the vulnerability before attempting file reads.

Inject the following test payload into the vulnerable parameter (e.g., via a form submission or URL):

{{ 7*7 }}

> If the response shows "49" instead of the literal string, SSTI is confirmed. This step ensures the application processes the input as executable template code.

### Step 2: Inject File Read Payload Using File Class

**Context**: Use Python's subclass enumeration to access the File class and read a target file. This bypasses direct restrictions on file operations in the template sandbox.

Use the code snippet [[codes/Jinja2-SSTI-File-Read-via-Subclasses]] to inject into the vulnerable parameter. Replace the file path with your target (e.g., '/etc/passwd').

> Expected: The response includes the file contents. For /etc/passwd, it shows user entries like root:x:0:0:root:/root:/bin/bash. If the index [40] fails (due to Python version differences), iterate through subclasses to find the correct File class index.

### Step 3: Inject File Read Payload Using Config Globals

**Context**: Access the File class via the application's config object, which is often exposed in Flask globals, to read another target file. This provides an alternative if the subclass method is blocked.

Use the code snippet [[codes/Jinja2-SSTI-File-Read-via-Subclasses]] (second payload) or adapt it for config.items()[4][1] (Flask's config access). Target a file like "/tmp/flag".

> Expected: Response embeds the file contents. Verify by checking for expected data; failure may indicate config index mismatch—probe with {{ config }} to enumerate.

### Step 4: Inject File Read Payload Using Builtins

**Context**: Traverse globals to reach builtins.open for direct file reading. This method accesses core Python functions and is useful if subclass access is restricted.

Use the code snippet [[codes/Jinja2-SSTI-File-Read-via-Subclasses]] (third payload), referencing get_flashed_messages.__globals__.__builtins__.open for the target file.

> Expected: File contents appear in the response. Success confirms unrestricted builtins access; monitor for errors indicating sandboxing.
