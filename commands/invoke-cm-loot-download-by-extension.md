---
id: d9ae7b2f-0dc5-4ab6-a7cd-99adb5369534
name: invoke-cm-loot-download-by-extension
type: command
executor: powershell
data: Invoke-CMLootDownload -InventoryFile .\sccmfiles.txt -Extension msi
output: null
created_at: '2023-04-06T03:56:08.273864+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - collection
  - sccm
verified: true
validated: true
---

# invoke-cm-loot-download-by-extension

## Command

```powershell
Invoke-CMLootDownload -InventoryFile $_INVENTORY_FILE -Extension $_EXTENSION
```

## Description

This PowerShell command bulk-downloads files from an SCCM share based on an inventory file and file extension filter using the CMLoot module. Useful for collecting all instances of a type, like MSI packages, to maximize data yield.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -InventoryFile ($_[INVENTORY_FILE]) | Path to the inventory text file (e.g., .\sccmfiles.txt) | Yes |
| -Extension ($_[EXTENSION]) | File extension to filter (e.g., msi, xml) | Yes |

## Examples

### Basic Usage

```powershell
Invoke-CMLootDownload -InventoryFile .\sccmfiles.txt -Extension msi
```

### Advanced Usage

```powershell
Invoke-CMLootDownload -InventoryFile C:\Temp\inventory.txt -Extension xml
```

## Expected Output

Messages like "Processing inventory... Downloading 5 MSI files..." and a summary: "Downloaded: app1.msi, app2.msi". Files save to current dir or subfolder; use dir to list.

## Related

- [[procedures/Active-Directory-SCCM-Loot-Inventory-and-Download]]
- [[commands/invoke-cm-loot-inventory]]
