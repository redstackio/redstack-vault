---
id: da14e31a-af29-4368-acda-a8a01ad57258
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:15.897866+00:00'
updated_at: '2023-04-10T20:19:32.545698+00:00'
---

# Code Snippet da14e31a

**Language**: Powershell

```powershell
PS Az> Get-AzResourceGroup
PS Az> Get-AzResourceGroupDeployment -ResourceGroupName SAP

# Export
PS Az> Save-AzResourceGroupDeploymentTemplate -ResourceGroupName <RESOURCE GROUP> -DeploymentName <DEPLOYMENT NAME>
cat <DEPLOYMENT NAME>.json # search for hardcoded password
cat <PATH TO .json FILE> | Select-String password
```
