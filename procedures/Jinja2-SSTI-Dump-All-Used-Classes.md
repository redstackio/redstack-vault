---
id: 935c7d1b-96c2-45d0-8087-0bfe222fb769
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.629435+00:00'
updated_at: '2024-01-01T00:00:00Z'
tactics:
  - '[[Collection]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[Data from Local System]]'
  - '[[Exploitation of Remote Services]]'
sub_techniques: []
tags:
  - '[[tags/Jinja2]]'
  - '[[tags/Server-Side-Template-Injection]]'
  - ssti
  - reconnaissance
  - python
commands:
  - '[[commands/jinja2-ssti-dump-subclasses]]'
  - '[[commands/jinja2-ssti-access-globals]]'
  - '[[commands/jinja2-ssti-access-builtins]]'
  - '[[commands/jinja2-ssti-access-builtins-via-self]]'
platforms:
  - web
  - python
tools: []
validated: true
---

# Jinja2-SSTI-Dump-All-Used-Classes

## Summary

This procedure exploits a Server-Side Template Injection (SSTI) vulnerability in Jinja2-based Python web applications to dump all loaded subclasses, access global variables, and enumerate built-in functions. By injecting specially crafted template expressions, an attacker can perform reconnaissance on the server's Python environment, identifying loaded modules, classes, and available functions for potential further exploitation such as remote code execution.

## Description

Jinja2 is a widely used templating engine in Python frameworks like Flask and Django. When user input is directly rendered without proper escaping or sandboxing, attackers can inject Python code via template syntax (e.g., {{ payload }}). This procedure focuses on class introspection techniques to list subclasses of core Python types, revealing the application's loaded classes and libraries. From there, chaining to __globals__ and __builtins__ exposes the namespace and built-in capabilities. This is typically used in web pentesting after identifying a vulnerable input point, such as a search field or dynamic content renderer. Success provides insights into the system architecture, potentially leading to identification of useful classes like subprocess for RCE. The target environment is a remote web server running a vulnerable Jinja2 application, with no authentication required if the injection point is public-facing.

## Requirements

1. Confirmed SSTI vulnerability in a Jinja2-rendered input (test with basic payload like {{7*7}} expecting 49)
2. Tool to send crafted HTTP requests (e.g., browser dev tools, curl, or [[tools/Burp-Suite]] for interception)
3. Network access to the target web application
4. Basic understanding of Python object model and Jinja2 syntax

## Defense

- Enable Jinja2's sandbox environment to restrict dangerous attributes and methods
- Implement strict input validation, whitelisting allowed template constructs, and escaping user input
- Deploy a Web Application Firewall (WAF) with rules to block common SSTI patterns (e.g., {{, class, __mro__, subclasses})
- Monitor application logs and responses for anomalous outputs like class lists or unexpected Python errors
- Regularly update Jinja2 and web frameworks to patch known vulnerabilities

## Objectives

1. Enumerate all subclasses loaded in the Python interpreter to map the environment
2. Access global variables and built-in functions to discover available resources
3. Collect reconnaissance data for chaining to more advanced exploits like file reads or command execution

## Instructions

### Step 1: Dump Loaded Subclasses

**Context**: Begin reconnaissance by injecting a payload to list all subclasses of the base 'type' class. This reveals hundreds of loaded classes from Python standard library and application modules, helping identify exploitable ones (e.g., os, subprocess). Use the most reliable variant; if blocked, try alternatives mentioned in the command's examples.

**Command** ([[commands/jinja2-ssti-dump-subclasses]]):
```python
{{ ''.__class__.__mro__[2].__subclasses__() }}
```

> This traverses the method resolution order (MRO) of the string class to reach 'type' and call subclasses(). Inject into the vulnerable parameter (e.g., GET ?q={{payload}}). If the response renders the list, scan for interesting classes like <class 'subprocess.Popen'> (index ~300-400 depending on version).

### Step 2: Access Global Variables

**Context**: Chain from a known object (e.g., a subclass instance from Step 1) to access __globals__, which exposes the module's global namespace. This may reveal configuration variables, imported modules, or sensitive data like database connections.

**Command** ([[commands/jinja2-ssti-access-globals]]):
```python
{{ [].__class__.__init__.__globals__ }}
```

> Append __globals__ to an object's chain (here using list's init for a complete payload). The output is a dictionary of globals; look for keys like 'os', 'sys', or app-specific vars. Why: Globals provide context on the rendering module's scope.

### Step 3: Enumerate Built-in Functions

**Context**: Directly access the __builtins__ module to list all available built-in functions and operators. This confirms access to core Python capabilities without imports, useful for planning RCE (e.g., using 'open' for file read).

**Command** ([[commands/jinja2-ssti-access-builtins]]):
```python
{{ __builtins__ }}
```

> If direct access works, the response shows a dict like {'abs': <built-in function abs>, ...}. If sandboxed, it may be restricted. Why: Builtins are always available and form the basis for further payloads.

### Step 4: Access Builtins via Class Context

**Context**: In cases where direct __builtins__ is blocked, chain through self (in class methods) or init globals. This alternative path confirms builtin access and can be used if the app renders in a class scope.

**Command** ([[commands/jinja2-ssti-access-builtins-via-self]]):
```python
{{ self.__init__.__globals__.__builtins__ }}
```

> Assumes 'self' context (common in Flask views); outputs the builtins dict. If not in self scope, adapt to a subclass chain. Why: Provides redundancy if direct access fails, enabling importless function calls.
