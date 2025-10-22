---
id: c9a4ec32-0370-4443-99e1-2c8614bd0cbd
name: XLM Excel 4.0 GruntHttp Payload Generation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.305976+00:00'
updated_at: '2023-04-10T20:36:57.297295+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Dynamic Data Exchange|T1173 - Dynamic Data Exchange]]'
tags:
- '[[Office - Attacks]]'
- '[[XLM Excel 4.0 - EXCELntDonut]]'
---

# XLM Excel 4.0 GruntHttp Payload Generation

## Summary

The XLM Excel 4.0 GruntHttp Payload Generation procedure is used to generate a payload that can be used to execute arbitrary code on a target system. This payload is generated using the GruntHttp tool and is delivered via an Excel 4.0 macro. The payload is designed to bypass traditional antivirus a

## Description

# Description

The XLM Excel 4.0 GruntHttp Payload Generation procedure is used to generate a payload that can be used to execute arbitrary code on a target system. This payload is generated using the GruntHttp tool and is delivered via an Excel 4.0 macro. The payload is designed to bypass traditional antivirus and endpoint detection and response solutions. The GruntHttp tool is used to generate the payload, which is then inserted into an Excel 4.0 macro. When the macro is executed, the payload is delivered to the target system and executed. This technique is effective because it does not rely on any external tools or libraries, and it can be executed using standard Microsoft Office functionality.

## Requirements

1. Access to a target system running Microsoft Office

1. Ability to generate a payload using the GruntHttp tool

1. Knowledge of Excel 4.0 macro execution

## Defense

1. Implement strong endpoint protection solutions that can detect and block malicious Excel 4.0 macros

1. Educate users on the risks of opening Excel files from unknown or untrusted sources

1. Monitor network traffic for suspicious activity, including traffic associated with GruntHttp payloads

## Objectives

1. Deliver and execute arbitrary code on a target system

1. Bypass traditional antivirus and endpoint detection and response solutions

# Instructions

1. This command generates a GruntHttp payload using the EXCELntDonut tool. Here are the arguments that you can use:

-f: This flag specifies the path to the file containing your C# source code (exe or dll).
-c: This flag specifies the ClassName where the method that you want to call lives (dll).
-m: This flag specifies the method containing your executable payload (dll).
-r: This flag specifies the references needed to compile your C# code (ex: -r 'System.Management').
-o: This flag specifies the output filename.
--sandbox: This flag performs basic sandbox checks.
--obfuscate: This flag performs basic macro obfuscation.

After running the above command, you can use the GruntHttp payload by following the instructions provided in the 'text' field.

**Code**: [[git clone https://github.com/FortyNorthSecurity/EX]]

> 

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Dynamic Data Exchange|T1173 - Dynamic Data Exchange]]

## Tags

- [[Office - Attacks]]
- [[XLM Excel 4.0 - EXCELntDonut]]
