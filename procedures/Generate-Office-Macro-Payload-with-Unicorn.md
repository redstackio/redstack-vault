---
id: 74a3e0a7-cb60-4933-8c75-a4ddfc34fa86
type: procedure
name: Generate-Office-Macro-Payload-with-Unicorn
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.454876+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/User Execution|T1204 - User Execution]]'
  - '[[techniques/Scheduled Task|T1053 - Scheduled Task]]'
sub_techniques:
  - '[[sub-techniques/Scheduled Task|T1053.005 - Scheduled Task]]'
tags:
  - office-macro
  - vba
  - payload-generation
  - office-attacks
commands:
  - '[[commands/unicorn-generate-macro-payload]]'
tools:
  - '[[tools/Unicorn-Payload-Generator]]'
platforms:
  - Windows
validated: true
---

# Generate-Office-Macro-Payload-with-Unicorn

## Summary

This procedure uses the Unicorn tool to generate a C# payload suitable for embedding in an Office VBA macro, enabling execution of arbitrary code when the macro is run in Microsoft Office applications like Word or Excel. It is commonly used in phishing campaigns or social engineering attacks to deliver payloads that establish persistence or escalate privileges on a target Windows system.

## Description

Unicorn is a lightweight tool for converting shellcode into various formats, including C# code that can be adapted for VBA macros in Office documents. The generated payload typically includes shellcode for reverse shells, downloaders, or scheduled tasks. This procedure focuses on generating the C# payload file, which can then be manually or automatically converted into VBA syntax for insertion into a malicious .docm or .xlsm file. The technique relies on user execution of the macro (T1204) and may involve scheduled tasks (T1053) if the payload implements persistence. It targets Windows environments where Microsoft Office is installed, assuming the target user enables macros. Prerequisites include a Python environment and access to Unicorn. Success results in a payload.cs file ready for VBA conversion, allowing attackers to bypass some macro security controls.

## Requirements

1. Python 2.7 or 3.x installed on the attacker's machine.
2. Unicorn tool installed and accessible in the PATH.
3. Basic knowledge of shellcode formats (e.g., for reverse shells or Meterpreter).
4. Optional: A VBA conversion script or manual editing tools for final macro integration.
5. Attacker-controlled listener (e.g., netcat or Metasploit) if the payload includes callbacks.

## Defense

- Disable macros by default in Office applications or require explicit user approval.
- Use antivirus/EDR solutions that scan for suspicious VBA code or block unsigned macros.
- Implement email filtering to detect attachments with potential macro content.
- Enable Office macro logging and monitor for anomalous scheduled task creation.

## Objectives

1. Generate a C# payload file using Unicorn for Office macro embedding.
2. Prepare the payload for conversion to VBA syntax.
3. Enable code execution on the target system via user-enabled macros.
4. Establish initial foothold or persistence through the delivered payload.

## Instructions

### Step 1: Prepare the Environment

**Context**: Ensure Unicorn is installed and ready. This step verifies the tool's availability and sets up the working directory to avoid errors during generation.

If Unicorn is not installed, clone the repository from GitHub:

```bash
git clone https://github.com/trustedsec/unicorn.git
cd unicorn
```

> This downloads the Unicorn tool. Expected output: Repository cloned successfully, with unicorn.py in the current directory. Verify by running `python unicorn.py --help` to see usage options.

### Step 2: Generate the C# Macro Payload

**Context**: Use Unicorn to create a C# payload from shellcode. Specify the output as a .cs file targeted for macro use, which embeds the shellcode in a format compatible with VBA conversion.

**Command** ([[commands/unicorn-generate-macro-payload]]):

```bash
python unicorn.py payload.cs cs macro
```

> This command invokes Unicorn to generate payload.cs in C# format optimized for Office macros. The 'cs' argument specifies C# language, and 'macro' indicates the target format. Replace 'payload.cs' with your desired filename if needed. Expected output: A new file 'payload.cs' created in the current directory, containing C# code with embedded shellcode (e.g., for a reverse shell). The file size should be small (under 10KB) and include Base64-encoded shellcode.

### Step 3: Verify and Convert the Payload

**Context**: Inspect the generated file and perform basic conversion to VBA. This ensures the payload is functional before embedding in an Office document.

Open payload.cs in a text editor and review the content. To convert to VBA, use a tool like the OfficeMalScanner or manual copy-paste, adapting C# syntax to VBA (e.g., replace C# classes with VBA Sub procedures).

Example manual adaptation snippet (for illustration):

```vba
Sub AutoOpen()
    ' Adapted from payload.cs shellcode execution
    Dim shellcode As String
    shellcode = "[Base64 shellcode from payload.cs]"
    ' Execute shellcode using VBA APIs
End Sub
```

> Expected output: Valid VBA code that compiles without errors when pasted into an Office macro editor. Test in a sandboxed environment to confirm execution (e.g., connects back to listener). If conversion fails, check for syntax mismatches between C# and VBA.

### Step 4: Embed in Office Document

**Context**: Integrate the converted VBA into a malicious Office file for delivery. This finalizes the payload for phishing or drive-by delivery.

Create a new Word/Excel document, enable Developer tab, and insert the VBA code into ThisDocument or a module. Save as .docm or .xlsm.

> Expected output: A macro-enabled Office file that prompts for macro enabling on open. Success is confirmed by executing the macro in a test VM and observing payload behavior (e.g., shell spawn).
