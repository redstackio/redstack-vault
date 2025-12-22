---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: compile-evilclippy-on-windows
type: command
executor: cmd
data: >-
  csc /reference:OpenMcdf.dll,System.IO.Compression.FileSystem.dll
  /out:EvilClippy.exe *.cs
output: null
created_at: '2023-04-06T03:56:23.824566+00:00'
updated_at: '2023-04-10T20:36:56.680981+00:00'
platforms:
  - Windows
tags:
  - compilation
  - evilclippy
verified: true
validated: true
---

# compile-evilclippy-on-windows

## Command

```cmd
csc /reference:OpenMcdf.dll,System.IO.Compression.FileSystem.dll /out:EvilClippy.exe *.cs
```

## Description

Compiles the EvilClippy C# source code into an executable using the .NET C# compiler on Windows. Essential for preparing the tool on Windows environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /reference:OpenMcdf.dll,System.IO.Compression.FileSystem.dll | References required DLLs for compound file handling and compression | Yes |
| /out:EvilClippy.exe | Specifies the output executable name | Yes |
| *.cs | Includes all C# source files in the current directory | Yes |

## Examples

### Basic Usage

```cmd
csc /reference:OpenMcdf.dll,System.IO.Compression.FileSystem.dll /out:EvilClippy.exe *.cs
```

### Advanced Usage

Execute in a directory with source files and DLLs; ensure .NET SDK is installed.

## Expected Output

"Compilation succeeded" or similar success indicator. EvilClippy.exe is generated without errors.

## Related

- [[procedures/VBA-Purging-with-EvilClippy]]
- [[tools/EvilClippy]]
