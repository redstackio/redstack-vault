---
type: command
executor: powershell
data: >-
  Get-AzureADApplication -All $true | ForEach-Object {try
  {Get-AzureADApplicationProxyApplication -ObjectId $_.ObjectID; $_.DisplayName;
  $_.ObjectID} catch {}}
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Azure AD
tags:
  - discovery
  - azure
verified: true
validated: true
---

# Enumerate Azure AD Applications with Proxy

## Command

```powershell
Get-AzureADApplication -All $true | ForEach-Object {try {Get-AzureADApplicationProxyApplication -ObjectId $_.ObjectID; $_.DisplayName; $_.ObjectID} catch {}}
```

## Description

This PowerShell command enumerates all Azure AD applications and identifies those configured with Application Proxy by querying proxy details. It outputs proxy configurations, display names, and Object IDs for matching applications, skipping non-proxy apps silently.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -All | Retrieves all applications (not just current user's) | Yes (set to $true) |
| ObjectId | Internal use: Object ID of each application for proxy query | Built-in (from pipeline) |

## Examples

### Basic Usage

```powershell
Get-AzureADApplication -All $true | ForEach-Object {try {Get-AzureADApplicationProxyApplication -ObjectId $_.ObjectID; $_.DisplayName; $_.ObjectID} catch {}}
```

### Advanced Usage

Run after Connect-AzureAD; pipe to Export-Csv for logging:

```powershell
Get-AzureADApplication -All $true | ForEach-Object {try {Get-AzureADApplicationProxyApplication -ObjectId $_.ObjectID; $_.DisplayName; $_.ObjectID} catch {}} | Export-Csv -Path proxy_apps.csv -NoTypeInformation
```

## Expected Output

Proxy details for configured apps, followed by names and IDs:

```
ExternalUrl              : https://app-contoso.msappproxy.net
InternalUrl              : http://internal-app
DisplayName              : Internal App
ObjectId                 : 12345678-1234-1234-1234-123456789abc

Finance Management System
12345678-1234-1234-1234-123456789abc
```

## Related

- [[procedures/azure-application-proxy-enumeration]]
- [[commands/find-azure-ad-service-principal-by-display-name]]
