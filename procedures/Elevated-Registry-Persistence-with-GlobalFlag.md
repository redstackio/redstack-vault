---
id: 6519db60-e033-484a-b170-7c6ab82c1afb
name: Elevated-Registry-Persistence-with-GlobalFlag
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.052393+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - >-
    [[techniques/Event-Triggered-Execution-Image-File-Execution-Options|T1546.012
    - Event Triggered Execution: Image File Execution Options]]
sub_techniques: []
tags:
  - '[[tags/Elevated]]'
  - '[[tags/GlobalFlag]]'
  - '[[tags/Registry-HKLM]]'
  - '[[tags/Windows-Persistence]]'
commands:
  - '[[commands/reg-add-globalflag-for-notepad]]'
  - '[[commands/reg-add-reportingmode-for-notepad]]'
  - '[[commands/reg-add-monitorprocess-for-notepad]]'
platforms:
  - Windows
tools: []
validated: true
---

# Elevated-Registry-Persistence-with-GlobalFlag

## Summary

This procedure establishes persistence on a Windows system by configuring silent process exit monitoring for a target process like Notepad.exe. It modifies registry keys under Image File Execution Options and SilentProcessExit to trigger execution of a malicious binary whenever the monitored process exits silently, ensuring the payload relaunches even after user logoff.

## Description

Silent process exit monitoring leverages Windows registry settings to detect when a specified process (e.g., notepad.exe) exits without proper termination, such as due to crashes or kills. By setting the GlobalFlag to 512 in the Image File Execution Options key, monitoring is enabled. Additional keys under SilentProcessExit specify reporting mode and the monitoring executable (a malicious payload). This creates a persistent mechanism where the payload executes repeatedly, ideal for maintaining access in post-exploitation scenarios on domain-joined or standalone Windows machines. The technique requires administrative privileges and targets HKLM registry hive, making it stealthy as it hijacks a common benign process.

## Requirements

1. Administrative (elevated) privileges on the target Windows system
2. Access to a malicious executable (e.g., placed at C:\temp\evil.exe) for the monitoring process
3. Windows operating system (tested on Windows 10/11 and Server editions)

## Defense

- Restrict registry modification access via Group Policy to prevent unauthorized changes to HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options and SilentProcessExit keys
- Monitor registry for additions or modifications using tools like Sysmon (Event ID 13) or Windows Event Logs for process creation tied to unusual registry triggers
- Deploy endpoint detection and response (EDR) solutions to alert on suspicious process launches from notepad.exe exits or GlobalFlag changes
- Regularly audit Image File Execution Options for non-standard values like GlobalFlag=512

## Objectives

1. Establish persistent execution of a malicious payload triggered by the exit of a monitored benign process
2. Maintain access across user logoffs or system restarts without relying on traditional startup folders
3. Evade basic detection by masquerading as legitimate process monitoring behavior

## Instructions

### Step 1: Enable GlobalFlag for Silent Process Exit Monitoring

**Context**: This step sets the GlobalFlag DWORD value to 512 in the Image File Execution Options key for notepad.exe, activating silent process exit monitoring. This is the foundational registry change that enables the persistence mechanism.

**Command** ([[commands/reg-add-globalflag-for-notepad]]):
```cmd
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe" /v GlobalFlag /t REG_DWORD /d 512
```

> This command creates the necessary subkey if it doesn't exist and adds the GlobalFlag value. Run it from an elevated Command Prompt or PowerShell. Verify success by checking the registry key exists and the value is set to 512 (decimal).

### Step 2: Configure Reporting Mode for Silent Exits

**Context**: With monitoring enabled, this step adds the ReportingMode DWORD value set to 1 under the SilentProcessExit subkey for notepad.exe. This ensures that silent exits are reported and trigger the monitoring action, rather than being ignored.

**Command** ([[commands/reg-add-reportingmode-for-notepad]]):
```cmd
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\notepad.exe" /v ReportingMode /t REG_DWORD /d 1
```

> Execute this in an elevated shell. If the subkey doesn't exist, it will be created. Confirm by querying the registry: `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\notepad.exe" /v ReportingMode`. Expected value: 0x1 (1).

### Step 3: Specify the Monitoring Executable

**Context**: Finally, set the MonitorProcess string value to the path of your malicious executable. This defines what runs when notepad.exe exits silently, completing the persistence loop. Ensure the payload (e.g., evil.exe) is already staged on the system.

**Command** ([[commands/reg-add-monitorprocess-for-notepad]]):
```cmd
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\notepad.exe" /v MonitorProcess /d "C:\temp\evil.exe"
```

> Run from elevated prompt. The value is a REG_SZ type by default. Test by launching and killing notepad.exe (e.g., via Task Manager); the payload should execute. Verify with `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\notepad.exe" /v MonitorProcess` showing the path.

### Step 4: Verification and Testing

**Context**: Validate the persistence by simulating a silent exit of notepad.exe and observing if the payload launches. This confirms the chain is active without external tools.

**Instructions**: Open notepad.exe, then use Taskkill to force-close it: `taskkill /f /im notepad.exe`. Monitor for execution of C:\temp\evil.exe using Process Explorer or Task Manager. If successful, the payload runs on exit.

> If the payload doesn't trigger, check registry values and ensure elevated privileges were used. Decision point: If notepad.exe is not suitable (e.g., rarely used), adapt for another process like explorer.exe, but test thoroughly to avoid system instability.
