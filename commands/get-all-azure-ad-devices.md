---
id: e5bd6ed5-fb5c-4c57-83a0-f249aab9a3c7
name: get-all-azure-ad-devices
type: command
executor: powershell
data: Get-AzureADDevice
output: null
created_at: '2023-05-23T19:33:22.166794+00:00'
updated_at: '2023-05-23T19:33:22.785549+00:00'
platforms:
  - Cloud
tags:
  - azure-ad
  - enumeration
  - devices
verified: true
validated: true
---

# Get All Azure AD Devices

## Command

```powershell
Get-AzureADDevice
```

## Description

Retrieves all devices registered in Azure AD, such as workstations and mobiles, for inventory assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (None) | Default retrieves all accessible devices | No |

## Examples

### Basic Usage

```powershell
Get-AzureADDevice
```

### Advanced Usage

Filter joined devices: Get-AzureADDevice | Where-Object {$_.JoinType -eq "AzureADJoined"}

## Expected Output

ObjectId                             DisplayName    DeviceOSType OperatingSystemVersion
--------                             -----------    ----------- ----------------------
33333333-...                        WORKSTATION-01 Windows      10.0.19041
44444444-...                        MOBILE-01      iOS          15.0

## Related

- [[procedures/azure-ad-enumeration-using-powershell-with-credentials]]
