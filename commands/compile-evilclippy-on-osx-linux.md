---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: compile-evilclippy-on-osx-linux
type: command
executor: bash
data: >-
  mcs /reference:OpenMcdf.dll,System.IO.Compression.FileSystem.dll
  /out:EvilClippy.exe *.cs
output: null
created_at: '2023-04-06T03:56:23.824566+00:00'
updated_at: '2023-04-10T20:36:56.680981+00:00'
platforms:
  - Linux
  - macOS
tags:
  - compilation
  - evilclippy
verified: true
validated: true
---

# compile-evilclippy-on-osx-linux

## Command

```bash
mcs /reference:OpenMcdf.dll,System.IO.Compression.FileSystem.dll /out:EvilClippy.exe *.cs
```

## Description

Compiles the EvilClippy C# source code into an executable using Mono on OSX or Linux platforms. This is the first step to prepare the tool for VBA manipulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /reference:OpenMcdf.dll,System.IO.Compression.FileSystem.dll | References required DLLs for compound file handling and compression | Yes |
| /out:EvilClippy.exe | Specifies the output executable name | Yes |
| *.cs | Includes all C# source files in the current directory | Yes |

## Examples

### Basic Usage

```bash
mcs /reference:OpenMcdf.dll,System.IO.Compression.FileSystem.dll /out:EvilClippy.exe *.cs
```

### Advanced Usage

Run in a directory containing the EvilClippy source files and DLLs.

## Expected Output

Compilation successful message, such as "Compilation succeeded". The EvilClippy.exe file is created in the current directory, ready for execution.

## Related

- [[procedures/VBA-Purging-with-EvilClippy]]
- [[tools/EvilClippy]]
