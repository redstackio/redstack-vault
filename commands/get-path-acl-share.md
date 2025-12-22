---
id: f12f8943-cf23-4ffb-be2d-3e230a502872
type: command
executor: powershell
data: Get-PathAcl -Path \"\\$_PATH\\Of\\Share\"
output: null
created_at: '2023-04-06T03:56:02.230676+00:00'
updated_at: '2023-04-06T21:33:38.759173+00:00'
platforms:
  - Windows
tags:
  - recon
  - ad
verified: true
validated: true
---

# Check ACLs for Specified Path

## Command

```powershell
Get-PathAcl -Path "\\$_PATH\Of\Share"
```

## Description

Gets ACLs for a file share path.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Path | Share path (e.g., '\\server\share') | Yes |

## Examples

### Basic Usage

```powershell
Get-PathAcl -Path '\\SERVER\Share'
```

## Expected Output

Path ACL entries.

## Related

- [[procedures/Active-Directory-Recon-with-PowerView]]
