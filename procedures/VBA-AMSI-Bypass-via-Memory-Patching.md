---
id: 302b309e-099c-49f9-ac62-2edcb52dd411
name: VBA-AMSI-Bypass-via-Memory-Patching
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.873981+00:00'
updated_at: '2023-04-10T20:36:59.460524+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
  - '[[techniques/Scripting|T1064 - Scripting]]'
  - '[[techniques/Software Packing|T1045 - Software Packing]]'
sub_techniques: []
tags:
  - '[[tags/Office - Attacks]]'
  - '[[tags/VBA - AMSI]]'
commands: []
platforms:
  - Windows
tools: []
validated: true
---

# VBA-AMSI-Bypass-via-Memory-Patching

## Summary

This procedure demonstrates how to bypass the Antimalware Scan Interface (AMSI) in Microsoft Office VBA macros by patching the memory of the AmsiScanBuffer function. It allows attackers to evade detection by security software and execute malicious VBA code within Office documents, such as Word or Excel macros, on Windows systems with AMSI-enabled applications.

## Description

AMSI is a Windows interface that enables applications like Microsoft Office to scan content for malware before execution. In VBA macros, AMSI inspects the code for malicious patterns. This bypass technique uses API calls to load amsi.dll, locate the AmsiScanBuffer function, alter its memory protection to writable, and overwrite it with shellcode that returns a non-malicious scan result (AMSI_RESULT_CLEAN). This effectively neuters the scan without removing AMSI entirely, allowing subsequent malicious code to run undetected. The technique is particularly useful in phishing campaigns or macro-based attacks targeting Office users. It requires 64-bit Office on Windows 10 or later, where AMSI is integrated. Success enables execution of payloads like downloaders or shells hidden in macros.

## Requirements

1. Microsoft Office (2016 or later) with VBA support enabled on a 64-bit Windows system.
2. Administrative privileges not required, but the macro must be enabled by the user (e.g., via trusting the document).
3. Access to edit VBA code in an Office document (e.g., .docm or .xlsm file).
4. Basic knowledge of VBA and Windows API declarations.

## Defense

Defensive measures and detection strategies:

- Regularly update and patch Microsoft Office applications to address known bypass vulnerabilities.
- Use endpoint protection software that monitors for AMSI tampering, such as unusual LoadLibrary calls to amsi.dll or memory modifications via VirtualProtect.
- Implement strict macro policies: Disable all macros by default and require digital signatures for trusted sources.
- Enable AMSI logging via PowerShell (Set-MpPreference -EnableControlledFolderAccess Enabled) and monitor Event ID 1102 in Windows Security logs for bypass attempts.
- Deploy application whitelisting (e.g., AppLocker) to restrict unsigned macros and use email/web filtering to block malicious Office attachments.

## Objectives

1. Patch the AmsiScanBuffer function to return clean scan results, bypassing AMSI detection.
2. Enable execution of obfuscated or malicious VBA code without triggering antivirus alerts.
3. Maintain stealth in Office-based attacks, allowing payload delivery via macros.

## Instructions

### Step 1: Prepare the VBA Environment

**Context**: Open the target Office document (e.g., Word .docm) and access the VBA editor (Alt+F11). Ensure macros are enabled and the document is trusted. This step sets up the environment for inserting the bypass code, which will run on Document_Open to automate the patch.

Insert the bypass script using the code snippet [[codes/VBA-AMSI-Bypass-Script]] into the ThisDocument module.

> This declares the necessary Windows API functions for DLL loading, address retrieval, memory protection changes, and copying. No command execution here; it's all VBA-based.

### Step 2: Define the Shellcode and Execute the Patch

**Context**: The core of the bypass involves creating a byte array representing shellcode that forces AmsiScanBuffer to return AMSI_RESULT_CLEAN (0x80070057). This step loads amsi.dll, retrieves the function address, makes the memory writable, and overwrites the first bytes of the function with the shellcode.

The shellcode is hardcoded in the VBA: MyByteArray with bytes {184, 87, 0, 7, 128, 195} (0xB8 0x57 0x00 0x07 0x80 0xC3), which assembles to mov eax, 0x80070057; ret. Execute by saving the macro and opening the document.

> Expected behavior: The Document_Open event triggers automatically, patching AMSI silently. No visible output in VBA, but subsequent malicious macros (e.g., shell spawners) will run without AMSI blocking.

### Step 3: Verify the Bypass and Test Malicious Code

**Context**: After patching, test by inserting and running known malicious VBA (e.g., a simple MsgBox with obfuscated payload). Monitor for detection; if AMSI is bypassed, the code executes without alerts.

Use PowerShell on the target to check AMSI status: Get-MpComputerStatus | Select-Object AmsiEnabled (should still show True, as the bypass is function-specific).

> If successful, AMSI remains enabled globally, but Office VBA scans fail to detect. Failure indicators: Antivirus popup or macro blocked. Retry if VirtualProtect returns 0 (check result variable for errors).
