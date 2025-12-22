---
id: 48fd856f-d742-43bd-bd56-5ceb68119e20
type: code
language: Powershell
verified: true
created_at: '2023-05-24T08:08:13.412515+00:00'
updated_at: '2023-05-24T08:08:13.433836+00:00'
tags:
  - azure
  - resources
  - permissions
  - recon
platforms:
  - Azure
  - Cloud
validated: true
---

# PowerShell-List-Azure-Resources-and-Permissions

## Code

```powershell
# Retrieve a list of subscriptions
$Token = 'eyJ0eX..'
$URI = 'https://management.azure.com/subscriptions/b3d2186f-0d10-4944-1c88-d7d853d36886/resources?api-version=2020-10-01'
$RequestParams = @{
 Method = 'GET'
 Uri = $URI
 Headers = @{
 'Authorization' = "Bearer $Token"
 }
}
(Invoke-RestMethod @RequestParams).value 

# List resources and check for runCommand privileges
$URI = 'https://management.azure.com/subscriptions/b3d2186f-0d10-4944-1c88-d7d853d36886/resourceGroups/<RG-NAME>/providers/Microsoft.Compute/virtualMachines/<RESOURCE/providers/Microsoft.Authorization/permissions?apiversion=2015-07-01'
```

## Description

This script first lists all resources in a specified Azure subscription using the Management API. It then prepares a URI for querying permissions on a virtual machine resource, enabling checks for specific actions like runCommand. The second part requires wrapping in a request to execute.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $Token | Azure access token for authentication | 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik...' |
| $URI | Endpoint for resources or permissions (update subscription ID, RG-NAME, RESOURCE) | 'https://management.azure.com/subscriptions/.../resources?api-version=2020-10-01' |
| <RG-NAME> | Name of the target resource group | 'myResourceGroup' |
| <RESOURCE> | Name of the virtual machine | 'myVM' |

## Usage

Run the first block to enumerate resources, then adapt the second URI into a full request for permission details. Ideal for identifying exploitable VMs in post-compromise scenarios.

## Detection

- Azure Resource Manager audit logs showing GET requests to /resources or /permissions endpoints.
- Anomalous PowerShell API calls from non-admin workloads.
- Token usage patterns indicating enumeration beyond expected scopes.

## Related

- [[procedures/Azure-Resource-Management-and-Privilege-Checking-with-PowerShell]]
