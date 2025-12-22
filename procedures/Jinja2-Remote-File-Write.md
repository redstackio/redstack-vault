---
id: c2551f88-2457-4c33-9c8d-2501c0e0f4fb
name: Jinja2-Remote-File-Write
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.709728+00:00'
updated_at: '2023-04-10T20:23:35.626269+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Python]]'
sub_techniques: []
tags:
  - '[[tags/Jinja2]]'
  - '[[tags/Jinja2 - Write into remote file]]'
  - '[[tags/Server Side Template Injection]]'
  - ssti
  - rce
  - file-write
commands: []
platforms:
  - Web
  - Python
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Jinja2-Remote-File-Write

## Summary

This procedure exploits a Server-Side Template Injection (SSTI) vulnerability in Jinja2-templated Python web applications to achieve remote code execution, specifically by writing arbitrary files to the server filesystem. It allows attackers to establish persistence by creating backdoors or modifying configuration files, leading to potential full system compromise.

## Description

Jinja2 is a popular templating engine used in Python frameworks like Flask and Django to dynamically generate HTML or other content. If user input is improperly rendered through Jinja2 without sanitization, attackers can inject template expressions that evaluate to arbitrary Python code execution on the server. This procedure focuses on using SSTI to access Python's file handling capabilities, enabling remote file writes. The attack targets web applications where templates process unsanitized user data, such as search fields, usernames, or profile inputs. Success results in file creation or modification, which can be used for persistence (e.g., writing a web shell) or data tampering. This maps to execution via Python interpreter abuse and is effective against misconfigured web apps running as a privileged user.

## Requirements

1. Network access to a vulnerable web application using Jinja2 for templating (e.g., Flask app exposing user input to templates).
2. Ability to submit input that gets rendered by Jinja2, such as via HTTP POST/GET parameters.
3. Knowledge of the target server's filesystem paths (e.g., web root like /var/www/html/).
4. A tool like Burp Suite or curl for intercepting and modifying requests (optional but recommended for testing).

## Defense

- Implement strict input validation and sanitization to prevent template injection, using libraries like MarkupSafe for auto-escaping.
- Run web applications under least-privilege accounts to limit file write access.
- Enable Web Application Firewall (WAF) rules to detect SSTI payloads (e.g., patterns like {{ }} or __class__).
- Monitor server logs for unusual file creations and use file integrity monitoring tools like OSSEC or Tripwire.
- Regularly audit template usage and avoid passing user input directly to render functions.

## Objectives

1. Confirm SSTI vulnerability by injecting a test payload that executes harmless code.
2. Craft and inject a payload to write an arbitrary file to the server.
3. Verify file creation for persistence or further exploitation.

## Instructions

### Step 1: Identify and Confirm SSTI Vulnerability

**Context**: Locate an input field or parameter that is rendered through Jinja2 templates without escaping. Test for injection by submitting a simple payload that causes visible server-side execution, such as displaying a Python object attribute.

Submit a test payload like `{{7*7}}` in a vulnerable field (e.g., username or search box). If the response shows `49`, SSTI is confirmed.

> This step verifies the vulnerability exists before attempting file operations, avoiding unnecessary noise.

### Step 2: Craft the File Write Payload

**Context**: Use Jinja2's access to Python classes to instantiate a file object and write content. The payload leverages the object hierarchy to reach the built-in file class.

Reference the payload code [[codes/Jinja2-File-Write-Payload]] and customize the file path and content as needed (e.g., write a simple web shell).

> The payload accesses subclasses of the type object to find the file class (typically at index 40, but verify via testing as indices can vary by Python version).

### Step 3: Inject the Payload and Execute

**Context**: Submit the crafted payload via the vulnerable input. Monitor the response for errors or success indicators, then verify the file write by accessing it directly (e.g., via HTTP if in web root).

Inject the payload into the same field used for confirmation. For example, in a POST request to a login or profile endpoint:

```http
POST /vulnerable-endpoint HTTP/1.1
Content-Type: application/x-www-form-urlencoded

username={{ ''.__class__.__mro__[2].__subclasses__()[40]('/var/www/html/myflaskapp/hello.txt', 'w').write('Hello here !') }}&submit=1
```

> If successful, no error in response; check server access logs or directly request /myflaskapp/hello.txt to see 'Hello here !'.

### Step 4: Verify and Escalate

**Context**: Confirm the file was written and assess for further actions, such as injecting a full reverse shell script.

Access the written file via browser or curl (e.g., `curl http://target.com/myflaskapp/hello.txt`). If content appears, the write succeeded. Use this for persistence by writing executable scripts.

> Success here enables lateral movement or data exfiltration; monitor for detection via file monitoring.
