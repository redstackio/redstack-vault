---
id: 77564bb4-3850-4738-a0fa-ca946ef4ed89
name: powershell-add-content-to-ads
type: command
executor: powershell
data: >-
  Add-Content -Path $_COVER_FILE -Value (Get-Content $_EMBEDDED_FILE) -Stream
  $_STREAM_NAME -Encoding UTF8
output: >-
  PS C:\Users\Bob\Desktop> Add-Content -Path normal.txt -Value (Get-Content
  hidden.txt) -Stream secret -Encoding UTF8
created_at: '2019-11-26T17:51:06.858904+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - obfuscation
  - file-system
verified: true
validated: true
---

# powershell-add-content-to-ads

## Command

```powershell
Add-Content -Path $_COVER_FILE -Value (Get-Content $_EMBEDDED_FILE) -Stream $_STREAM_NAME -Encoding UTF8
```

## Description

This PowerShell command embeds the content of a source file into an alternate data stream (ADS) attached to a cover file on an NTFS volume. It is used for hiding data in Windows environments to evade detection during defense evasion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_COVER_FILE | Path to the host file where the ADS will be attached (e.g., normal.txt) | Yes |
| $_EMBEDDED_FILE | Path to the file whose content will be hidden in the ADS (e.g., hidden.txt) | Yes |
| $_STREAM_NAME | Name of the ADS stream (e.g., secret) | Yes |
| -Encoding UTF8 | Specifies UTF8 encoding for the content; use ASCII or Unicode as alternatives | No |

## Examples

### Basic Usage

```powershell
Add-Content -Path C:\temp\normal.txt -Value (Get-Content C:\temp\secret.txt) -Stream hidden
```

### Advanced Usage

```powershell
Add-Content -Path $_COVER_FILE -Value "Direct hidden text here" -Stream $_STREAM_NAME -NoNewline
```

This variation embeds direct text instead of file content.

## Expected Output

The command executes silently with no output if successful. Verify with Get-Item -Path $_COVER_FILE -Stream * to see the new stream listed.

For example:

```
PS C:\Users\Bob\Desktop> Add-Content -Path normal.txt -Value (Get-Content hidden.txt) -Stream secret -Encoding UTF8
```

(No console output; success confirmed via verification command.)

## Related

- [[procedures/Embed-Alternate-Data-Stream-in-File]]
- [[commands/cmd-type-to-ads]]
