---
id: 8e3c6b2f-602a-4e99-aca2-53eae9238b06
name: join-aadint-device-to-intune
type: command
executor: powershell
data: Join-AADIntDeviceToIntune -DeviceName "$_DEVICE_NAME"
output: null
created_at: '2023-04-06T03:56:15.982656+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - azure
  - intune
  - device-join
verified: true
validated: true
---

# join-aadint-device-to-intune

## Command

```powershell
Join-AADIntDeviceToIntune -DeviceName "$_DEVICE_NAME"
```

## Description

This command enrolls the specified device in Intune, linking it to the Azure AD registration for compliance simulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -DeviceName | Name of the device to enroll | Yes |

## Examples

### Basic Usage

```powershell
Join-AADIntDeviceToIntune -DeviceName "FakeDevice"
```

## Expected Output

Enrollment success:
```
Device enrolled in Intune.
ComplianceStatus : Compliant
```

## Related

- [[procedures/Bypass-Azure-Conditional-Access-via-Fake-Device-Join]]
- [[tools/AADInternals]]
