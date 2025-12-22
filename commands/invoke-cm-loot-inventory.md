---
id: 34d3a881-1696-4064-b34c-dacd076feaf9
name: invoke-cm-loot-inventory
type: command
executor: powershell
data: Invoke-CMLootInventory -SCCMHost sccm01.domain.local -Outfile sccmfiles.txt
output: null
created_at: '2023-04-06T03:56:08.273750+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - discovery
  - sccm
verified: true
validated: true
---

# invoke-cm-loot-inventory

## Command

```powershell
Invoke-CMLootInventory -SCCMHost $_SCCM_HOST -Outfile $_OUTFILE
```

## Description

This PowerShell command uses the CMLoot module to enumerate files available in an SCCM content library share, generating a text inventory for targeted downloads. Use it after gaining access to an AD environment to map lootable assets without immediate exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -SCCMHost ($_[SCCM_HOST]) | Hostname or FQDN of the SCCM server (e.g., sccm01.domain.local) | Yes |
| -Outfile ($_[OUTFILE]) | Path to the output text file for the inventory list (e.g., sccmfiles.txt) | Yes |

## Examples

### Basic Usage

```powershell
Invoke-CMLootInventory -SCCMHost sccm01.domain.local -Outfile sccmfiles.txt
```

### Advanced Usage

```powershell
Invoke-CMLootInventory -SCCMHost sccm01.domain.local -Outfile C:\Temp\inventory.txt
```

## Expected Output

The command outputs progress messages like "Enumerating SCCM share..." and creates a text file with lines such as:

```
\\sccm\SCCMContentLib$\DataLib\SC100001.1\x86\MigApp.xml
\\sccm\SCCMContentLib$\DataLib\SC100002.1\x64\app.msi
```

No errors if shares are accessible; otherwise, "Access denied" or connection failures.

## Related

- [[procedures/Active-Directory-SCCM-Loot-Inventory-and-Download]]
- [[commands/invoke-cm-loot-download-single-file]]
