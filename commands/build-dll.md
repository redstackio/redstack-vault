---
id: cmd-build-dll
data: build_dll.bat
tags:
  - compilation
  - gadget
type: command
output: 'Compiled DLL file (e.g., sleep.dll)'
executor: batch
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:33.139Z'
verified: false
validated: true
submitted: true
---
# build-dll

## Command

```batch
build_dll.bat
```

## Description

Compiles a C# DLL gadget for .NET deserialization exploitation using Visual Studio tools, as per BishopFox guidance for Telerik RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | N/A | N/A |

## Examples

### Basic Usage

```batch
build_dll.bat
```

### Advanced Usage

Run in VS Developer Command Prompt; modify source for custom payloads.

## Expected Output

Build success message and output DLL file in the project directory.

## Related

- [[commands/upload-and-trigger-dll-poc]]
