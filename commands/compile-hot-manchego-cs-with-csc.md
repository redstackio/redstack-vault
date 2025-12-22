---
type: command
executor: cmd
data: >-
  C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe /reference:EPPlus.dll
  hot-manchego.cs /out:hot-manchego.exe
tags:
  - compilation
  - c-sharp
platforms:
  - Windows
verified: true
validated: true
---

# compile-hot-manchego-cs-with-csc

## Command

```cmd
C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe /reference:EPPlus.dll hot-manchego.cs /out:hot-manchego.exe
```

## Description

This command uses the C# compiler (csc.exe) to compile hot-manchego.cs into an executable, referencing EPPlus.dll for Excel handling, producing hot-manchego.exe for VBA generation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/reference:EPPlus.dll` | References the EPPlus library for Excel operations | Yes |
| `hot-manchego.cs` | Input source file to compile | Yes |
| `/out:hot-manchego.exe` | Specifies the output executable name | Yes |

## Examples

### Basic Usage

```cmd
C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe /reference:EPPlus.dll hot-manchego.cs /out:hot-manchego.exe
```

### Advanced Usage

```cmd
C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe /reference:EPPlus.dll /target:exe hot-manchego.cs /out:custom.exe /debug
```

## Expected Output

Microsoft (R) Visual C# Compiler version 4.7.3056.0
Copyright (C) Microsoft Corporation. All rights reserved.

hot-manchego.cs(1,8): warning CS7027: Defined symbol `DEBUG' is not used by the code.
Compilation succeeded - 1 warning(s), 0 error(s).

No errors indicate successful compilation; the .exe file is created.

## Related

- [[procedures/Generate-Obfuscated-VBA-Macro-Using-Hot-Manchego]]
