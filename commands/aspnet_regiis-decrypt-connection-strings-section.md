---
type: command
executor: cmd
data: >-
  aspnet_regiis -pdf "connectionStrings" "." -prov
  "DataProtectionConfigurationProvider"
output: null
created_at: '2023-04-06T03:55:51.711373+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - iis
  - decryption
  - credentials
verified: true
validated: true
---

# aspnet_regiis-decrypt-connection-strings-section

## Command

```cmd
aspnet_regiis -pdf "connectionStrings" "." -prov "DataProtectionConfigurationProvider"
```

## Description

This command decrypts a specified protected configuration section (e.g., connectionStrings) in an ASP.NET web.config file using the Data Protection API (DPAPI) provider. It modifies the file in place to reveal plaintext content, useful for extracting embedded credentials during post-exploitation on an IIS server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -pdf | Flag to decrypt the specified section | Yes |
| "connectionStrings" | Name of the configuration section to decrypt (e.g., connectionStrings, appSettings) | Yes |
| "." | Path to the directory containing the config file ("." for current directory, targeting web.config) | Yes |
| -prov "DataProtectionConfigurationProvider" | Specifies the DPAPI provider for decryption (machine-level or user-level context required) | Yes |

## Examples

### Basic Usage

Decrypt connectionStrings in the current web app directory:

```cmd
aspnet_regiis -pdf "connectionStrings" "." -prov "DataProtectionConfigurationProvider"
```

### Advanced Usage

Decrypt appSettings section in a specific path:

```cmd
aspnet_regiis -pdf "appSettings" "C:\inetpub\wwwroot\myapp" -prov "DataProtectionConfigurationProvider"
```

## Expected Output

The command runs silently with no stdout if successful (error if section not protected or access denied). Verify by opening web.config; the section appears in plaintext, e.g.:

```xml
<connectionStrings>
  <add name="MyDB" connectionString="Data Source=server;Initial Catalog=db;User ID=user;Password=pass" />
</connectionStrings>
```

If failed: Error message like "The configuration section 'connectionStrings' was not encrypted." or access denied.

## Related

- [[procedures/IIS-Machine-Key-Exploitation]]
- [[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]
