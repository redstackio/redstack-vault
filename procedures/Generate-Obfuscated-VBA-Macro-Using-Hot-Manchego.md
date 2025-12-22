---
type: procedure
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Obfuscated-Files-or-Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques:
  - '[[sub-techniques/Compile-After-Delivery|T1027.004 - Compile After Delivery]]'
  - '[[sub-techniques/Software-Packing|T1027.002 - Software Packing]]'
tags:
  - '[[tags/Office-Attacks]]'
  - '[[tags/XLSM-Hot-Manchego]]'
  - vba-macro
  - obfuscation
commands:
  - '[[commands/powershell-create-empty-xlsm-file]]'
  - '[[commands/compile-hot-manchego-cs-with-csc]]'
  - '[[commands/run-hot-manchego-to-generate-vba]]'
platforms:
  - Windows
tools: []
verified: true
validated: true
---

# Generate-Obfuscated-VBA-Macro-Using-Hot-Manchego

## Summary

This procedure generates an obfuscated VBA macro from C# source code using the Hot Manchego tool, which compiles and processes the code to create a macro embeddable in an Excel (.xlsm) file. The resulting macro evades detection by antivirus and other security controls, enabling execution of arbitrary commands on a victim's machine when the file is opened.

## Description

The Hot Manchego technique leverages C# code to produce obfuscated VBA that can be inserted into Microsoft Excel workbooks. This is particularly useful in phishing campaigns where the malicious .xlsm file is attached to an email. Upon opening and enabling macros, the VBA executes payloads such as downloading malware or exfiltrating data. The obfuscation occurs through compilation and packing, making static analysis difficult. This procedure assumes access to a Windows environment with .NET Framework installed, and requires the hot-manchego.cs source file and EPPlus.dll for compilation. The target environment is typically a Windows workstation with Microsoft Office, where macro execution is permitted.

## Requirements

1. Windows system with .NET Framework 4.0 or later (includes csc.exe compiler).
2. hot-manchego.cs file containing the C# code for macro generation.
3. EPPlus.dll library for handling Excel files during compilation.
4. Microsoft Excel installed to create and test the .xlsm file.
5. Administrative privileges may be needed for compilation if paths are restricted.

## Defense

- Disable or restrict VBA macro execution in Microsoft Office via Group Policy or application settings.
- Implement advanced email security gateways to scan attachments for malicious macros and block spear-phishing.
- Deploy endpoint detection and response (EDR) tools with behavioral analysis to monitor macro execution and anomalous Office processes.
- Enable macro antivirus scanning and use sandboxing for Office files from untrusted sources.

## Objectives

1. Compile C# code into an executable that generates obfuscated VBA.
2. Create an empty Excel workbook to serve as the macro container.
3. Produce the VBA macro code for embedding in the .xlsm file to execute malicious commands.
4. Deliver the file via phishing to achieve initial access and code execution on the victim.

## Instructions

### Step 1: Create Empty Excel Workbook

**Context**: Begin by creating a blank .xlsm file, which supports macros and will host the generated VBA code. This ensures the file is ready for macro insertion without triggering immediate alerts.

**Command** ([[commands/powershell-create-empty-xlsm-file]]):
```powershell
New-Item -ItemType File -Name blank.xlsm -Force
```

> This PowerShell command creates an empty file named blank.xlsm in the current directory. Verify the file exists using `ls` or File Explorer; it should be a zero-byte file initially.

### Step 2: Compile the C# Source Code

**Context**: Compile the hot-manchego.cs file using the built-in C# compiler (csc.exe) to produce the hot-manchego.exe executable. The EPPlus.dll reference is required for Excel manipulation functions in the code.

**Command** ([[commands/compile-hot-manchego-cs-with-csc]]):
```cmd
C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe /reference:EPPlus.dll hot-manchego.cs /out:hot-manchego.exe
```

> Run this in Command Prompt or PowerShell from the directory containing hot-manchego.cs and EPPlus.dll. Successful compilation produces hot-manchego.exe without errors. Check for the .exe file and review any output for warnings about missing references.

### Step 3: Generate the Obfuscated VBA Macro

**Context**: Use the compiled executable to process the blank.xlsm file and output the obfuscated VBA code to a text file. This step applies the obfuscation and packing to hide the malicious intent.

**Command** ([[commands/run-hot-manchego-to-generate-vba]]):
```cmd
.\hot-manchego.exe .\blank.xlsm .\vba.txt
```

> Execute this from the directory with hot-manchego.exe and blank.xlsm. The tool reads the Excel structure, injects the obfuscated VBA based on the C# logic, and writes it to vba.txt. Success is indicated by the creation of vba.txt containing the VBA code, which can then be manually pasted into the Excel VBA editor (Alt+F11) under a module.
