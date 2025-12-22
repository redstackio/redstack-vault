---
id: c0b4bddd-c4a7-4812-9143-dc66ef5c6c02
name: Twig-Debugging-Injection-for-Arbitrary-Code-Execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:40.278039+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[sub-techniques/JavaScript|T1059.007 - JavaScript]]'
tags:
  - '[[tags/Server-Side-Template-Injection]]'
  - '[[tags/Twig]]'
  - '[[tags/RCE]]'
  - '[[tags/Web-Application]]'
commands:
  - '[[commands/curl-post-twig-injection]]'
tools: []
platforms:
  - Web
  - PHP
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Twig-Debugging-Injection-for-Arbitrary-Code-Execution

## Summary

This procedure exploits Twig templating engine vulnerabilities in PHP web applications where debugging mode is enabled, allowing injection of Twig syntax into user-controlled inputs like form fields, cookies, or HTTP headers to execute arbitrary code, dump sensitive variables, or reveal server information.

## Description

Twig is a flexible, fast, and secure templating engine for PHP, commonly used in frameworks like Symfony. When debug mode is active (often in development but sometimes left on in production), attackers can inject Twig expressions to execute code in the context of the web server. This Server-Side Template Injection (SSTI) technique bypasses typical input sanitization, enabling remote code execution (RCE), data exfiltration, or further compromise. It targets unsanitized user inputs rendered through Twig templates, such as search forms, user profiles, or custom headers. Success depends on the application's configuration and input handling.

## Requirements

1. Access to a PHP web application using Twig templating engine with debug mode enabled (check for debug indicators like detailed error pages).
2. Identification of a user-controlled input point that is rendered via Twig (e.g., via Burp Suite or manual testing).
3. Knowledge of basic Twig syntax for crafting payloads.
4. Tools for sending HTTP requests, such as curl or a proxy like Burp Suite.
5. Network access to the target application.

## Defense

- Disable Twig debug mode in production by setting 'debug' to false in Twig configuration.
- Implement strict input validation and sanitization to strip or escape template syntax (e.g., using Twig's autoescape).
- Use web application firewalls (WAFs) to detect and block common SSTI patterns like '{{' or 'dump()'.
- Monitor application logs for anomalous requests containing template syntax and enable comprehensive logging for Twig rendering.
- Regularly audit and update dependencies to patch known Twig vulnerabilities.

## Objectives

1. Inject Twig payloads to execute arbitrary expressions and reveal application context.
2. Dump sensitive variables like app configuration or server details for further exploitation.
3. Achieve RCE by chaining dumps to command execution if the application allows.
4. Exfiltrate data or pivot to deeper system access.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Locate an input field, cookie, or header that is directly interpolated into a Twig template without proper escaping. Test with simple payloads like '{{7*7}}' to confirm injection.

Use [[commands/curl-post-twig-injection]] to send a test request:

```bash
curl -X POST http://target.com/vulnerable-endpoint -d "input={{7*7}}" -v
```

This step verifies if the output renders '49', indicating successful injection.

### Step 2: Dump Application Context

**Context**: Once injection is confirmed, use Twig's dump() function to expose variables like the app object or request context, revealing sensitive information such as server variables or session data.

Reference the payload in [[codes/Twig-Debug-Dump-Payload]] and inject it via [[commands/curl-post-twig-injection]]:

```bash
curl -X POST http://target.com/vulnerable-endpoint -d "input={{dump(app)}}" -v
```

If the input is a cookie, use `-H "Cookie: session=input{{dump(_context)}}"`. Expected: Output displays dumped variables, including paths, configs, or database connections.

### Step 3: Extract Server Information

**Context**: Chain to more advanced payloads to join and output server arrays, aiding in reconnaissance for further attacks like path traversal or command injection.

Inject the join filter payload from [[codes/Twig-Debug-Dump-Payload]] using [[commands/curl-post-twig-injection]]:

```bash
curl -X POST http://target.com/vulnerable-endpoint -d "input={{app.request.server.all|join(',')}}" -v
```

This concatenates server variables (e.g., PHP_SELF, HTTP_HOST) into a comma-separated string for easy parsing.

### Step 4: Escalate to RCE if Possible

**Context**: If the application context reveals command execution capabilities (e.g., via plugins or extensions), craft payloads to run system commands. Note: This depends on Twig extensions; basic Twig may limit to data dumps.

Test with a command execution attempt, such as injecting into a context allowing `{% ... %}` blocks, but verify compatibility. Use the same injection method as prior steps.

**Decision Point**: If dump reveals a vulnerable extension (e.g., allowing `app.addGlobal` or shell access), proceed to custom RCE; otherwise, use dumped info for social engineering or other vectors.
