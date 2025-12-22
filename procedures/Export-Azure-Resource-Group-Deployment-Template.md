---
id: bd661e30-4844-4c6f-9bea-606723d7e3f3
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:15.899432+00:00'
updated_at: '2023-04-10T20:19:32.527752+00:00'
tactics:
  - '[[Defense Evasion]]'
  - '[[Discovery]]'
techniques:
  - '[[Obfuscated Files or Information]]'
  - '[[System Information Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Deployment Template]]'
commands:
  - '[[commands/get-az-resourcegroup-list-all]]'
  - '[[commands/get-az-resourcegroup-deployment]]'
  - '[[commands/save-az-resourcegroup-deployment-template]]'
  - '[[commands/search-json-for-passwords-powershell]]'
platforms:
  - Azure
tools:
  - '[[tools/Az-PowerShell]]'
validated: true
---

# Export-Azure-Resource-Group-Deployment-Template

## Summary

This procedure exports the JSON template for an Azure Resource Group deployment using PowerShell commands from the Az module. The resulting template captures the configuration of resources like virtual machines, storage accounts, and networking components, allowing recreation in another environment or analysis for modifications. Offensively, it enables discovery of deployment structures to identify potential vulnerabilities or hardcoded secrets; defensively, it supports consistent deployments and secure updates.

## Description

In an offensive security context, exporting an Azure Resource Group deployment template provides attackers with detailed insights into the infrastructure, including resource configurations that may reveal misconfigurations, exposed secrets, or attack paths. The procedure retrieves the template in JSON format, which can be inspected for sensitive data like passwords or keys. Defensively, it aids in auditing and replicating secure deployments across environments. Technically, it leverages Azure PowerShell cmdlets to query and save the deployment state, requiring appropriate subscription access. This maps to discovery of cloud resources and evasion through template obfuscation or analysis.

## Requirements

1. Active Azure subscription with access to the target resource group.
2. Azure PowerShell module (Az) installed and authenticated via Connect-AzAccount.
3. Permissions: Reader or Contributor role on the resource group to view and export deployments.
4. PowerShell environment (Windows, Linux, or macOS with PowerShell Core).

## Defense

- Restrict Azure RBAC roles to least privilege, limiting export permissions to authorized users only.
- Enable Azure Activity Logs and monitor for Get-AzResourceGroupDeployment and Save-AzResourceGroupDeploymentTemplate executions via Azure Sentinel or Microsoft Defender for Cloud.
- Use Azure Policy to enforce no hardcoded secrets in templates and scan exports with tools like Azure AD Privileged Identity Management.
- Regularly audit resource groups for unexpected exports and implement just-in-time access.

## Objectives

1. Retrieve and export the JSON template of an Azure Resource Group deployment for analysis or replication.
2. Inspect the template for hardcoded credentials or sensitive configurations to identify vulnerabilities (offensive use).
3. Ensure deployment consistency and facilitate secure modifications (defensive use).

## Instructions

### Step 1: List All Resource Groups

**Context**: Begin by listing all available resource groups in the subscription to identify the target group for export. This step provides an overview of the environment and confirms access.

**Command** ([[commands/get-az-resourcegroup-list-all]]):
```powershell
Get-AzResourceGroup
```

> This command outputs a table of resource groups, including names, locations, and provisioning states. Use this to select the target resource group name for subsequent steps.

### Step 2: Retrieve Deployments for the Target Resource Group

**Context**: Once the resource group is identified, query its deployments to list available templates. This reveals historical or current deployments that can be exported.

**Command** ([[commands/get-az-resourcegroup-deployment]]):
```powershell
Get-AzResourceGroupDeployment -ResourceGroupName $_RESOURCE_GROUP_NAME
```

> Expected output is a list of deployments with names, timestamps, and modes (e.g., Incremental or Complete). Note the deployment name for export.

### Step 3: Export the Deployment Template

**Context**: Export the selected deployment as a JSON template file. This captures the full resource configuration for review or reuse.

**Command** ([[commands/save-az-resourcegroup-deployment-template]]):
```powershell
Save-AzResourceGroupDeploymentTemplate -ResourceGroupName $_RESOURCE_GROUP_NAME -DeploymentName $_DEPLOYMENT_NAME
```

> The command saves a JSON file named after the deployment in the current directory. Verify the file creation and open it for inspection.

### Step 4: Search for Hardcoded Secrets in the Template

**Context**: Analyze the exported JSON for sensitive information like passwords or keys, which could indicate misconfigurations exploitable by attackers.

**Command** ([[commands/search-json-for-passwords-powershell]]):
```powershell
Get-Content $_JSON_FILE_PATH | Select-String -Pattern "password"
```

> This scans the JSON content and outputs lines containing "password". Review matches manually to confirm if they are hardcoded secrets; if none found, the template is likely secure.
