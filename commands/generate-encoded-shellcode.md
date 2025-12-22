---
type: command
executor: bash
data: python2 ./shellcode_encoder.py -cpp -cs -py $_INPUT_FILE $_PASSWORD $_METHOD
output: null
created_at: '2023-04-06T03:56:16.386855+00:00'
updated_at: '2023-04-10T20:36:24.586607+00:00'
platforms:
  - Linux
  - Windows
tags:
  - encoding
  - obfuscation
verified: true
validated: true
---

# Generate Encoded Shellcode

## Command

```bash
python2 ./shellcode_encoder.py -cpp -cs -py $_INPUT_FILE $_PASSWORD $_METHOD
```

## Description

This command uses a Python script to encode raw shellcode with XOR or other methods, outputting versions in C++, C#, and Python formats for embedding in loaders like MSBuild XML. It helps evade static analysis by obfuscating the payload bytes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INPUT_FILE | Path to the raw shellcode binary (e.g., payload.bin) | Yes |
| $_PASSWORD | Encoding key or password for XOR (e.g., MySecretPassword) | Yes |
| $_METHOD | Encoding algorithm (e.g., xor) | Yes |
| -cpp | Generate C++ output | Built-in |
| -cs | Generate C# output | Built-in |
| -py | Generate Python output | Built-in |

## Examples

### Basic Usage

```bash
python2 ./shellcode_encoder.py -cpp -cs -py payload.bin MySecretPassword xor
```

### Advanced Usage

```bash
python2 ./shellcode_encoder.py -cpp -cs -py payload.bin StrongKey123 aes
```

## Expected Output

Encoded files such as payload_encoded.cs containing byte arrays and decoder code, e.g.:

```csharp
byte[] encoded = new byte[] { 0xBE, 0xEF, ... };
// Decoder function follows
```

No console errors; files written to current directory.

## Related

- [[procedures/msbuild-shellcode-execution]]
- [[tools/cobalt-strike]]
