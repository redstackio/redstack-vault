---
id: de6124e3-1936-4947-9500-2c8ee164e0f2
name: get-childitem-regex-search-powershell
type: command
executor: powershell
data: >-
  Get-ChildItem -Path $_START_PATH -Recurse | Where-Object { $_.Name -Match
  $_REGEX }
output: >-
  PS C:\Users > Get-ChildItem -Path C:\Users -Recurse | Where-Object { $_.Name
  -Match "^secret.*" }

      Directory: C:\Users\Bob\Desktop

  Mode                LastWriteTime         Length Name

  ----                -------------         ------ ----

  -a----        4/24/2020  11:23 AM              0 secretdocument.txt
created_at: '2020-04-24T18:25:00.592827+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - discovery
verified: true
validated: true
---

# get-childitem-regex-search-powershell

## Command

```powershell
Get-ChildItem -Path $_START_PATH -Recurse | Where-Object { $_.Name -Match $_REGEX }
```

## Description

This PowerShell command recursively searches for files and folders in a specified path whose names match a given regular expression pattern. It is useful for discovering sensitive or targeted items during file system enumeration in security assessments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_START_PATH | Starting directory for the search (e.g., C:\\Users or . for current) | Yes |
| -Recurse | Enables recursive traversal of subdirectories | Yes |
| $_REGEX | Regular expression pattern to match against item names (e.g., "^secret.*" for names starting with 'secret') | Yes |
| -ErrorAction SilentlyContinue | (Optional) Suppresses error messages for inaccessible directories | No |

## Examples

### Basic Usage

```powershell
Get-ChildItem -Path C:\Users -Recurse | Where-Object { $_.Name -Match "password" }
```

Searches user directories for items containing 'password' in the name.

### Advanced Usage

```powershell
Get-ChildItem -Path . -Recurse -ErrorAction SilentlyContinue | Where-Object { $_.Name -Match "^config.*\.txt$" } | Select-Object FullName, Length
```

Limits to current directory, targets config text files, and selects key properties.

## Expected Output

A list of matching FileInfo or DirectoryInfo objects in table format, showing mode, last write time, length, and name. For example:

```
PS C:\Users > Get-ChildItem -Path C:\Users -Recurse | Where-Object { $_.Name -Match "^secret.*" }

    Directory: C:\Users\Bob\Desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        4/24/2020  11:23 AM              0 secretdocument.txt
```

If no matches, returns nothing. Pipe to Format-List for detailed view.

## Related

- [[procedures/Find-Files-and-Folders-with-Regex-PowerShell]]
