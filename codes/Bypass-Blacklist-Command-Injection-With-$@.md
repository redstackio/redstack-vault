---
id: 2e8b06e9-708e-441f-b5fa-9492a37d456d
type: code
name: Bypass-Blacklist-Command-Injection-With-$@
language: bash
verified: true
created_at: '2023-04-06T03:55:57.329039+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Unix
tags:
  - command-injection
  - bypass
  - shell
validated: true
---

# Bypass-Blacklist-Command-Injection-With-$-Syntax

## Code

```bash
who$@ami

echo $0
-> /usr/bin/zsh
echo whoami|$0
```

## Description

This code snippet illustrates a command injection payload using the $@ shell variable to bypass input filters that blacklist complete commands like 'whoami'. The first line 'who$@ami' splits the command across the variable expansion point, potentially evading detection. The subsequent lines identify the shell ($0) and execute a piped command to confirm injection success. It is intended for use in vulnerable applications that execute unsanitized input via Unix shells.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This snippet has no substitutable variables; adapt the injected command (e.g., replace 'whoami' with 'id' or 'cat /etc/passwd') based on the target. | N/A |

## Usage

Inject this payload into a vulnerable input field that feeds into a shell command (e.g., a web form parameter). First, use 'echo $0' to confirm the shell, then submit 'who$@ami' or pipe via the identified shell. Listen for output indicating success, such as user enumeration. This is typically used in web pentesting or red team engagements to achieve initial RCE.

## Detection

- Monitor application logs for anomalous shell expansions or split commands containing '$@' or similar variables.
- Use intrusion detection systems (IDS) to flag inputs with shell metacharacters (| , $).
- Enable command-line auditing on the server to detect unexpected executions like 'whoami' from application contexts.
- WAF rules targeting variable injections and blacklisted word fragments.

## Related

- [[procedures/Command-Injection-Bypass-Using-$-Syntax]]
