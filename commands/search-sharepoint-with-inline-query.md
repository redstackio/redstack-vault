---
id: 3595da96-76ba-4214-8cd8-fa477993110d
name: search-sharepoint-with-inline-query
type: command
executor: powershell
data: >-
  .\SnaffPoint.exe -u "https://your.sharepoint.com" -t $token -l -q
  "filename:.config"
output: null
created_at: '2023-04-06T03:56:28.947949+00:00'
updated_at: '2023-10-10T20:37:31.881047+00:00'
platforms:
  - Windows
tags:
  - search
  - looting
  - sharepoint
  - fql
verified: true
validated: true
---

# search-sharepoint-with-inline-query

## Command

```powershell
.\SnaffPoint.exe -u "https://your.sharepoint.com" -t $token -l -q "filename:.config"
```

## Description

This command performs a targeted SharePoint search using inline FQL queries with SnaffPoint, enabling precise filtering for files like .config that may contain passwords.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | SharePoint site URL | Yes |
| -t | Bearer token | Yes |
| -l | Enable FQL (Fast Query Language) mode | Yes |
| -q | Inline search query (e.g., filename:.config) | Yes |

## Examples

### Basic Usage

```powershell
.\SnaffPoint.exe -u "https://contoso.sharepoint.com" -t $token -l -q "filename:.config"
```

### Advanced Usage

Search for password content:
```powershell
.\SnaffPoint.exe -u "https://contoso.sharepoint.com" -t $token -l -q "*password* AND filename:txt"
```

## Expected Output

Filtered search results with matches, e.g., "[MATCH] web.config at /sites/app - Snippet: connectionString password=...". Potential loot flagged for download.

## Related

- [[procedures/Password-Looting-from-SharePoint-and-SMB-Shares]]
- [[tools/SnaffPoint]]
