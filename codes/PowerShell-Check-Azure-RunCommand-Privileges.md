---
id: c04eace7-a485-4a41-94cf-fa4eb6e17086
type: code
language: Powershell
verified: true
created_at: '2023-05-24T08:08:13.412672+00:00'
updated_at: '2023-05-24T08:08:13.433836+00:00'
tags:
  - azure
  - privileges
  - runcommand
  - escalation
platforms:
  - Azure
  - Cloud
validated: true
---

# PowerShell-Check-Azure-RunCommand-Privileges

## Code

```powershell
# Check for runCommand privileges
$Token = 'eyJ0eX..'
$URI = 'https://management.azure.com/subscriptions/b3d2186f-0d10-4944-1c88-d7d853d36886/resourceGroups/<RG-NAME>/providers/Microsoft.Compute/virtualMachines/<RESOURCE/providers/Microsoft.Authorization/permissions?apiversion=2015-07-01'
$RequestParams = @{
 Method = 'GET'
 Uri = $URI
 Headers = @{
 'Authorization' = "Bearer $Token"
 }
}
(Invoke-RestMethod @RequestParams).value 
```

## Description

This PowerShell script queries the Azure Authorization API to check permissions on a specific virtual machine within a resource group, focusing on actions like runCommand for potential remote execution capabilities.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $Token | Valid Azure bearer token | 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik...' |
| $URI | Permissions endpoint with placeholders for subscription, RG, and resource | 'https://management.azure.com/subscriptions/.../permissions?apiversion=2015-07-01' |
| <RG-NAME> | Resource group name | 'prod-rg' |
| <RESOURCE> | Virtual machine name | 'target-vm' |

## Usage

Substitute placeholders and execute to retrieve permission sets. Search output for 'Microsoft.Compute/virtualMachines/runCommand' with 'write' actions to confirm escalation potential. Used in privilege checking phases.

## Detection

- Audit logs for /Microsoft.Authorization/permissions queries on Compute resources.
- Behavioral analytics on token-driven API calls targeting VM permissions.
- Integration with Microsoft Defender for Cloud for privilege access alerts.

## Related

- [[procedures/Azure-Resource-Management-and-Privilege-Checking-with-PowerShell]]
