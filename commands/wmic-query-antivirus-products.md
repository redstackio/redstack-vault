---
id: 7b8e774e-b67a-4490-96a3-746fe8a62b24
name: wmic-query-antivirus-products
type: command
executor: cmd
data: >-
  WMIC /Node:localhost /Namespace:\\root\SecurityCenter2 Path AntivirusProduct
  Get displayName
output: null
created_at: '2023-04-06T03:56:28.745109+00:00'
updated_at: '2023-04-10T20:37:53.522638+00:00'
platforms:
  - Windows
tags:
  - discovery
  - antivirus
  - wmi
verified: true
validated: true
---

# wmic-query-antivirus-products

## Command

```cmd
WMIC /Node:$_TARGET_NODE /Namespace:\\root\SecurityCenter2 Path AntivirusProduct Get $_PROPERTIES
```

## Description

This command uses WMIC to query the Windows Security Center for installed antivirus products, retrieving their display names or other properties. It is useful for discovering endpoint protection software during reconnaissance or to plan evasion tactics in privilege escalation scenarios. Run from an elevated Command Prompt on Windows systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_NODE | Target computer name or IP (e.g., 'localhost' for local, 'remote-host' for remote) | Yes |
| $_PROPERTIES | WMI properties to retrieve (e.g., 'displayName' for names, 'displayName,productState' for names and status) | Yes |
| /Namespace:\\root\SecurityCenter2 | Specifies the WMI namespace for security products (fixed) | Built-in |
| /Node:$_TARGET_NODE | Specifies the target machine for the query | Built-in |
| Path AntivirusProduct | WMI class for antivirus products (fixed) | Built-in |
| Get $_PROPERTIES | Retrieves the specified properties | Built-in |

## Examples

### Basic Usage (Local Query for Display Names)

```cmd
WMIC /Node:localhost /Namespace:\\root\SecurityCenter2 Path AntivirusProduct Get displayName
```

### Advanced Usage (Remote Query with Status)

```cmd
WMIC /Node:remote-server /Namespace:\\root\SecurityCenter2 Path AntivirusProduct Get displayName,productState /format:table
```

## Expected Output

A list or table of installed AV products. For example:

```
displayName                  
Windows Defender Antivirus   

```

Or with status:

```
displayName                  productState
Windows Defender Antivirus   397568      
```

(productState values: 0x10000 = Enabled, real-time protection on; check Microsoft docs for full decoding). If no output beyond headers, no registered AV is present.

## Related

- [[procedures/Enumerate-Installed-Antivirus-Products-Windows]] (procedure that uses this command)
- [[techniques/Security Software Discovery|T1063]] (MITRE technique)
