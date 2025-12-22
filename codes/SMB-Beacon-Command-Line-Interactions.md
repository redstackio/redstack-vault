---
id: b725fe72-cffb-4dc2-8dd6-7cee90362571
name: SMB-Beacon-Command-Line-Interactions
type: code
language: cobaltstrike
verified: true
created_at: '2023-04-06T03:56:16.338917+00:00'
updated_at: '2023-04-10T20:36:22.182970+00:00'
platforms:
  - Windows
tags:
  - c2
  - smb
  - beacon-commands
validated: true
---

# SMB-Beacon-Command-Line-Interactions

## Code

```cobaltstrike
link [host] [pipename]
connect [host] [port]
unlink [host] [PID]
jump [exec] [host] [pipe]
```

## Description

This code snippet provides the syntax for key command-line interactions within a Cobalt Strike SMB Beacon session. These commands enable connecting to named pipes, TCP ports, disconnecting processes, and injecting into new executables, all over SMB for stealthy C2 operations.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| [host] | Target hostname or IP address | 192.168.1.100 |
| [pipename] | Named pipe path | \\pipe\foo |
| [port] | TCP port number | 4444 |
| [PID] | Process ID to target | 1234 |
| [exec] | Executable path | cmd.exe |
| [pipe] | Pipe for new connection | \\pipe\bar |

## Usage

Execute these commands directly in the Cobalt Strike beacon console after establishing an SMB Beacon session. Use `link` and `connect` for initial pivots, `unlink` for cleanup, and `jump` for process migration. Ideal in Windows domain environments for lateral movement without alerting network monitors.

## Detection

- Monitor for anomalous SMB named pipe creations (e.g., via Sysmon Event ID 17/18).
- EDR alerts on unexpected process injections or connections to high ports over SMB.
- Network logs showing SMB traffic with embedded shell commands or unusual pipe activity.
- Behavioral analysis of Cobalt Strike artifacts like beacon.dll in memory.

## Related

- [[procedures/Establish-and-Interact-with-SMB-Beacon-Payload]]
- [[tools/Cobalt Strike]]
