---
id: 6b47abf8-c412-4b07-8f96-0ed5b9741402
name: Disable Script Logging and Clear Signatures
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.978013+00:00'
updated_at: '2023-04-10T20:36:17.611905+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Impair Defenses|T1562 - Impair Defenses]]'
- '[[Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
tags:
- '[[Disable Script Logging]]'
commands:
- '[[Disable Script Block Logging]]'
---

# Disable Script Logging and Clear Signatures

## Summary

This procedure involves disabling PowerShell script logging and clearing script block signatures to evade detection by security monitoring tools. By disabling script logging, attackers can prevent their malicious activities from being logged and detected by defenders. Clearing script block signatur

## Description

# Description

This procedure involves disabling PowerShell script logging and clearing script block signatures to evade detection by security monitoring tools. By disabling script logging, attackers can prevent their malicious activities from being logged and detected by defenders. Clearing script block signatures helps to further cover the attacker's tracks by removing any evidence of the malicious scripts that were executed. This technique is commonly used in post-exploitation activities and can help attackers maintain persistence in a compromised environment.

 

## Requirements

1. Access to PowerShell

1. Privileged access to disable script logging

 

## Defense

1. Implement strict access controls to limit privileged access

1. Monitor for changes to PowerShell logging settings

1. Regularly review PowerShell logs for any suspicious activity

 

## Objectives

1. Disable PowerShell script logging to avoid detection

1. Clear script block signatures to remove evidence of malicious activity

1. Maintain persistence in a compromised environment

 

# Instructions

1. To disable PowerShell ScriptBlock Logging, run the following command:

 



**Code**: [[$settings = [Ref].Assembly.GetType("System.Managem]]



> This command disables ScriptBlock logging in PowerShell by setting the value of "EnableScriptBlockLogging" to 0 in the registry key "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging". This prevents PowerShell from logging any executed commands and arguments in the ScriptBlock logs. 



**Command** ([[Disable Script Block Logging]]):

```bash
$settings = [Ref].Assembly.GetType(\"System.Management.Automation.Utils\").GetField(\"cachedGroupPolicySettings\",\"NonPublic,Static\").GetValue($null);\n$settings[\"HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows\\PowerShell\\ScriptBlockLogging\"] = @{}\n$settings[\"HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows\\PowerShell\\ScriptBlockLogging\"].Add(\"EnableScriptBlockLogging\", \"0\")
```



2. This command clears the signature cache of PowerShell ScriptBlocks.

 



**Code**: [[[Ref].Assembly.GetType("System.Management.Automati]]



> The signature cache is used to store previously verified signatures of ScriptBlocks. This command clears the cache and forces PowerShell to re-verify the signatures the next time the ScriptBlock is executed. This can be useful in situations where the signature of a ScriptBlock has changed and needs to be re-verified.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Impair Defenses|T1562 - Impair Defenses]]
- [[Indicator Removal on Host|T1070 - Indicator Removal on Host]]

## Commands Used

- [[Disable Script Block Logging]]

## Tags

- [[Disable Script Logging]]


