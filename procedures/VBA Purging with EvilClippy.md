---
id: 73ad2795-e20f-4d34-8264-093941f8239f
name: VBA Purging with EvilClippy
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.836783+00:00'
updated_at: '2023-04-10T20:36:56.624120+00:00'
tags:
- '[[EvilClippy]]'
- '[[Office - Attacks]]'
- '[[VBA Purging]]'
commands:
- '[[Compile EvilClippy.exe on OSX/Linux]]'
- '[[Compile EvilClippy.exe on Windows]]'
- '[[Confuse analysis tools with -r flag]]'
- '[[Generate malicious macro with fake.vbs script]]'
- '[[Inject fake VBA code into macrofile.doc for Office 2013 x64]]'
- '[[Inject fake VBA code into macrofile.doc for Office 2016 x86]]'
- '[[Mark project as locked and unviewable]]'
---

# VBA Purging with EvilClippy

## Summary

VBA Purging with EvilClippy is a technique used to bypass security controls in Microsoft Office documents. This technique involves removing the VBA code from a document and replacing it with a malicious payload. EvilClippy is a tool that automates this process, making it easier for attackers to cre

## Description

# Description

VBA Purging with EvilClippy is a technique used to bypass security controls in Microsoft Office documents. This technique involves removing the VBA code from a document and replacing it with a malicious payload. EvilClippy is a tool that automates this process, making it easier for attackers to create malicious documents without being detected.

From an offensive perspective, this technique can be used to deliver a payload to a victim's machine without being detected by traditional antivirus software. The technical explanation is that EvilClippy removes the VBA code from a document and replaces it with a malicious payload. This allows the attacker to deliver the payload without triggering any alarms or alerts.

The business value of this technique is that it allows attackers to bypass security controls and deliver malware to a victim's machine. This can lead to data theft, system compromise, and other malicious activities.

 

## Requirements

1. A Microsoft Office document with VBA code

1. EvilClippy tool

 

## Defense

1. Ensure that all Microsoft Office documents are scanned for malicious content

1. Implement a least privilege model for users to prevent unauthorized execution of malicious documents

1. Use endpoint detection and response (EDR) tools to detect and respond to malicious activity

 

## Objectives

1. To bypass security controls in Microsoft Office documents

1. To deliver a malicious payload to a victim's machine

1. To avoid detection by traditional antivirus software

 

# Instructions

1. EvilClippy is a tool used to create malicious Microsoft Office macros. The tool can be used to obfuscate and hide malicious macros from detection by security tools. The tool provides multiple commands to create malicious macros such as -s, -g, -t, and -r. The -s command is used to specify the name of the VBA script file to add to the macro. The -g command is used to generate an obfuscated version of the macro. The -t command is used to specify the version of Microsoft Office to target. The -r command is used to remove the VBA source code from the macro and leave only the compiled code. EvilClippy can also mark the project as locked and unviewable using the -u command.

 



**Code**: [[# OSX/Linux
mcs /reference:OpenMcdf.dll,System.IO.]]



> The 'data' field of this JSON object provides the command line instructions to use EvilClippy. The 'lang' field specifies the language used to write the tool. The 'instruction' field provides a brief overview of EvilClippy and its commands. The 'explain' field provides a detailed explanation of the commands used in EvilClippy.



**Command** ([[Compile EvilClippy.exe on OSX/Linux]]):

```bash
mcs /reference:OpenMcdf.dll,System.IO.Compression.FileSystem.dll /out:EvilClippy.exe *.cs
```





**Command** ([[Compile EvilClippy.exe on Windows]]):

```bash
csc /reference:OpenMcdf.dll,System.IO.Compression.FileSystem.dll /out:EvilClippy.exe *.cs
```





**Command** ([[Generate malicious macro with fake.vbs script]]):

```bash
EvilClippy.exe -s fake.vbs -g -r cobaltstrike.doc
```





**Command** ([[Inject fake VBA code into macrofile.doc for Office 2016 x86]]):

```bash
EvilClippy.exe -s fakecode.vba -t 2016x86 macrofile.doc
```





**Command** ([[Inject fake VBA code into macrofile.doc for Office 2013 x64]]):

```bash
EvilClippy.exe -s fakecode.vba -t 2013x64 macrofile.doc
```





**Command** ([[Mark project as locked and unviewable]]):

```bash
EvilClippy.exe -u macrofile.doc
```





**Command** ([[Confuse analysis tools with -r flag]]):

```bash
EvilClippy.exe -r macrofile.doc
```



## Commands Used

- [[Compile EvilClippy.exe on OSX/Linux]]
- [[Compile EvilClippy.exe on Windows]]
- [[Confuse analysis tools with -r flag]]
- [[Generate malicious macro with fake.vbs script]]
- [[Inject fake VBA code into macrofile.doc for Office 2013 x64]]
- [[Inject fake VBA code into macrofile.doc for Office 2016 x86]]
- [[Mark project as locked and unviewable]]

## Tags

- [[EvilClippy]]
- [[Office - Attacks]]
- [[VBA Purging]]


