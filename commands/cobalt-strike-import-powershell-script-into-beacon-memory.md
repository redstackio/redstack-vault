---
id: d05a17e5-776f-4128-9432-983331c49f97
name: cobalt-strike-import-powershell-script-into-beacon-memory
type: command
executor: bash
data: powershell-import /path/to/script.ps1
output: null
created_at: '2023-04-06T03:56:16.489500+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - cobalt-strike
  - powershell
verified: true
validated: true
---

# Cobalt Strike Import PowerShell Script into Beacon Memory

## Command

```bash
powershell-import /path/to/script.ps1
```

## Description

This Cobalt Strike Beacon command imports a PowerShell (.ps1) script from the team server into the Beacon's in-memory storage, allowing subsequent execution without repeated downloads. Use this in an established Beacon session to prepare scripts for stealthy operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/path/to/script.ps1` | Relative path on the team server to the .ps1 file | Yes |

## Examples

### Basic Usage

```bash
powershell-import /scripts/discovery.ps1
```

Imports `discovery.ps1` from the scripts directory on the team server.

### Advanced Usage

```bash
powershell-import /user_scripts/custom-toolkit.ps1
```

For a nested directory structure.

## Expected Output

Beacon console shows: "[*] Script imported: /path/to/script.ps1" followed by any errors if the file is missing or invalid. No output from the script itself at this stage.

## Related

- [[commands/cobalt-strike-execute-powershell-script]]
- [[procedures/powershell-script-execution-with-cobalt-strike]]
