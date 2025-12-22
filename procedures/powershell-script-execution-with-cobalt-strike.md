---
id: 0ad55538-85d3-4c0e-afa3-71b441efd5db
name: powershell-script-execution-with-cobalt-strike
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:16.497331+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter/PowerShell|T1059.001 -
    PowerShell]]
  - '[[techniques/System-Time-Discovery|T1124 - System Time Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cobalt Strike]]'
  - '[[tags/Powershell and .NET]]'
  - '[[tags/Powershell commands]]'
commands:
  - '[[commands/cobalt-strike-import-powershell-script-into-beacon-memory]]'
  - '[[commands/cobalt-strike-execute-powershell-script]]'
  - '[[commands/cobalt-strike-launch-function-using-unmanaged-powershell]]'
  - '[[commands/cobalt-strike-inject-unmanaged-powershell-into-process]]'
platforms:
  - Windows
tools:
  - '[[tools/Cobalt-Strike]]'
validated: true
---

# Powershell Script Execution with Cobalt Strike

## Summary

This procedure outlines how to execute PowerShell scripts on a compromised Windows system using Cobalt Strike's Beacon payload. It leverages Cobalt Strike's built-in commands to import, execute, and inject PowerShell scripts for tasks like discovery, payload deployment, and persistence, all while maintaining a low-profile C2 channel.

## Description

In a red team engagement or attack simulation, once initial access is gained via a Beacon implant, attackers use Cobalt Strike to run PowerShell scripts remotely without spawning visible processes. This technique involves importing scripts into Beacon's memory, executing functions via managed or unmanaged PowerShell, and injecting into processes for stealthy, long-running operations. It targets Windows environments with PowerShell enabled (default on modern systems) and is effective for evading endpoint detection by avoiding direct powershell.exe invocations where possible. The procedure assumes an active Beacon session and focuses on script handling for malicious activities like data exfiltration or lateral movement.

## Requirements

1. Active Cobalt Strike team server with Beacon payload deployed on the target Windows system.
2. PowerShell v2 or later enabled on the target (default on Windows 7+).
3. Network connectivity between the target and C2 server for command execution.
4. Administrative or user-level access via the Beacon session.

## Defense

- Enable PowerShell Constrained Language Mode and script block logging to monitor execution.
- Implement application whitelisting (e.g., AppLocker) to block unsigned scripts and Cobalt Strike artifacts.
- Monitor for anomalous network connections to C2 domains and unusual PowerShell process spawns or injections.
- Use EDR tools to detect memory-based script imports and unmanaged PowerShell usage.

## Objectives

1. Import and store PowerShell scripts in Beacon memory for repeated use.
2. Execute script functions to perform discovery or payload actions on the target.
3. Run scripts stealthily without spawning powershell.exe using unmanaged methods.
4. Inject PowerShell into existing processes for persistent, low-detection execution.

## Instructions

### Step 1: Import PowerShell Script into Beacon Memory

**Context**: Begin by importing a .ps1 script from the Cobalt Strike team server into the Beacon's memory. This allows the script to be referenced later without redownloading, reducing network noise and enabling offline-like execution.

**Command** ([[commands/cobalt-strike-import-powershell-script-into-beacon-memory]]):
```bash
powershell-import /path/to/script.ps1
```

This command uploads the script to the team server and loads it into the Beacon session's memory. Verify success by checking the Beacon console for confirmation messages like "Script imported successfully." If the path is incorrect, Beacon will return an error.

### Step 2: Execute Imported PowerShell Script

**Context**: After importing, execute a specific function from the script using managed PowerShell. This downloads the script temporarily via a local TCP server setup by Beacon and runs it, capturing output back to the C2 channel. Use this for quick, one-off tasks like system discovery.

**Command** ([[commands/cobalt-strike-execute-powershell-script]]):
```bash
powershell function_name arguments
```

Replace `function_name` with the script's exported function (e.g., `Get-SystemInfo`) and `arguments` with any parameters. Expected output includes the function's results, such as system details, returned to the Beacon console. Monitor for errors like function not found, which indicates import issues.

### Step 3: Launch Function Using Unmanaged PowerShell

**Context**: For stealthier execution, use unmanaged PowerShell to run a function without launching powershell.exe, leveraging the `spawnto` configuration to specify the parent process (e.g., svchost.exe). This is ideal for evading process-based detection during lateral movement or persistence setup.

**Command** ([[commands/cobalt-strike-launch-function-using-unmanaged-powershell]]):
```bash
powerpick function_name argument
```

The command executes the function in memory using the pre-configured spawnto process. Success is indicated by the function's output in the Beacon without new process creation visible in tools like Task Manager. If the function requires arguments, provide them; otherwise, omit.

### Step 4: Inject Unmanaged PowerShell into a Process

**Context**: For long-running scripts or to blend with legitimate processes, inject unmanaged PowerShell into a target process ID (PID). This is useful for sustained operations like keylogging or monitoring without standalone process footprints.

**Command** ([[commands/cobalt-strike-inject-unmanaged-powershell-into-process]]):
```bash
psinject [pid][arch] function_name arguments
```

Specify the target PID (e.g., 1234), architecture (x86 or x64), function name, and arguments. Beacon injects and executes, returning results asynchronously. Expected output confirms injection success; failures may occur if the PID is invalid or architecture mismatches. Use tools like `ps` in Beacon to list PIDs beforehand.

### Step 5: Verify and Clean Up

**Context**: After execution, verify outputs and ensure no artifacts remain. This step confirms objectives met and minimizes detection risk.

Review Beacon console for all outputs from prior steps. If needed, use Cobalt Strike's cleanup commands or revoke sessions. Success is confirmed by achieved objectives without alerts in defensive tools.
