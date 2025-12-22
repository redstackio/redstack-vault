---
id: df61b4ba-04f4-4eee-9c1d-55a8a71a6f49
name: dotnet-to-jscript-assembly-to-vba
type: command
executor: cmd
data: >-
  DotNetToJScript.exe $_ASSEMBLY_PATH -l vba -o $_OUTPUT_VBA_PATH -c
  $_CLASS_NAME
output: null
created_at: '2023-04-06T03:56:23.670590+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - conversion
  - evasion
  - dotnet
verified: true
validated: true
---

# dotnet-to-jscript-assembly-to-vba

## Command

```cmd
DotNetToJScript.exe $_ASSEMBLY_PATH -l vba -o $_OUTPUT_VBA_PATH -c $_CLASS_NAME
```

## Description

This command uses the DotNetToJScript.exe tool to convert a .NET assembly file into VBA code, facilitating the embedding of .NET payloads into Office macros for stealthy execution. It is used in evasion techniques to run .NET code in environments where direct execution is restricted.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ASSEMBLY_PATH | Path to the input .NET assembly DLL file (e.g., ExampleAssembly.dll) | Yes |
| -l vba | Specifies the output language as VBA (alternatives: jscript, cscript) | Yes |
| -o $_OUTPUT_VBA_PATH | Output file path and name for the generated VBA (e.g., test.vba) | Yes |
| -c $_CLASS_NAME | Name of the class containing the Main method to execute (e.g., CactusTorch) | Yes |

## Examples

### Basic Usage

```cmd
DotNetToJScript.exe ExampleAssembly.dll -l vba -o payload.vba -c CactusTorch
```

### Advanced Usage

For a different class or output language:

```cmd
DotNetToJScript.exe MyPayload.dll -l jscript -o script.js -c PayloadClass
```

## Expected Output

The command generates a .vba file with the converted code. Console output may include progress messages like "Converting assembly..." and any errors if the assembly is invalid. Successful run: "Output written to test.vba". The VBA file contains functions mirroring the .NET logic, ready for Office insertion.

## Related

- [[procedures/Convert-DotNet-Assembly-to-VBA-for-CactusTorch]]
