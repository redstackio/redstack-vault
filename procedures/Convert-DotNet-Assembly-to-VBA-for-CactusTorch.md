---
id: f6f9be91-4678-4be3-8bf4-0d5dd6ccdae1
name: Convert-DotNet-Assembly-to-VBA-for-CactusTorch
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.675333+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Visual Basic]]'
  - '[[Obfuscated Files or Information]]'
sub_techniques: []
tags:
  - office-attacks
  - macro
  - evasion
  - dotnet
  - cactustorch
commands:
  - '[[commands/dotnet-to-jscript-assembly-to-vba]]'
platforms:
  - Windows
  - Office
tools: []
validated: true
---

# Convert-DotNet-Assembly-to-VBA-for-CactusTorch

## Summary

This procedure converts a .NET assembly into VBA code using the DotNetToJScript tool, enabling the execution of .NET-based payloads within Office macros via the CACTUSTORCH VBA module. It allows attackers to evade detection by embedding obfuscated .NET functionality in legitimate-looking Office documents, commonly used for command execution on victim machines during targeted attacks.

## Description

The CACTUSTORCH VBA Module facilitates the execution of arbitrary commands on a victim's Windows machine by leveraging Office's macro capabilities. By converting a .NET assembly (containing the malicious logic) into VBA-compatible code, attackers can bypass restrictions on direct .NET execution in macro environments. This involves disassembling the assembly with tools like Ildasm.exe and recompiling it into JScript/VBA using jsc.exe or dedicated converters like DotNetToJScript. The resulting VBA can be inserted into documents like Excel or Word for delivery via phishing. This technique is effective in environments with macro execution enabled, as it masquerades as benign VBA while running .NET code, making it hard to detect through signature-based tools. It maps to execution via scripting interpreters and obfuscated files or information.

## Requirements

1. A compiled .NET assembly (.dll) containing the payload logic, such as a class with a Main method for command execution.
2. Access to the DotNetToJScript.exe tool on a development machine (Windows with .NET Framework).
3. Basic knowledge of VBA and .NET to verify the output code.
4. An Office document template (e.g., .xlsm or .docm) for embedding the generated VBA.

## Defense

- Implement strict application whitelisting policies using tools like AppLocker or WDAC to block unauthorized script execution in Office.
- Enable macro security settings to disable all macros by default and require digital signatures for trusted sources.
- Monitor for anomalous Office processes spawning child processes or network connections using EDR solutions.
- Regularly patch Office and .NET Framework to address known vulnerabilities in macro parsing.
- Analyze VBA code in documents with antivirus scanners that detect obfuscated or converted payloads.

## Objectives

1. Convert .NET assembly code into executable VBA for use in Office macros.
2. Enable stealthy command execution on victim machines via CACTUSTORCH module.
3. Evade detection by leveraging legitimate Office functionality.

## Instructions

### Step 1: Prepare the .NET Assembly

**Context**: Ensure the .NET assembly is ready for conversion, containing a class (e.g., CactusTorch) with the Main method that defines the malicious behavior, such as downloading and executing payloads.

Identify the assembly file path and the class name to target. No command is needed here; verify the DLL exists and is compilable.

> This step confirms prerequisites; success is having a valid .dll file.

### Step 2: Convert Assembly to VBA

**Context**: Use the DotNetToJScript tool to translate the .NET assembly into VBA code, specifying the output language, file, and entry class.

**Command** ([[commands/dotnet-to-jscript-assembly-to-vba]]):
```cmd
DotNetToJScript.exe $_ASSEMBLY_PATH -l vba -o $_OUTPUT_VBA_PATH -c $_CLASS_NAME
```

> Run this on a Windows machine with the tool. Replace placeholders: $_ASSEMBLY_PATH with the input DLL (e.g., ExampleAssembly.dll), $_OUTPUT_VBA_PATH with the desired VBA file (e.g., test.vba), and $_CLASS_NAME with the entry class (e.g., CactusTorch). The tool disassembles the IL code and generates equivalent VBA. Expected output is a .vba file containing the converted code, which may require minor tweaks for Office compatibility.

### Step 3: Verify and Embed the VBA

**Context**: Test the generated VBA in an Office document to ensure it executes without errors, then embed it into the CACTUSTORCH module structure.

Open the output .vba file in a text editor and review for syntax issues. Insert into an Office document's VBA editor (Alt+F11 in Excel/Word), associating it with an auto-open event.

> Success is the VBA compiling without errors in the Office VBA editor and executing the intended .NET logic (e.g., command spawn) when the document opens.
