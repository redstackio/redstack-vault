---
id: c10df431-fdf2-4a07-8aa9-6fa098ea67c9
name: XLSM - Hot Manchego VBA Macro Generation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.204572+00:00'
updated_at: '2023-04-10T20:36:49.309367+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
sub_techniques:
- '[[Compile After Delivery|T1027.004 - Compile After Delivery]]'
- '[[Software Packing|T1027.002 - Software Packing]]'
tags:
- '[[Office - Attacks]]'
- '[[XLSM - Hot Manchego]]'
commands:
- '[[Compile C# code]]'
- '[[Create new Excel file]]'
- '[[Generate CS Macro]]'
---

# XLSM - Hot Manchego VBA Macro Generation

## Summary

The XLSM - Hot Manchego VBA Macro Generation procedure involves generating an obfuscated VBA macro from C# code that can be used to execute malicious commands. This technique can be used to bypass security controls such as antivirus software and can allow an attacker to execute code on a victim's m

## Description

# Description

The XLSM - Hot Manchego VBA Macro Generation procedure involves generating an obfuscated VBA macro from C# code that can be used to execute malicious commands. This technique can be used to bypass security controls such as antivirus software and can allow an attacker to execute code on a victim's machine. The VBA macro can be delivered via a spear-phishing email or an infected document. 

The technical process involves writing C# code that generates an obfuscated VBA macro. The VBA macro can then be pasted into a Microsoft Excel file and executed when the file is opened. The VBA macro can then execute any commands that the attacker has programmed it to do, such as downloading and executing additional malware or exfiltrating data. 

The business value of this procedure is that it can be used to gain access to sensitive information or systems. This can be used for espionage, financial gain, or to disrupt business operations.

 

## Requirements

1. Access to a C# compiler

1. Access to a Microsoft Excel file

 

## Defense

1. Disable or restrict the use of VBA macros in Microsoft Office

1. Implement email security controls to prevent spear-phishing attacks

1. Use antivirus software to detect and block malicious files and macros

 

## Objectives

1. Generate an obfuscated VBA macro from C# code

1. Deliver the VBA macro to a victim via a spear-phishing email or infected document

1. Execute malicious commands on the victim's machine

 

# Instructions

1. To generate a VBA macro from C# code, follow these steps:
1. Create a new Excel workbook and save it as 'blank.xlsm'.
2. Open PowerShell and navigate to the folder containing the C# code.
3. Run the following command to compile the code and create the macro:
   C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe /reference:EPPlus.dll hot-manchego.cs
4. Run the following command to generate the macro:
   .\hot-manchego.exe .\blank.xlsm .\vba.txt
5. The VBA macro will be saved to 'vba.txt' in the same folder as the C# code.

 



**Code**: [[Generate CS Macro and save it to Windows as vba.tx]]



> This command generates a VBA macro from C# code. The 'hot-manchego.cs' file contains the C# code for the macro. The 'blank.xlsm' file is a new Excel workbook that will be used to create the macro. The 'vba.txt' file is where the generated macro will be saved. The 'csc.exe' command is used to compile the C# code and the 'hot-manchego.exe' command is used to generate the macro. The 'EPPlus.dll' file is a reference that is needed to compile the C# code.



**Command** ([[Create new Excel file]]):

```bash
New-Item blank.xlsm
```





**Command** ([[Compile C# code]]):

```bash
C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe /reference:EPPlus.dll hot-manchego.cs
```





**Command** ([[Generate CS Macro]]):

```bash
.\hot-manchego.exe .\blank.xlsm .\vba.txt
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

### Sub-Techniques

- [[Compile After Delivery|T1027.004 - Compile After Delivery]]
- [[Software Packing|T1027.002 - Software Packing]]

## Commands Used

- [[Compile C# code]]
- [[Create new Excel file]]
- [[Generate CS Macro]]

## Tags

- [[Office - Attacks]]
- [[XLSM - Hot Manchego]]


