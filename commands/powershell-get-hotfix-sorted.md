---
id: 11bdb499-96f7-40b2-ae8c-40cde2548b89
type: command
executor: powershell
data: Get-HotFix | Sort-Object HotFixID
output: >-
  Source        Description      HotFixID      InstalledBy          InstalledOn

  ------        -----------      --------      -----------          -----------

  BOB-PC        Security Update  KB4503308                          7/9/2019
  12:00:00 AM

  BOB-PC        Update           KB4506472                          7/9/2019
  12:00:00 AM

  BOB-PC        Security Update  KB4509096                          7/9/2019
  12:00:00 AM

  BOB-PC        Security Update  KB4515383     NT AUTHORITY\SYSTEM  10/5/2019
  12:00:00 AM

  BOB-PC        Update           KB4515871     NT AUTHORITY\SYSTEM  10/5/2019
  12:00:00 AM

  BOB-PC        Security Update  KB4516115     NT AUTHORITY\SYSTEM  10/5/2019
  12:00:00 AM

  BOB-PC        Update           KB4517389     NT AUTHORITY\SYSTEM  10/21/2019
  12:00:00 AM

  BOB-PC        Security Update  KB4520390     NT AUTHORITY\SYSTEM  10/5/2019
  12:00:00 AM

  BOB-PC        Security Update  KB4521863     NT AUTHORITY\SYSTEM  10/14/2019
  12:00:00 AM
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - Enumeration
verified: true
validated: true
---

# powershell-get-hotfix-sorted

## Command

```powershell
Get-HotFix | Sort-Object HotFixID
```

## Description

This PowerShell command retrieves all installed hotfixes on the system and sorts them alphabetically by HotFixID for easy review. It's effective for identifying patch status in discovery operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Get-HotFix | Retrieves hotfix info from registry | Yes (built-in) |
| Sort-Object HotFixID | Sorts output by HotFixID | Yes |

## Examples

### Basic Usage

```powershell
Get-HotFix | Sort-Object HotFixID
```

### Advanced Usage

Filter recent installs:
```powershell
Get-HotFix | Where-Object InstalledOn -gt (Get-Date).AddDays(-30) | Sort-Object HotFixID
```

## Expected Output

A sorted table of hotfixes:

Source        Description      HotFixID      InstalledBy          InstalledOn
------        -----------      --------      -----------          -----------
BOB-PC        Security Update  KB4503308                          7/9/2019 12:00:00 AM
BOB-PC        Update           KB4506472                          7/9/2019 12:00:00 AM
BOB-PC        Security Update  KB4509096                          7/9/2019 12:00:00 AM
BOB-PC        Security Update  KB4515383     NT AUTHORITY\SYSTEM  10/5/2019 12:00:00 AM
... (additional entries)

## Related

- [[procedures/search-windows-installed-patches-hotfixes]]
