---
id: c59a05e2-95e5-43ec-ad37-c5ad756de4fe
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.795281+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005]]'
  - '[[tactics/Execution|TA0002]]'
techniques:
  - '[[techniques/Obfuscated Files or Information|T1027]]'
  - '[[techniques/Command and Scripting Interpreter|T1059.005]]'
sub_techniques: []
tags:
  - Office Attacks
  - OfficePurge
  - VBA Purging
commands:
  - '[[commands/officepurge-list-macros-in-document]]'
  - '[[commands/officepurge-purge-and-execute-word-macro]]'
  - '[[commands/officepurge-purge-and-execute-excel-module]]'
  - '[[commands/officepurge-purge-and-execute-publisher-macro]]'
platforms:
  - Windows
tools:
  - '[[tools/OfficePurge]]'
skill_level: intermediate
impact_level: medium
detection_risk: high
validated: true
---

# VBA-Purging-with-OfficePurge

## Summary

This procedure uses the OfficePurge tool to remove or obfuscate unnecessary VBA code from Microsoft Office documents (Word, Excel, Publisher), allowing attackers to execute malicious macros while evading antivirus detection that relies on common VBA keywords and structures.

## Description

VBA Purging involves stripping compressed or redundant VBA code from Office files to reduce detectable signatures, making malicious payloads harder for security tools to identify. OfficePurge modifies the document's VBA project by purging non-essential modules while preserving and executing the targeted malicious macro. This technique is useful in campaigns where initial access is gained via phishing or malicious attachments, and evasion is critical to maintain persistence or execute further payloads. It targets Windows environments with Microsoft Office installed and requires local access to the document file. Success results in a modified document that runs the macro without triggering common AV heuristics.

## Requirements

1. Local access to the target Office document containing VBA macros (Word .doc, Excel .xls/.xlsx, Publisher .pub).
2. OfficePurge tool installed and executable on a Windows system.
3. Administrative or user-level permissions to modify files (no elevated privileges typically needed).
4. Knowledge of the malicious macro module name within the document.

## Defense

- Keep Microsoft Office updated with the latest security patches to address macro-related vulnerabilities.
- Enable macro security settings to disable all macros by default or require digital signatures.
- Deploy endpoint detection tools that monitor file modifications and VBA project changes.
- Use antivirus software with behavioral analysis for Office documents and block unsigned macros.
- Educate users to avoid opening attachments from untrusted sources and enable Protected View.

## Objectives

1. Obfuscate VBA macros in Office documents to bypass signature-based detection.
2. Execute a specific malicious macro post-purging without alerting security solutions.
3. Maintain stealth in attacks involving Office-based payloads for initial execution or persistence.

## Instructions

### Step 1: List Available Macros in the Document

**Context**: Before purging, identify the macros and modules present in the Office document to select the malicious one for execution while purging others. This helps avoid accidental removal of the payload.

**Command** ([[commands/officepurge-list-macros-in-document]]):
```cmd
OfficePurge.exe -d $_DOCUMENT_TYPE -f $_FILE_PATH -l
```

> Run this command to enumerate macros. Replace $_DOCUMENT_TYPE with 'word', 'excel', or 'publisher'; $_FILE_PATH with the path to your document (e.g., .\malicious.doc). Expected output is a list of available modules/macros, such as 'Module1', 'NewMacros', or 'ThisDocument'. Verify the malicious module is listed.

### Step 2: Purge and Execute Macro in Word Document

**Context**: Target a Word document to purge unnecessary VBA code and execute the specified malicious macro, stripping keywords that AV engines detect.

**Command** ([[commands/officepurge-purge-and-execute-word-macro]]):
```cmd
OfficePurge.exe -d word -f $_FILE_PATH -m $_MODULE_NAME
```

> Execute this on a Word file (e.g., -f .\malicious.doc -m NewMacros). The tool modifies the file by removing compressed VBA elements and runs the named macro. Expected output confirms purging and execution success, with the document now obfuscated.

### Step 3: Purge and Execute Module in Excel Document

**Context**: Apply purging to an Excel workbook to clean VBA modules, enabling stealthy execution of the targeted module.

**Command** ([[commands/officepurge-purge-and-execute-excel-module]]):
```cmd
OfficePurge.exe -d excel -f $_FILE_PATH -m $_MODULE_NAME
```

> Use for Excel files (e.g., -f .\payroll.xls -m Module1). Post-execution, open the file in Excel to verify the macro runs without detection flags. Expected output indicates successful purge and module execution.

### Step 4: Purge and Execute Macro in Publisher Document

**Context**: Extend the technique to Publisher files, purging VBA to execute the document's macro while evading scans.

**Command** ([[commands/officepurge-purge-and-execute-publisher-macro]]):
```cmd
OfficePurge.exe -d publisher -f $_FILE_PATH -m $_MODULE_NAME
```

> Target Publisher files (e.g., -f .\donuts.pub -m ThisDocument). The command processes the file, removing detectable code. Expected output shows purge completion; test by opening in Publisher to confirm macro execution.
