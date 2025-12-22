---
type: command
executor: cmd
data: >-
  psexec.exe @$_TARGETS_FILE -u $_USERNAME -p $_PASSWORD $_COMMAND >
  $_OUTPUT.csv
output: null
platforms:
  - Windows
tags:
  - psexec
  - remote-execution
  - multi-target
verified: true
validated: true
---

# psexec-execute-on-multiple-targets-from-file

## Command

```cmd
psexec.exe @$_TARGETS_FILE -u $_USERNAME -p $_PASSWORD $_COMMAND > $_OUTPUT.csv
```

## Description

Runs a command across multiple remote Windows hosts listed in a file, authenticating with credentials and logging results to CSV. Ideal for batch lateral movement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @$_TARGETS_FILE | File with one target per line (e.g., targets.txt) | Yes |
| -u $_USERNAME | Username | Yes |
| -p $_PASSWORD | Password | Yes |
| $_COMMAND | Command to run on each | Yes |
| > $_OUTPUT.csv | Output file for results | No |

## Examples

### Basic Usage

Create targets.txt:

192.168.1.100
192.168.1.101

Then:
```cmd
psexec.exe @targets.txt -u admin -p pass cmd.exe /c hostname > results.csv
```

## Expected Output

CSV with host-specific outputs, e.g.:

Connecting to 192.168.1.100...
TARGET1

Connecting to 192.168.1.101...
TARGET2

## Related

- [[procedures/windows-impacket-psexec-remote-execution-with-credentials]]
- [[tools/PSExec]]
