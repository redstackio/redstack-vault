---
type: procedure
description: >-
  Utilizes Cobalt Strike's Beacon to execute a .NET assembly remotely in memory
  for post-exploitation tasks.
verified: true
submitted: false
created_at: '2023-04-06T03:56:16.527966+00:00'
updated_at: '2023-04-10T20:36:23.206608+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral-Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Distributed-Component-Object-Model|T1175 - Distributed
    Component Object Model]]
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques: []
tags:
  - '[[tags/Cobalt-Strike]]'
  - '[[tags/.NET-remote-execution]]'
  - '[[tags/PowerShell-and-.NET]]'
commands:
  - '[[commands/cobalt-strike-execute-assembly]]'
tools:
  - '[[tools/Cobalt-Strike]]'
platforms:
  - Windows
validated: true
---

# Execute-NET-Assembly-via-Cobalt-Strike-Beacon

## Summary

This procedure uses Cobalt Strike's Beacon post-exploitation module to execute a .NET program remotely on a compromised Windows host. By loading the assembly directly into memory via PowerShell reflection, it enables attackers to run custom .NET tools for tasks like privilege escalation or lateral movement without writing files to disk, evading common detection mechanisms.

## Description

In a post-exploitation scenario, after gaining initial foothold via a Beacon implant, attackers leverage the 'execute-assembly' command to run .NET executables in the target's memory space. This technique relies on .NET's reflection capabilities, often invoked through PowerShell, to load and invoke the assembly. It's particularly effective in enterprise environments with Active Directory, where tools like Rubeus.exe can be executed for Kerberos attacks. The method supports both local execution on the beaconed host and remote execution across the network, aligning with defense evasion by avoiding disk artifacts and traditional process creation monitoring. Prerequisites include an active Beacon session and access to the .NET binary, which can be staged over the C2 channel.

## Requirements

1. Active Cobalt Strike team server with operator access.
2. Established Beacon session on the target Windows host (e.g., via initial exploit or phishing).
3. .NET executable (e.g., compiled C# tool like Rubeus.exe) available on the attacker's system or staged to the target.
4. PowerShell execution policy allowing script execution on the target (or bypass techniques if restricted).

## Defense

Defensive measures and detection strategies:

- Monitor PowerShell logs for reflection and assembly loading events (e.g., Event ID 4104 for module loads).
- Deploy EDR solutions to detect in-memory .NET execution and anomalous child processes from legitimate binaries like powershell.exe.
- Enforce application whitelisting and restrict unsigned .NET assemblies via tools like AppLocker or Windows Defender Application Control.
- Network segmentation and C2 beaconing detection to prevent initial Beacon implantation.

## Objectives

1. Execute arbitrary .NET code on a remote host without disk persistence.
2. Facilitate post-exploitation activities such as credential dumping or privilege escalation.
3. Maintain operational security by minimizing forensic footprints on the target system.

## Instructions

### Step 1: Prepare the .NET Assembly

**Context**: Ensure the .NET executable is ready for execution. This could involve compiling a custom tool or downloading a known one like Rubeus for Kerberos operations. Stage the binary to the attacker's Cobalt Strike client if not local.

Use [[tools/Cobalt-Strike]] to upload the assembly via the Beacon if needed, but for execute-assembly, the path can be local to the operator or remote.

### Step 2: Execute the Assembly via Beacon

**Context**: From the Cobalt Strike client console, interact with the Beacon session and issue the execute-assembly command. This loads the .NET binary into the target's memory using PowerShell and executes its entry point, returning output over the C2 channel.

**Command** ([[commands/cobalt-strike-execute-assembly]]):
```powershell
beacon > execute-assembly /path/to/assembly.exe [arguments]
```

> This command tasks the Beacon to run the specified .NET assembly. Replace `/path/to/assembly.exe` with the local path to your binary (e.g., `/home/user/Rubeus.exe`) and add any required arguments. The Beacon will download the assembly if remote, load it via reflection, and execute. Expected output includes task confirmation, data transfer size, and the program's stdout, such as banner text or results from the tool. If successful, no errors like 'assembly not found' appear, and results are displayed in the console.

### Step 3: Verify Execution and Handle Output

**Context**: Review the returned output for success. If the assembly performs actions like dumping credentials, parse the results for further use. Monitor for any errors indicating policy restrictions or AV interference.

Check the Beacon console for the received output section. If the tool ran successfully (e.g., Rubeus version banner), proceed to next objectives like using extracted tickets.
