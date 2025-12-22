---
id: c3a562f5-8d68-4fd8-baed-93c7253a4d71
name: invoke-enumerate-azure-subdomains
type: command
executor: powershell
data: |-
  . C:\Tools\MicroBurst\Misc\InvokeEnumerateAzureSubDomains.ps1
  Invoke-EnumerateAzureSubDomains -Base $_TENANT_NAME -Verbose
output: |-
  Subdomain Service
  --------- -------
  $_TENANT_NAME.mail.protection.outlook.com Email
  $_TENANT_NAME.onmicrosoft.com Microsoft Hosted Domain
created_at: '2023-05-23T16:51:26.151206+00:00'
updated_at: '2023-05-23T16:51:26.181993+00:00'
platforms:
  - Cloud
tags:
  - azure
  - enumeration
  - reconnaissance
verified: true
validated: true
---

# invoke-enumerate-azure-subdomains

## Command

```powershell
. C:\Tools\MicroBurst\Misc\InvokeEnumerateAzureSubDomains.ps1
Invoke-EnumerateAzureSubDomains -Base $_TENANT_NAME -Verbose
```

## Description

This command loads the InvokeEnumerateAzureSubDomains script from the MicroBurst toolkit and executes it to enumerate subdomains associated with an Azure tenant. It performs passive DNS queries to identify common Azure services linked to the tenant, useful for initial reconnaissance in cloud environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TENANT_NAME | The base name of the Azure AD tenant (e.g., 'contoso' for contoso.onmicrosoft.com) | Yes |
| -Base | Specifies the tenant base for subdomain queries (aliased to $_TENANT_NAME) | Yes |
| -Verbose | Enables detailed output showing query progress and additional information | No |

## Examples

### Basic Usage

```powershell
. C:\Tools\MicroBurst\Misc\InvokeEnumerateAzureSubDomains.ps1
Invoke-EnumerateAzureSubDomains -Base contoso -Verbose
```

### Usage with Output Export

```powershell
Invoke-EnumerateAzureSubDomains -Base contoso -Verbose | Out-File -FilePath azure-subdomains.txt
```

## Expected Output

A table listing discovered subdomains and their services:

```
Subdomain Service
--------- -------
contoso.mail.protection.outlook.com Email
contoso.onmicrosoft.com Microsoft Hosted Domain
```

If no subdomains are found, check the tenant name or network connectivity for DNS resolution.

## Related

- [[procedures/Enumerate-Azure-Subdomains-with-MicroBurst]]
- [[tools/MicroBurst]]
