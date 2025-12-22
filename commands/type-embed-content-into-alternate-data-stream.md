---
id: ab7d6336-9462-43fe-b6ad-d1756d133b2b
type: command
executor: command_prompt
data: 'type $_EMBEDDED_FILE > $_COVER_FILE:$_STREAM_NAME'
output: 'C:\Users\Bob\Desktop>type hidden.txt > normal.txt:secret'
created_at: '2019-11-22T17:24:23.001983+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - Obfuscation
  - File-System
verified: true
validated: true
---

# type-embed-content-into-alternate-data-stream

## Command

```cmd
type $_EMBEDDED_FILE > $_COVER_FILE:$_STREAM_NAME
```

## Description

This Command Prompt command uses the type utility to read the contents of an embedded file and redirect it into a named alternate data stream (ADS) attached to a cover file. ADS allows hiding data within NTFS files without changing the visible file size or properties, making it a stealthy method for storing payloads, credentials, or scripts during security assessments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_EMBEDDED_FILE | Path to the source file whose contents will be embedded (e.g., C:\temp\hidden.txt) | Yes |
| $_COVER_FILE | Path to the host (cover) file where the ADS will be created (e.g., C:\temp\normal.txt) | Yes |
| $_STREAM_NAME | Name of the ADS stream (e.g., secret or :hidden_payload) | Yes |

## Examples

### Basic Usage

Embed the contents of a secret file into an ADS on a normal text file:

```cmd
type C:\temp\secret.txt > C:\temp\normal.txt:hidden
```

### Advanced Usage

Embed direct text content using echo as an alternative, though type is used for file-based embedding:

```cmd
echo "Hidden payload" > C:\temp\normal.txt:secret
```

For file embedding with type:

```cmd
type C:\path\to\payload.exe > C:\innocent\document.doc:malware
```

## Expected Output

The command executes silently with no console output if successful. The cover file's size and directory listing remain unchanged, but the ADS content is now hidden within it.

For example:

```
C:\Users\Bob\Desktop>type hidden.txt > normal.txt:secret
```

(No visible output; verify ADS creation with `dir /R` or PowerShell `Get-Item -Stream *`.)

## Related

- [[procedures/Embed-Alternate-Data-Stream-in-File]]
- [[commands/powershell-add-content-to-ads]]
