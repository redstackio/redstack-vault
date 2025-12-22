---
id: 89ada62d-b43d-4ed6-8aca-8e442524e5f6
name: sharpaztoken-join-mdm-device
type: command
executor: bash
data: >-
  SharpAzToken.exe mdm --joindevice --accesstoken $_ACCESS_TOKEN --devicename
  $_DEVICE_NAME --outpfxfile $_PFX_PATH
output: null
created_at: '2023-05-24T07:40:26.708382+00:00'
updated_at: '2023-05-24T07:40:26.785283+00:00'
platforms:
  - Cloud
tags:
  - azure
  - mdm
  - device-enrollment
verified: true
validated: true
---

# SharpAzToken Join MDM Device

## Command

```bash
SharpAzToken.exe mdm --joindevice --accesstoken $_ACCESS_TOKEN --devicename $_DEVICE_NAME --outpfxfile $_PFX_PATH
```

## Description

This command enrolls a device into Azure Mobile Device Management (MDM) using a provided access token, generating a PFX certificate file for the device. It is used in scenarios requiring device identity creation for token generation and persistent access in Azure AD environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --joindevice | Flag to initiate device join to MDM | Yes |
| --accesstoken | Azure access token for authentication (raw or base64) | Yes |
| --devicename | Unique name for the device (e.g., 'TestDevice01') | Yes |
| --outpfxfile | Output path for the generated PFX certificate file | Yes |

## Examples

### Basic Usage

```bash
SharpAzToken.exe mdm --joindevice --accesstoken eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6... --devicename CompromisedDevice --outpfxfile ./device.pfx
```

### Advanced Usage

```bash
SharpAzToken.exe mdm --joindevice --accesstoken $_ACCESS_TOKEN --devicename $_DEVICE_NAME --outpfxfile $_PFX_PATH --verbose
```

## Expected Output

Successful execution produces output like:

"Device joined successfully. PFX file saved to $_PFX_PATH"

The PFX file contains the device certificate and private key, verifiable by opening it with tools like OpenSSL: `openssl pkcs12 -info -in device.pfx`.

## Related

- [[procedures/Azure Device Management and Token Generation with SharpAzToken]]
- [[commands/sharpaztoken-generate-device-keys]]
