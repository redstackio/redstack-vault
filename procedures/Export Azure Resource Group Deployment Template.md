---
id: bd661e30-4844-4c6f-9bea-606723d7e3f3
name: Export Azure Resource Group Deployment Template
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:15.899432+00:00'
updated_at: '2023-04-10T20:19:32.527752+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Cloud - Azure]]'
- '[[Deployment Template]]'
---

# Export Azure Resource Group Deployment Template

## Summary

The Export Azure Resource Group Deployment Template procedure is used to export the JSON template for an Azure Resource Group deployment. This template can then be used to recreate the same deployment in another environment or to make changes to the deployment before redeploying it. This procedure 

## Description

# Description

The Export Azure Resource Group Deployment Template procedure is used to export the JSON template for an Azure Resource Group deployment. This template can then be used to recreate the same deployment in another environment or to make changes to the deployment before redeploying it. This procedure can be used both offensively and defensively. Offensively, an attacker can use this procedure to gain insight into an organization's deployment structure and potentially identify vulnerabilities. Defensively, this procedure can be used to ensure consistency across deployments and to make changes to deployments in a controlled manner.

From a technical perspective, the Export Azure Resource Group Deployment Template procedure retrieves the JSON template for an Azure Resource Group deployment. The template includes all of the resources that make up the deployment, including virtual machines, storage accounts, and networking resources. The template can be edited to make changes to the deployment or to create a new deployment in another environment. 

The business value of this procedure is that it allows organizations to easily recreate deployments in different environments or to make changes to deployments in a controlled manner. This can help to ensure consistency across deployments and reduce the risk of errors or misconfigurations.

## Requirements

1. Access to an Azure subscription

1. Permission to view and export Azure Resource Group deployments

## Defense

1. Ensure that access to Azure subscriptions is restricted to authorized personnel only

1. Monitor for unauthorized access to Azure Resource Group deployments

1. Regularly review and update Azure Resource Group deployments to ensure they are configured securely

## Objectives

1. To export the JSON template for an Azure Resource Group deployment

1. To gain insight into an organization's deployment structure (offensive)

1. To ensure consistency across deployments (defensive)

# Instructions

1. To export an Azure Resource Group Deployment Template, follow these steps:
1. Use the 'Get-AzResourceGroup' command to retrieve the resource group you want to export.
2. Use the 'Get-AzResourceGroupDeployment' command to retrieve the deployment you want to export.
3. Use the 'Save-AzResourceGroupDeploymentTemplate' command to export the deployment template. Specify the resource group name and deployment name.
4. Use the 'cat' command to search for hardcoded passwords in the exported JSON file.
5. Review the exported JSON file to ensure that no sensitive information is present.

**Code**: [[PS Az> Get-AzResourceGroup
PS Az> Get-AzResourceGr]]

> This command exports an Azure Resource Group Deployment Template to a JSON file. The exported JSON file can be used to recreate the deployment in the future. It is important to review the exported JSON file to ensure that no sensitive information, such as hardcoded passwords, is present.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Tags

- [[Cloud - Azure]]
- [[Deployment Template]]
