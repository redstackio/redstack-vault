---
id: 6580fffa-5e74-4fa0-b8f9-1194757aca13
name: aspdotnetwrapper-decode-mac
type: command
executor: bash
data: >-
  AspDotNetWrapper.exe --keypath $_KEYPATH --encrypteddata "$_VIEWSTATE_DATA"
  --purpose=viewstate --modifier="$_MODIFIER" --macdecode
output: null
created_at: '2023-04-06T03:55:53.378606+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - viewstate
  - asp-net
  - decryption
  - mac
verified: true
validated: true
---

# aspdotnetwrapper-decode-mac

## Command

```bash
AspDotNetWrapper.exe --keypath $_KEYPATH --encrypteddata "$_VIEWSTATE_DATA" --purpose=viewstate --modifier="$_MODIFIER" --macdecode
```

## Description

This command uses AspDotNetWrapper to decode the Message Authentication Code (MAC) and decrypt ASP.NET ViewState using a provided machine key file. It targets encrypted data in web applications, allowing extraction of sensitive serialized objects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --keypath | Path to the machine key file (e.g., web.config snippet with keys) | Yes |
| $_KEYPATH | File path for machine keys (e.g., MachineKeys.txt) | Yes |
| --encrypteddata | Base64-encoded encrypted data (e.g., __VIEWSTATE) | Yes |
| $_VIEWSTATE_DATA | The actual encrypted ViewState string | Yes |
| --purpose | Purpose of the data (e.g., viewstate, cookie) | Yes |
| --modifier | __VIEWSTATEGENERATOR value from the application | No |
| $_MODIFIER | Modifier string if present | No |
| --macdecode | Flag to decode and validate the MAC | Yes |

## Examples

### Basic Usage

```bash
AspDotNetWrapper.exe --keypath MachineKeys.txt --encrypteddata "base64_viewstate" --purpose=viewstate --macdecode
```

### Advanced Usage

With modifier for specific ViewState:
```bash
AspDotNetWrapper.exe --keypath MachineKeys.txt --encrypteddata "encrypted_data" --purpose=viewstate --modifier="generator_value" --macdecode
```

## Expected Output

```
MAC Validated: True
Decrypted Data: [serialized .NET object or plaintext]
```
Errors may indicate invalid keys or mismatched algorithms.

## Related

- [[Related Procedure]]: [[procedures/Exploit-IIS-Machine-Key-via-API-Key-Leaks]]
- [[Related Tool]]: [[tools/aspdotnetwrapper]]
