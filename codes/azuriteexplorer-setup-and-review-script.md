---
id: 35a32f0f-0a2a-4fa6-902b-b42f4945cdaf
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:14.586128+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - azurite
  - subscription
validated: true
---

# azuriteexplorer-setup-and-review-script

## Code

```powershell
git submodule init
git submodule update
PS> Import-Module AzureRM
PS> Import-Module AzuriteExplorer.ps1
PS> Review-AzureRmSubscription
PS> Review-CustomAzureRmSubscription
```

## Description

Sets up AzuriteExplorer by initializing submodules, importing AzureRM and custom module, then reviewing subscriptions for recon.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Assumes Git repo cloned and AzureRM installed | N/A |

## Usage

Clone AzuriteExplorer repo, run git commands, then import and review. Outputs subscription details and resources for enumeration.

## Detection

- Git submodule activity in temp dirs.
- Import-Module calls for AzuriteExplorer.ps1.
- AzureRM queries for subscription lists.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/AzuriteExplorer]]
