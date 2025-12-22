---
id: ac26c1ad-3fdc-4a86-b621-287335df52dd
name: Bash-Command-Injection-Payload-for-Cat-Etc-Passwd
type: code
language: bash
verified: true
created_at: '2023-04-06T03:55:57.097369+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - command-injection
  - payload
  - rce
validated: true
---

# Bash-Command-Injection-Payload-for-Cat-Etc-Passwd

## Code

```bash
original_cmd_by_server `cat /etc/passwd`
original_cmd_by_server $(cat /etc/passwd)
```

## Description

This code snippet provides example payloads for injecting a command to read /etc/passwd into a vulnerable application's system command execution. The backticks (`) or command substitution ($( )) execute `cat /etc/passwd` alongside the original command, appending the file contents to the application's output. It targets bash shells on Linux servers and is used in web-based command injection attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `original_cmd_by_server` | The application's original command (e.g., `ping` or `ls`) | `ping` |

## Usage

Replace `original_cmd_by_server` with the actual command the application runs (identified via error messages or testing). Inject the payload into a vulnerable input field, such as a URL parameter or form submission. For example, if the app runs `ping $_INPUT`, submit `127.0.0.1 `cat /etc/passwd``. The response will include the passwd contents concatenated with ping output. Use in tools like Burp Suite for precise delivery during pentesting.

## Detection

- Monitor application logs for shell metacharacters in inputs (e.g., `, $, ;).
- WAF rules to block payloads containing command substitution patterns.
- Anomaly detection in response sizes or contents (e.g., unexpected user lists in HTTP responses).
- Enable shell execution logging on the server to capture injected commands.

## Related

- [[procedures/Command-Injection-to-Read-Etc-Passwd]]
