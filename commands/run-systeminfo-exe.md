---
id: systeminfo-exe-run
data: 'C:\Program Files\Common Files\Acronis\AdvReport\systeminfo.exe'
tags:
  - trigger
  - execution
type: command
output: >-
  System information output (if any), but primarily triggers DLL loading for
  hijacking
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.843Z'
verified: false
validated: true
submitted: true
---
# run-systeminfo-exe

## Command

```cmd
C:\Program Files\Common Files\Acronis\AdvReport\systeminfo.exe
```

## Description

This command executes the Acronis systeminfo.exe utility, which gathers system details but vulnerably loads DLLs via search order, making it ideal for triggering hijacking payloads in privilege escalation attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Runs the executable directly; no flags specified in the attack | Yes |

## Examples

### Basic Usage

```cmd
C:\Program Files\Common Files\Acronis\AdvReport\systeminfo.exe
```

### Advanced Usage

Run with monitoring:

```cmd
start procmon.exe & C:\Program Files\Common Files\Acronis\AdvReport\systeminfo.exe
```

## Expected Output

Console output may include system hardware/software details, but the key effect is the DLL load attempt on snapapi.dll from PATH, enabling hijack if malicious file is present. No errors if hijack succeeds; payload executes silently.

## Related

- [[Related Procedure: Trigger-DLL-Hijacking-for-Escalation]]
