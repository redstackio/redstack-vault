---
id: da14e31a-af29-4368-acda-a8a01ad57258
type: code
language: Powershell
verified: true
created_at: '2023-04-06T03:56:15.897866+00:00'
updated_at: '2023-04-10T20:19:32.545698+00:00'
platforms:
  - Azure
tags:
  - export
  - template
  - azure
validated: true
---

# Export-Azure-Deployment-Template-Script

## Code

```powershell
PS Az> Get-AzResourceGroup
PS Az> Get-AzResourceGroupDeployment -ResourceGroupName SAP

# Export
PS Az> Save-AzResourceGroupDeploymentTemplate -ResourceGroupName <RESOURCE GROUP> -DeploymentName <DEPLOYMENT NAME>
cat <DEPLOYMENT NAME>.json # search for hardcoded password
cat <PATH TO .json FILE> | Select-String password
```

## Description

This PowerShell script sequence lists Azure resource groups, retrieves deployments for a specific group, exports the deployment template to JSON, and searches the file for hardcoded passwords. It supports discovery of cloud configurations and secret hunting in offensive operations.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <RESOURCE GROUP> | Name of the Azure resource group | SAP |
| <DEPLOYMENT NAME> | Name of the deployment to export | SAPDeployment |
| <PATH TO .json FILE> | Full path to the exported JSON file | C:\SAPDeployment.json |

## Usage

Execute in an authenticated PowerShell session with Az module loaded. Use after connecting via Connect-AzAccount. The script outputs lists and saves the JSON file; review the search results for secrets. Integrate into red team workflows for Azure enumeration or defensive audits.

## Detection

- Monitor Azure PowerShell executions in Activity Logs for Get-AzResourceGroupDeployment and Save-AzResourceGroupDeploymentTemplate.
- Detect file creations of JSON templates in unexpected locations or searches for sensitive patterns via EDR tools like Microsoft Defender.
- Alert on Az module imports outside approved sessions.

## Related

- [[procedures/Export-Azure-Resource-Group-Deployment-Template]]
- [[tools/Az-PowerShell]]
