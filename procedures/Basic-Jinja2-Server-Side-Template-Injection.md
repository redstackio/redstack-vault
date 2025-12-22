---
id: 1cb4d7f8-5adf-46dc-9a08-1af34b35e19d
name: Basic-Jinja2-Server-Side-Template-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.561568+00:00'
updated_at: '2023-04-10T20:23:44.307099+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - >-
    [[techniques/Cloud Instance Metadata API|T1522 - Cloud Instance Metadata
    API]]
sub_techniques: []
tags:
  - '[[tags/Jinja2]]'
  - '[[tags/Jinja2 - Basic injection]]'
  - '[[tags/Server Side Template Injection]]'
  - ssti
  - rce
  - python
commands:
  - '[[commands/curl-test-jinja2-ssti]]'
platforms:
  - Web
  - Python
tools: []
validated: true
---

# Basic-Jinja2-Server-Side-Template-Injection

## Summary

This procedure demonstrates how to identify and exploit basic Server-Side Template Injection (SSTI) vulnerabilities in web applications using the Jinja2 templating engine. By injecting malicious template expressions, an attacker can achieve remote code execution (RCE), extract sensitive configuration data, dump credentials, or access system information, potentially leading to full server compromise.

## Description

Jinja2 is a widely used Python templating engine for dynamically generating content in web applications, such as Flask or Django sites. If user input is unsafely passed to the template renderer without proper sandboxing or escaping, attackers can inject Jinja2 expressions to evaluate arbitrary Python code on the server. This procedure focuses on detection through simple arithmetic and string payloads, information disclosure via config access, and escalation to RCE for objectives like credential dumping or metadata retrieval in cloud environments. It assumes a vulnerable endpoint where user-supplied data (e.g., a search query or username field) is rendered directly into a template.

## Requirements

1. Access to a web application with a suspected Jinja2 backend (e.g., via browser or API endpoint).
2. Tools for sending HTTP requests, such as curl or a proxy like Burp Suite.
3. Knowledge of basic Jinja2 syntax for crafting payloads.
4. Network access to the target application (no authentication required for public-facing endpoints).

## Defense

- Implement strict input validation and sanitization to prevent untrusted data from reaching the template engine.
- Use Jinja2's sandbox mode or third-party extensions like jinja2-secure to restrict dangerous operations.
- Deploy a Web Application Firewall (WAF) to detect anomalous payloads containing template syntax like {{ }} or {% %}.
- Enable application logging for template rendering errors and monitor for unexpected code execution indicators, such as unusual process spawns or file accesses.

## Objectives

1. Detect the presence of a Jinja2 SSTI vulnerability through expression evaluation.
2. Extract environment and configuration details from the server.
3. Achieve arbitrary code execution to dump credentials or system information.
4. Establish persistence via web shell creation if escalation succeeds.

## Instructions

### Step 1: Identify Potential Injection Point

**Context**: Locate an input field or parameter in the web application where user data is dynamically rendered, such as a search box, profile name, or error message. This is typically a GET or POST parameter that feeds into a Jinja2 template.

Inspect the application using developer tools or a proxy to confirm the input is reflected in the response without escaping.

### Step 2: Test for SSTI Vulnerability

**Context**: Inject simple Jinja2 expressions to verify if the server evaluates templates. Start with non-destructive arithmetic or string operations to confirm injection without alerting defenses.

**Command** ([[commands/curl-test-jinja2-ssti]]):
```bash
curl -X GET "http://target.com/search?q={{7*'7'}}" -v
```

> This sends a payload that should render as '7777777' if SSTI is possible, instead of the literal string '{{7*'7'}}'. Observe the response body for evaluation. If successful, proceed to information disclosure; otherwise, try variations like double braces {{ }} or other parameters.

### Step 3: Extract Configuration and System Information

**Context**: Once SSTI is confirmed, access the Jinja2 environment config to gather details like version, installed packages, and potentially sensitive paths or keys. This helps in tailoring further exploits.

Inject payloads from [[codes/Jinja2-Basic-SSTI-Payloads]] to enumerate the config object.

For example, append `{{config}}` to the vulnerable parameter and submit via the same endpoint.

**Expected Output**: A response containing Jinja2 environment details, such as version and packages, confirming access to internal objects.

### Step 4: Escalate to Remote Code Execution

**Context**: Use the SSTI to execute Python code on the server, such as running system commands for credential dumping (e.g., reading /etc/passwd or environment variables) or accessing cloud metadata if hosted on AWS/GCP.

Craft a payload like `{{''.__class__.__mro__[1].__subclasses__()}}` to list available classes, then chain to execute `os.popen('whoami').read()` for basic RCE. For cloud environments, target metadata endpoints like `http://169.254.169.254/latest/meta-data/` via requests library invocation.

Submit the payload through the vulnerable parameter and parse the response for command output.

**Expected Output**: Execution results, such as current user ('www-data') or metadata JSON, indicating successful RCE.

### Step 5: Verify and Clean Up

**Context**: Confirm the impact by checking for credential access or persistence opportunities, then test defensive responses.

If RCE is achieved, attempt to write a simple web shell (e.g., via `open('/tmp/shell.py', 'w').write('import os;os.system(request)')`) and access it separately.

Monitor logs or responses for errors that might indicate detection.
